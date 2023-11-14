import json
import os

import argparse
import websockets
from jsonschema import validate
import yaml





def start_backend():
    # Command line arguments
    parser = argparse.ArgumentParser(prog='cms-chatbot', description='Backend for the cms chatbot')
    parser.add_argument('-c', '--config', help='path to the config file', default="/etc/cms-chatbot/conf.yaml")
    args = parser.parse_args()

    # Validate config file
    schema = json.load(open(os.getcwd()+"/conf.schema.json", "r"))
    conf = yaml.safe_load(open(args.config, "r"))
    validate(instance=conf, schema=schema)

    async def respond(websocket):
        sources = []
        if conf["search"]["engine"] == "elasticsearch":
            tool = create_elastic_tool(es_url, es_index, es_result_size, es_result_number, sources)
        elif conf["search"]["engine"] == "typesense":
            tool = create_typesense_tool(ts_host, ts_port, ts_protocol, ts_api_key, ts_collection,
                                         ts_result_size, ts_result_number, sources)
        else:
            raise Exception("Search engine not supported")

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        db_entry = Chat.create()

        tools = [
            tool
        ]

        handler = WebsocketCallbackHandler(websocket)

        agent = initialize_agent(
            tools,
            ChatOpenAI(
                temperature=0, openai_api_key=open_ai_key,
                model_name=open_ai_model,
                # streaming=True,
                callbacks=[StreamingWebsocketHandler(websocket)]
            ),
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=False,
            memory=memory,
            # callbacks=[handler]
        )
        try:
            with get_openai_callback() as cb:
                async for message in websocket:
                    source_lang = None
                    if translator is not None:
                        trans = translator.translate_text(message, target_lang="DE")
                        message = trans.text
                        source_lang = trans.detected_source_lang

                    if get_cost_of_current_month() >= limit:
                        await websocket.send(
                            json.dumps({"type": "message",
                                        "content": f"{translate_if_source_lang(translator, 'Das monatliche Limit wurde erreicht. Bitte wende dich an den Administrator.', source_lang)}"}))
                        continue

                    prompt = message + "\n Antworte auf Deutsch verwende lediglich die gegeben Informationen. Zitiere deine Aussagen, indem du sie mit dem Index (beginnend mit 1) der Quelle versiehst, aus der die Information stammt, z.B.: 'Dies ist ein zitiertes Beispiel [i].'"
                    try:
                        task = asyncio.create_task(asyncio.to_thread(agent.run, prompt, callbacks=[handler]))
                        await task
                        result = task.result()
                        result = translate_if_source_lang(translator, result, source_lang)
                        if len(sources) > 0:
                            result += f"\n\n{translate_if_source_lang(translator, 'Gefundene Informationen:', source_lang)}"
                            index = 1
                            while len(sources) > 0:
                                s = sources.pop(0)
                                result += f"\n- [{index}] [{s['title']}]({sr_exp.sub(sr_to, s['source'])})"
                                index += 1
                    except Exception as e:
                        result = translate_if_source_lang(translator, "Es ist ein Fehler aufgetreten.",
                                                          source_lang)
                        print(e)
                    await websocket.send(json.dumps({"type": "message",
                                                     "content": result}))
                    await websocket.send(json.dumps({
                        "type": "usage",
                        "content": {
                            "tokens": {
                                "total": cb.total_tokens,
                                "prompt": cb.prompt_tokens,
                                "completion": cb.completion_tokens
                            },
                            "cost": cb.total_cost,
                            "successful_requests": cb.successful_requests
                        }
                    }))
                    db_entry.cost = cb.total_cost
                    db_entry.tokens = cb.total_tokens
                    db_entry.save()
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed")

    async def run_websocket(port_number):
        async with websockets.serve(respond, "0.0.0.0", port_number):
            print(f"Started websocket server on port", port_number)
            await asyncio.Future()

    asyncio.run(run_websocket(port))
