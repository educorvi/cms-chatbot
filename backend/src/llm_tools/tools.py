import json
from typing import Callable
from langchain.tools import Tool
import typesense
import elasticsearch

from src.llm_tools.customTypesenseRetriever import CustomTypesenseRetriever
from src.llm_tools.customElasticSearchRetriever import CustomElasticSearchRetriever



def search_documents(get_documents_func: Callable[[str], list[any]], sources: list) -> Callable[[str], str]:
    """
    Create a function that searches documents and returns the results formatted as a string that can be used as
    context for the LLM.

    Args:
        get_documents_func (Callable[[str], list[any]]): The function to use to get the documents.
        sources (list): The list to append the sources to.

    Returns:
        Callable[[str], str]: The function described above.
    """
    def func(query: str) -> str:
        """
        Search documents and return the results formatted as a string that can be used as context for the LLM.

        Args:
            query (str): The query to use to search the tool.

        Returns:
            str: The results formatted as a string.
        """
        results = get_documents_func(query)
        sources.extend(
            list(
                map(lambda d:
                    {'source': d.metadata["source"], 'title': d.metadata["title"]},
                    results
                    )
            )
        )
        ret_string = (
            "\n--------------------------------------------------------------------\n"
            .join(
                list(
                    map(lambda d:
                        "Metadata: \n" + json.dumps(d.metadata) + "\nContent: \n" + d.page_content,
                        results
                        )
                )
            ))
        return ret_string

    return func


def create_elastic_tool(es_config, sources: list):
    """
    Create an ElasticSearch tool.

    Args:
        es_config (dict): The configuration for the ElasticSearch tool.
        sources (list): The list to append the sources to.

    Returns:
        Tool: The tool.
    """
    retriever = CustomElasticSearchRetriever(
        elasticsearch.Elasticsearch(es_config["url"]),
        es_config["index"],
        es_config["result_size"],
        es_config["result_number"]
    )

    return Tool(
        name="ElasticSearch",
        func=search_documents(retriever.get_relevant_documents, sources),
        description="useful for when you need to answer questions about everything related to health and safety, "
                    "the DGUV and most other things. The Contents are in German and the search has to be done in "
                    "german as well. This tool provides access to an elasticsearch index, so formulate your query "
                    "accordingly."
    )


def create_typesense_tool(ts_conf, sources: list):
    """
    Create a Typesense tool.

    Args:
        ts_conf (dict): The configuration for the Typesense tool.
        sources (list): The list to append the sources to.

    Returns:
        Tool: The tool.
    """
    client = typesense.Client({
        'api_key': ts_conf["api_key"],
        'nodes': [
            {
                'host': ts_conf["host"],
                'port': ts_conf["port"],
                'protocol': ts_conf["protocol"]
            }
        ]
    })
    retriever = CustomTypesenseRetriever(
        client,
        ts_conf["collection"],
        ts_conf["result_size"],
        ts_conf["result_number"]
    )

    return Tool(
        name="Typesense",
        func=search_documents(retriever.get_relevant_documents, sources),
        description="useful for when you need to answer questions about everything related to health and safety, "
                    "the DGUV and most other things. The Contents are in German and the search has to be done in "
                    "german as well. This tool provides access to a typesense index, so formulate your query "
                    "accordingly.")
