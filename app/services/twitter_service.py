"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""

import asyncio
from os import getenv

import tweepy


class TwitterService:
    """
    Service to interact with Twitter API using Tweepy.
    """

    def __init__(self):
        self.client = tweepy.Client(bearer_token=getenv("TWITTER_BEARER_TOKEN"))

    async def get_tweets(self, query: str, max_results: int):
        """
        Retrieves recent tweets based on the provided query.
        Args:
            query (str): The search query string.
            max_results (int): The maximum number of tweets to retrieve.
        Returns:
            list: A list of tweets matching the query.
        """
        tweets = await asyncio.to_thread(
            self.client.search_recent_tweets, query=query, max_results=max_results
        )
        return tweets

    @staticmethod
    def create_query(team: list[str], start_date: str, end_date: str):
        """
        Creates a query string for searching tweets.
        """
        query = f"from:{' OR from:'.join(team)} since:{start_date} until:{end_date}"
        return query