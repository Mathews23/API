"""
This module defines the data models for the application, including representations
for platforms, clients, people, profiles, types, campaigns, posts, and replies.
Models are implemented using SQLModel for data validation and ORM capabilities.
"""

from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime, date
from sqlmodel import SQLModel, Field, Relationship


# ----------- Platform Models -----------
class PlatformBase(SQLModel):
    name: str
    description: Optional[str] = None
    url: Optional[str] = None
    active: bool = True


class Platform(PlatformBase, table=True):
    id: int = Field(default=None, primary_key=True)
    profiles: List["Profile"] = Relationship(back_populates="platform")


# ----------- Person Models -----------
class PersonBase(SQLModel):
    first_name: str
    last_name: str
    mobile: Optional[str] = None
    email: str
    active: bool = True
    address: Optional[str] = None


class Person(PersonBase, table=True):
    id: int = Field(default=None, primary_key=True)
    profiles: List["Profile"] = Relationship(back_populates="person")

class PersonCreate(PersonBase):
    pass


# ----------- Profile Models -----------
class ProfileBase(SQLModel):
    handle: str
    url: Optional[str] = None
    active: bool = True


class Profile(ProfileBase, table=True):
    id: int = Field(default=None, primary_key=True)
    platform_id: int = Field(foreign_key="platform.id")
    person_id: int = Field(foreign_key="person.id")
    platform: Optional[Platform] = Relationship(back_populates="profiles")
    person: Optional[Person] = Relationship(back_populates="profiles")
    posts: List["Post"] = Relationship(back_populates="profile")


# ----------- Post Models -----------
class PostBase(SQLModel):
    reference_id: str
    like_count: Optional[int] = 0
    reply_count: Optional[int] = 0
    bookmark_count: Optional[int] = 0
    impression_count: Optional[int] = 0
    last_updated_at: Optional[datetime] = None


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id")
    campaign_id: Optional[int] = Field(foreign_key="campaign.id")
    type_id: Optional[int] = Field(foreign_key="type.id")
    profile: Optional[Profile] = Relationship(back_populates="posts")
    campaign: Optional["Campaign"] = Relationship(back_populates="posts")
    type: Optional["Type"] = Relationship(back_populates="posts")


# ----------- Campaign Models -----------
class CampaignBase(SQLModel):
    name: str
    start_date: date
    end_date: date


class Campaign(CampaignBase, table=True):
    id: int = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    client: Optional["Client"] = Relationship(back_populates="campaigns")
    posts: List[Post] = Relationship(back_populates="campaign")


# ----------- Client Models -----------
class ClientBase(SQLModel):
    name: str
    email: str
    phone: Optional[str] = None


class Client(ClientBase, table=True):
    id: int = Field(default=None, primary_key=True)
    campaigns: List[Campaign] = Relationship(back_populates="client")


# ----------- Type Models -----------
class TypeBase(SQLModel):
    name: str
    description: Optional[str] = None


class Type(TypeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    posts: List[Post] = Relationship(back_populates="type")