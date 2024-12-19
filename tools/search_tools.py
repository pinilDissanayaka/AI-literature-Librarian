import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.tools import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain.tools import tool

load_dotenv(find_dotenv(filename=".env"))


os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")


@tool("Web Search tool")
def web_search(search_quary: None, max_results=7, include_images=True):
    """
    Perform a web search using the TavilySearchResults tool.

    Args:
        search_quary (None): The search query to perform.
        max_results (int): Maximum number of results to retrieve. Defaults to 7.
        include_images (bool): Whether to include images in the results. Defaults to True.

    Returns:
        list: A list of search results.

    Raises:
        ValueError: If the API key is not set.
        Exception: If any error occurs during the search.
    """
    # Check if the API key is set
    if os.environ["TAVILY_API_KEY"] is None:
        raise ValueError("Web search cannot be performed at this time.")
    
    try:
        # Initialize the search tool with the specified parameters
        search = TavilySearchResults(
            max_results=max_results,
            include_images=include_images
        )

        # Perform the search and get the results
        search_results = search.invoke(input=search_quary)
    except Exception as e:
        # Raise any exception encountered during the search
        raise Exception(e.args)

    return search_results


@tool("Wikipedia Search tool")
def wikipidia_search(query: str) -> list:
    """
    Perform a search on Wikipedia using the specified query.

    Args:
        query (str): The search query to perform on Wikipedia.

    Returns:
        list: A list of search results from Wikipedia.

    Raises:
        Exception: If any error occurs during the search.
    """
    try:
        # Initialize the Wikipedia searcher with the specified query
        wikipidia_searcher = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        
        # Perform the search and get the results
        wikipidia_search_result = wikipidia_searcher.invoke(input=query)
        
        # Return the search results
        return wikipidia_search_result
    except Exception as e:
        # Raise any exception encountered during the search
        raise ValueError(e.args)


