import os 
import requests
from dotenv import load_dotenv 
import pprint

load_dotenv()

# FUNCTION TO SCRAPE LINKEDIN PROFILE 
def scrape_linkedin_profile(linkedin_profile: str, mock: bool = False):
    """Scrape information from LinkedIn profiles manually or using an API"""

    if mock: 
        linkedin_profile_url = "https://gist.githubusercontent.com/ashishvalentinealex/d38965a27126efc057a395eafc4b63b9/raw/465a1536d8f9fa4d3f910c0024dd16b8c8c150c3/gistfile1.txt"
        print(f"[DEBUG] Mock URL: {linkedin_profile_url}")  # Debugging statement
        response = requests.get(linkedin_profile_url, timeout=10)
        return response.json()

    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile,  # This should be linkedin_profile, not linkedin_profile_url
        }
        print(f"[DEBUG] API Endpoint: {api_endpoint}")  # Debugging statement
        print(f"[DEBUG] Params: {params}")  # Debugging statement
        
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    print(f"[DEBUG] Response Status Code: {response.status_code}")  # Debugging statement
    print(f"[DEBUG] Response Content: {response.text[:500]}")  # Debugging statement (limit for readability)

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data["groups"]:
            group_dict.pop("profile_pic_url")

    return data

# if __name__ == "__main__":
#     data = scrape_linkedin_profile(linkedin_profile="Hello there", mock=True)
    
#     # Using pprint to pretty-print the output
#     pprint.pprint(data)
