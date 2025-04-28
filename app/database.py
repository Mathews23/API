"""
Connect to the database and create the tables if they don't exist.
"""
from os import getenv
from typing import Annotated
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends, FastAPI

# Load environment variables from .env file
load_dotenv()

# Get the database password and user from environment variables
password = getenv("DB_PASSWORD")
mysql_user = getenv("DB_USER", "root")

# Check if the password is set
if not password or not mysql_user:
    raise ValueError("Credentials environment variable not set")


# Create the database URL
mysql_url = f"mysql+pymysql://{mysql_user}:{password}@localhost:3306/test"

# Create the database engine
engine = create_engine(mysql_url, echo=True)

def create_db_and_tables(app: FastAPI):
    """
    Create the database and tables if they don't exist.
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Get a session to interact with the database.
    
    Returns:
        Session: A SQLModel session object.
    """
    with Session(engine) as session:
        yield session

# Define a type alias for the session dependency
SessionDep = Annotated[Session, Depends(get_session)]