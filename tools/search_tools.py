import os
import requests
from dotenv import load_dotenv, find_dotenv
from langchain_community.tools import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain.tools import tool

load_dotenv(find_dotenv(filename=".env"))


os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")


def web_search(search_quary: str, max_results: int = 7, include_images: bool = True) -> list:
    """
    Perform a web search using the TavilySearchResults tool.

    Args:
        search_quary (str): The search query to perform.
        max_results (int): Maximum number of results to retrieve. Defaults to 7.
        include_images (bool): Whether to include images in the results. Defaults to True.

    Returns:
        list: A list of search results containing URLs.

    Raises:
        ValueError: If the API key is not set.
        Exception: If any error occurs during the search.
    """

    top_urls = []

    # Check if the API key is set
    if os.environ["TAVILY_API_KEY"] is None:
        raise ValueError(
            "The Tavily API key must be set in the environment variable TAVILY_API_KEY."
        )

    try:
        # Initialize the search tool with the specified parameters
        search = TavilySearchResults(
            max_results=max_results,
            include_images=include_images
        )

        # Perform the search and get the results
        search_results = search.invoke(input=search_quary)

        for search_result in search_results:
            top_urls.append(search_result['url'])
    except Exception as e:
        # Raise any exception encountered during the search
        raise Exception(
            "An error occurred while performing the web search. "
            "Please check the API key and try again."
        )

    return top_urls



def open_web_page(url):
    res=requests.get(url=url)

    return res.text





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
    




loader=WebBaseLoader(['https://scholar.google.com/scholar?start=10&q=sinhala+nlp&hl=en&as_sdt=0,5&as_ylo=2024'], encoding="utf-8", continue_on_failure=True)


print(loader.load())