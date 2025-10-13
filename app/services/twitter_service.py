"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
'''
This is poorly should only handle the interaction with Twitter API
The logic to store the tweets should be in another service
'''
import asyncio
from os import getenv
from datetime import datetime

import tweepy

from app.models import Post
from app.database import SessionDep

## Todo
## - Definir el esquema de datos para los tweets
## - Implementar la logica para los request de tweets
## - Manejar la paginación de resultados
## - Manejar errores y excepciones
## - Implementar tests unitarios

class TwitterService:
    """
    Service to interact with Twitter API using Tweepy.
    """

    def __init__(self, bearer_token: str):
        """
        Initialize the TwitterService with the provided Bearer Token.

        Args:
            bearer_token (str): The Bearer Token for Twitter API authentication.
        """
        try:
            self.client = tweepy.Client(bearer_token=bearer_token)
        except Exception as e:
            print(f"Error initializing Twitter client: {e}")
            self.client = None