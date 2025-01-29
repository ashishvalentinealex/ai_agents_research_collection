import os 
import requests
from dotenv import load_dotenv 

load_dotenv()

# FUNCTION TO SCRAPE LINKEDIN PROFILE 
def scrape_linkedin_profile(linkedin_profile : str, mock : bool =False):
    """scrape information from linkedin profiles, Manually scrape the information from the linkedin Profile"""

    if mock: 
        linkedin_profile_url = "https://gist.githubusercontent.com/ashishvalentinealex/d38965a27126efc057a395eafc4b63b9/raw/465a1536d8f9fa4d3f910c0024dd16b8c8c150c3/gistfile1.txt"
        response = requests.get(linkedin_profile_url,timeout=10,)
        return response.json()

    else:
        pass
        

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile="Hello there",mock=True)
    )