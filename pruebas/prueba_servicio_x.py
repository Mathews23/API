import requests
import json
from dotenv import load_dotenv
from os import getenv


load_dotenv()

bearertoken = getenv("BEARER_TOKEN")
url = "https://api.twitter.com/2/tweets/search/recent"

headers = {
    "Authorization": f"Bearer {bearertoken}"
}
