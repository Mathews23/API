"""
This module initializes the FastAPI application and defines the root endpoint.
"""
import uvicorn
from fastapi import FastAPI
from routes import platform

app = FastAPI()


app.include_router(platform.router)



@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    """
    Main entry point for the application. Runs the FastAPI app using Uvicorn.
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)