"""
This module initializes the FastAPI application and defines the root endpoint.
"""

from fastapi import FastAPI
from app.routes import person, platform, client

app = FastAPI()

# Include routers for different modules
app.include_router(person.router, prefix="/people", tags=["people"])
app.include_router(platform.router, prefix="/platforms", tags=["platforms"])
app.include_router(client.router, prefix="/clients", tags=["clients"])



@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


