"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
from sqlmodel import select
from datetime import datetime
from app.models import Post, Profile
from typing import Optional
from app.database import SessionDep

class TwitterService:

    def __init__(self, session: SessionDep):
        self.session = session

    def get_profile_id_by_username(self, username: str) -> Optional[int]:
        statement = select(Profile).where(Profile.handle == username)
        profile = self.session.exec(statement).first()
        return profile.id if profile else None

    def upsert_tweets(self, tweets_response):
        for tweet in tweets_response.data:
            metrics = tweet.public_metrics

            # 👇 Extract author's username (from "includes" field)
            username = None
            for user in tweets_response.includes['users']:
                if user.id == tweet.author_id:
                    username = user.username
                    break

            # Match profile_id
            profile_id = self.get_profile_id_by_username(username) if username else None

            # Check if post exists
            statement = select(Post).where(Post.id == tweet.id)
            existing_post = self.session.exec(statement).first()

            if existing_post:
                # Update
                existing_post.like_count = metrics.get('like_count', 0)
                existing_post.reply_count = metrics.get('reply_count', 0)
                existing_post.bookmark_count = metrics.get('bookmark_count', 0)
                existing_post.impression_count = metrics.get('impression_count', 0)
                existing_post.last_updated_at = datetime.utcnow()
                existing_post.profile_id = profile_id  # update link
            else:
                # Insert
                new_post = Post(
                    id=tweet.id,
                    profile_id=profile_id,
                    campaign_id=None,
                    type_id=None,
                    reference_id=None,

                    like_count=metrics.get('like_count', 0),
                    reply_count=metrics.get('reply_count', 0),
                    bookmark_count=metrics.get('bookmark_count', 0),
                    impression_count=metrics.get('impression_count', 0),

                    last_updated_at=datetime.utcnow()
                )
                self.session.add(new_post)

        self.session.commit()
        return {"message": f"Upserted {len(tweets_response.data)} tweets."}
