"""
This module initializes the FastAPI application and defines the root endpoint.
"""
import uvicorn
from fastapi import FastAPI
from routes import platform, person

app = FastAPI()


app.include_router(person.router, prefix="/people", tags=["people"])





@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


