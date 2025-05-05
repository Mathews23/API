"""
Connect to the database and create the tables if they don't exist.
"""
from os import getenv
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from fastapi import Depends
from typing import Annotated

load_dotenv()
password = getenv("DB_PASSWORD")
mysql_user = getenv("DB_USER", "root")
if not password or not mysql_user:
    raise ValueError("DB creds not set")

mysql_url = f"mysql+pymysql://{mysql_user}:{password}@localhost:3306/test"
engine = create_engine(mysql_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]