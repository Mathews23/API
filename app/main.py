"""
This module initializes the FastAPI application and defines the root endpoint.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}
