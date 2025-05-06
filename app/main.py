"""
This module initializes the FastAPI application and defines the root endpoint.
"""

from fastapi import FastAPI
from app.routes import person, platform, client, type
import tweepy  # type: ignore
from os import getenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the FastAPI application
app = FastAPI()

# Include routers for different modules
app.include_router(person.router, prefix="/people", tags=["people"])
app.include_router(platform.router, prefix="/platforms", tags=["platforms"])
app.include_router(client.router, prefix="/clients", tags=["clients"])
app.include_router(type.router, prefix="/types", tags=["types"])

# Create the Tweepy client on startup
@app.on_event("startup")
def create_tweepy_client():
    """
    Initialize the Tweepy client and store it in the app state.
    """
    api_key = getenv("TWITTER_API_KEY")
    api_secret = getenv("TWITTER_API_SECRET")
    access_token = getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        raise ValueError("Twitter API credentials are not set in the environment variables.")

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    app.state.tweepy_client = tweepy.API(auth)

# Access the Tweepy client in any endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


