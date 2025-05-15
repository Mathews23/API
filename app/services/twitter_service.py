"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
from sqlmodel import select
from datetime import datetime
from app.models import Post, Profile
from typing import Optional
from app.database import SessionDep
from os import getenv
from dotenv import load_dotenv

class TwitterService:
    
    def __init__(self, headers: dict):
        self.headers = {
            'Authorization': f'Bearer {getenv("TWITTER_BEARER_TOKE")}' }
