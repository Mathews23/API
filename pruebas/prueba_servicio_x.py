import requests
import json
from dotenv import load_dotenv
from os import getenv


load_dotenv()

bearer_token = getenv("TWITTER_BEARER_TOKEN")
url = "https://api.twitter.com/2/tweets/search/recent"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}
# Obtener equipos
# Armar query
    # Filtrar por equipos
    # Filtrar por fecha
query_string = {
    "query": "from:elonmusk",
    "tweet.fields": "public_metrics",
    
}
response = requests.get(url, headers=headers, params=query_string)

data = response.json()
print(data)
