import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.tools import TavilySearchResults

load_dotenv(find_dotenv(filename=".env"))


os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")



s=TavilySearchResults()

o=s.invoke("site:google.comAi")

print(o)
