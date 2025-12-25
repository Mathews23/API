"""
This module initializes the FastAPI application and defines the root endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import content_type, person, platform, client, campaign, analytics, twitter_fetch, teams

# Initialize the FastAPI application with lifespan
app = FastAPI(
    title="Social Media Analytics API",
    description="API for managing social media profiles, posts, and campaigns.",
    version="1.0.0"
)


# Configure CORS middleware to allow cross-origin requests

# origins = [
#     "http://localhost:3000",  # Next.js development server
#     "http://localhost",
#     "http://127.0.0.1:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# Include routers for different modules
app.include_router(person.router, prefix="/people", tags=["people"])
app.include_router(platform.router, prefix="/platforms", tags=["platforms"])
app.include_router(client.router, prefix="/clients", tags=["clients"])
app.include_router(content_type.router, prefix="/types", tags=["types"])
app.include_router(campaign.router, prefix="/campaigns", tags=["campaigns"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
app.include_router(twitter_fetch.router, prefix="/twitter", tags=["twitter"])
app.include_router(teams.router, prefix="/teams", tags=["teams"])

# Access the Tweepy client in any endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


