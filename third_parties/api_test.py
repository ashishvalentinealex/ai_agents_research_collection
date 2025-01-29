import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PROXYURL_API_KEY")
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'url': 'https://www.linkedin.com/in/ashish-valentine-732ab2147/',
    
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())
