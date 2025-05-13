import requests
from dotenv import load_dotenv
from os import getenv


load_dotenv()

bearer_token = getenv("TWITTER_BEARER_TOKEN")
url = "https://api.twitter.com/2/tweets/search/recent"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}
# Obtener equipos
    # Obtener campaña asociada con el equipo 
    #  Por ejemplo, la campaña de nombre "Campaña de prueba"
    #  Busco la campaña por nombre
    # Obtener el id de esa campaña, obtener los equipos asociados
    # Obtener el id de la obtener el encargado de la campaña
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
