import asyncio
import json
import re
import deepl
import websockets

from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

from src.helper.CallbackHandler import WebsocketCallbackHandler
from src.helper.DB_Classes import get_cost_of_current_month, Chat
from src.helper.config import get_config
from src.llm_tools.tools import create_typesense_tool, create_elastic_tool
from src.helper.translation import translate_if_target_lang


def start_backend():
    """
    Starts the backend.
    """
    conf = get_config()

    translator = None
    if conf["deepl"]["enabled"] is True:
        translator = deepl.Translator(conf["deepl"]["api_key"])

    limit = 50
    if "spending_limit" in conf["open_ai"]:
        limit = conf["open_ai"]["spending_limit"]

    sr_from = conf["source_replace"]["from"]
    sr_to = conf["source_replace"]["to"]
    sr_exp = re.compile(sr_from)

    port = conf["websocket"]["port"]
    host = "localhost"
    if "host" in conf["websocket"]:
        host = conf["websocket"]["host"]

    async def respond(websocket):
        """
        Respond to messages from the websocket.

        Args:
            websocket: The websocket to respond to.
        """
        # Create the list of sources that will be displayed along with the answer
        sources = []

        # Determine which search engine to use and create the relevant tool
        if conf["search"]["engine"] == "elasticsearch":
            tool = create_elastic_tool(conf["search"]["elasticsearch"], sources)
        elif conf["search"]["engine"] == "typesense":
            tool = create_typesense_tool(conf["search"]["typesense"], sources)
        else:
            raise Exception("Search engine not supported")
        tools = [
            tool
        ]

        # Create the memory and the database entry
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        db_entry = Chat.create()

        # Create the callback handler and initialize the agent
        handler = WebsocketCallbackHandler(websocket)
        agent = initialize_agent(
            tools,
            ChatOpenAI(
                temperature=0, openai_api_key=conf["open_ai"]["api_key"],
                model_name=conf["open_ai"]["model"],
                callbacks=[handler]
            ),
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=False,
            memory=memory,
        )

        try:
            with get_openai_callback() as cb:
                async for message in websocket:
                    # Translate the message if necessary
                    source_lang = None
                    if translator is not None:
                        trans = translator.translate_text(message, target_lang="DE")
                        message = trans.text
                        source_lang = trans.detected_source_lang
                        if source_lang == "EN":
                            source_lang = "EN-US"

                    # Check if the spending limit has been reached
                    if get_cost_of_current_month() >= limit:
                        await websocket.send(
                            json.dumps({"type": "message",
                                        "content": f"{translate_if_target_lang(translator, 'Das monatliche Limit wurde erreicht. Bitte wende dich an den Administrator.', source_lang)}"}))
                        continue

                    # Run the agent
                    prompt = message + "\n Antworte auf Deutsch verwende lediglich die gegeben Informationen. Zitiere deine Aussagen, indem du sie mit dem Index (beginnend mit 1) der Quelle versiehst, aus der die Information stammt, z.B.: 'Dies ist ein zitiertes Beispiel [i].'"
                    try:
                        task = asyncio.create_task(asyncio.to_thread(agent.run, prompt, callbacks=[handler]))
                        await task
                        result = task.result()
                        result = translate_if_target_lang(translator, result, source_lang)
                        # Add the sources to the result
                        if len(sources) > 0:
                            result += f"\n\n{translate_if_target_lang(translator, 'Gefundene Informationen:', source_lang)}"
                            index = 1
                            while len(sources) > 0:
                                s = sources.pop(0)
                                result += f"\n- [{index}] [{s['title']}]({sr_exp.sub(sr_to, s['source'])})"
                                index += 1
                    except Exception as e:
                        result = translate_if_target_lang(translator, "Es ist ein Fehler aufgetreten.",
                                                          source_lang)
                        print(e)

                    # Send the result and the usage information
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

                    # Save the usage information to the database
                    db_entry.cost = cb.total_cost
                    db_entry.tokens = cb.total_tokens
                    db_entry.save()
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed")

    async def run_websocket(port_number):
        """
        Run the websocket.

        Args:
            port_number: The port number to use.

        Returns:
            Future: The never ending future.
        """
        async with websockets.serve(respond, host, port_number):
            print(f"Started websocket server on port", port_number)
            await asyncio.Future()

    asyncio.run(run_websocket(port))
