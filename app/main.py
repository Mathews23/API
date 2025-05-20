"""
This module initializes the FastAPI application and defines the root endpoint.
"""

from fastapi import FastAPI
from app.routes import content_type, person, platform, client, campaign, analytics

# Initialize the FastAPI application with lifespan
app = FastAPI()

# Include routers for different modules
app.include_router(person.router, prefix="/people", tags=["people"])
app.include_router(platform.router, prefix="/platforms", tags=["platforms"])
app.include_router(client.router, prefix="/clients", tags=["clients"])
app.include_router(content_type.router, prefix="/types", tags=["types"])
app.include_router(campaign.router, prefix="/campaigns", tags=["campaigns"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

# Access the Tweepy client in any endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


