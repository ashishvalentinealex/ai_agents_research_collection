import os
from langchain_community.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv
load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter profile page"""
    
    if not tavily_api_key:
        raise ValueError("TAVILY_SEARCH_API key is missing. Set it in the environment variables or .env file.")

    search = TavilySearchResults(tavily_api_key=tavily_api_key)  # Pass as keyword argument
    res = search.run(f"{name}")
    return res
