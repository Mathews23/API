"""
Prueba de servicio de Twitter"""

from os import getenv

import requests
from dotenv import load_dotenv

load_dotenv()

bearer_token = getenv("TWITTER_BEARER_TOKEN")
URL = "https://api.twitter.com/2/tweets/search/recent"

headers = {"Authorization": f"Bearer {bearer_token}"}
# Obtener equipos
# Obtener campaña asociada con el equipo
#  Por ejemplo, la campaña de nombre "Campaña de prueba"
#  Busco la campaña por nombre
# Obtener el id de esa campaña, obtener los equipos asociados
# Obtener el id de la obtener el encargado de la campaña
# In: id de la campaña
# Out: dict con tres llaves:
# 'nombre de equipo': int,
# 'id de equipo': int,
# 'integrantes del equipo': list[str]
# Escribir store procedure que busque los integrantes de un grupo
# Armar query
# Filtrar por equipos
# Filtrar por fecha
query_string = {
    "query": "from:elonmusk",
    "tweet.fields": "public_metrics",
}
response = requests.get(URL, headers=headers, params=query_string, timeout=10)

# data = response.json()
print(response.text)
