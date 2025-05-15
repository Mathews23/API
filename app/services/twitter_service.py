"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
from os import getenv

class TwitterService:
    """
    Servicio para interactuar con la API de Twitter usando Tweepy.
    """
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {getenv("TWITTER_BEARER_TOKE")}' }
