"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""

import asyncio
from os import getenv
from datetime import datetime

import tweepy
from sqlmodel import Session

from app.models import Post
from app.database import engine


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

    async def fetch_and_store_tweets(
        self,
        query: str,
        max_results: int,
        profile_id: int,
        campaign_id: int,
        type_id: int,
    ):
        """
        Fetch tweets from Twitter API and insert them into the post table.
        """
        tweets_response = await self.get_tweets(query, max_results)
        tweets = getattr(tweets_response, "data", [])

        if not tweets:
            return 0  # No tweets to insert

        with Session(engine) as session:
            for tweet in tweets:
                metrics = tweet.public_metrics if hasattr(tweet, "public_metrics") else {}
                post = Post(
                    content=getattr(tweet, "text", ""),
                    reference_id=str(tweet.id),
                    profile_id=profile_id,
                    campaign_id=campaign_id,
                    type_id=type_id,
                    like_count=metrics.get("like_count", 0),
                    reply_count=metrics.get("reply_count", 0),
                    bookmark_count=metrics.get("bookmark_count", 0),
                    impression_count=metrics.get("impression_count", 0),
                    last_updated_at=getattr(tweet, "created_at", datetime.utcnow()),
                )
                session.add(post)
            session.commit()
        return len(tweets)