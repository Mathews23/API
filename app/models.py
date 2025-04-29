"""
This module defines the data models for the application, including representations
for platforms, clients, people, profiles, types, campaigns, posts, and replies.
Models are implemented using SQLModel for data validation and ORM capabilities.
"""

from typing import Optional
from datetime import UTC, datetime
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr


from uuid import UUID, uuid4

# ----------- Person Models -----------

class Person(SQLModel):
    """
    Represents a person with a unique identifier, name, and email.
    """
    id: int = Field(default_factory=uuid4, primary_key=True)
    first_name: str = Field(default="")
    last_name: str = Field(default="")
    mobile: str = Field(default="")
    email: str = Field(default="")
    active: bool = Field(default=True)
    address: str = Field(default="")

class PersonCreate(SQLModel):
    first_name: str
    last_name: str
    mobile: str
    email: str
    active: bool = True
    address: str