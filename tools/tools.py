import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.tools import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import tool

load_dotenv(find_dotenv(filename=".env"))


os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")


@tool("Web Search tool")
def web_search(search_quary:None,max_results=7, include_images=True):
    if os.environ["TAVILY_API_KEY"] == None:
        raise ValueError("Web search can not be perform that time.")
    else:
        try:
            search=TavilySearchResults(
                max_results=max_results,
                include_images=include_images
            )

            search_results=search.invoke(input=search_quary)
        except Exception as e:
            raise Exception(e)


    return search_results
