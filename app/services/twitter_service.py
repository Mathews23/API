"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""

import asyncio
from os import getenv

import tweepy


class TwitterService:
    """
    Servicio para interactuar con la API de Twitter usando Tweepy.
    """

    def __init__(self):
        self.client = tweepy.Client(bearer_token=getenv("TWITTER_BEARER_TOKEN"))

    async def get_tweets(self, query: str, max_results: int):
        """
        Obtiene tweets de forma asíncrona según la consulta y obtiene la cantidad solicitada.
        """
        tweets = await asyncio.to_thread(
            self.client.search_recent_tweets, query=query, max_results=max_results
        )
        return tweets

    @staticmethod
    def create_query(team: list[str], start_date: str, end_date: str):
        """
        Crea una consulta para buscar tweets de un equipo específico entre dos fechas.
        """
        query = f"from:{team} since:{start_date} until:{end_date}"
        return query
