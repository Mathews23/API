"""
This module defines the data models for the application, including representations
for platforms, clients, people, profiles, types, campaigns, posts, and replies.
Models are implemented using SQLModel for data validation and ORM capabilities.
"""

from typing import Optional, List
from datetime import datetime, date
from sqlmodel import SQLModel, Field, Relationship


# ----------- Platform Models -----------
class PlatformBase(SQLModel):
    """
    Base model for a social media platform.
    """

    name: str
    description: Optional[str] = None
    url: Optional[str] = None
    active: bool = True


class Platform(PlatformBase, table=True):
    """
    Represents a row in the platform table.
    """

    id: int = Field(default=None, primary_key=True)
    profiles: List["Profile"] = Relationship(back_populates="platform")


# ----------- Person Models -----------
class PersonBase(SQLModel):
    """
    Base model for a person.
    """

    first_name: str
    last_name: str
    mobile: Optional[str] = None
    email: str
    active: bool = True
    address: Optional[str] = None


class Person(PersonBase, table=True):
    """
    Represents a row in the person table.
    """

    id: int = Field(default=None, primary_key=True)
    profiles: List["Profile"] = Relationship(back_populates="person")


class PersonCreate(PersonBase):
    """
    Model for validating data when creating a new person.
    """


# ----------- Profile Models -----------
class ProfileBase(SQLModel):
    """
    Base model for a user profile.
    """

    handle: str
    url: Optional[str] = None
    active: bool = True


class Profile(ProfileBase, table=True):
    """
    Represents a row in the profile table.
    Each profile is associated with a platform and a person.
    """

    id: int = Field(default=None, primary_key=True)
    platform_id: int = Field(foreign_key="platform.id")
    person_id: int = Field(foreign_key="person.id")
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    platform: Optional[Platform] = Relationship(back_populates="profiles")
    person: Optional[Person] = Relationship(back_populates="profiles")
    team: Optional["Team"] = Relationship(back_populates="profiles")
    posts: List["Post"] = Relationship(back_populates="profile")


# ----------- Post Models -----------
class PostBase(SQLModel):
    """
    Base model for a social media post.
    """

    content: str
    reference_id: str
    like_count: Optional[int] = 0
    reply_count: Optional[int] = 0
    bookmark_count: Optional[int] = 0
    impression_count: Optional[int] = 0
    last_updated_at: Optional[datetime] = None


class Post(PostBase, table=True):
    """
    Represents a row in the post table.
    """

    id: int = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id")
    campaign_id: Optional[int] = Field(foreign_key="campaign.id")
    type_id: Optional[int] = Field(foreign_key="type.id")
    profile: Optional[Profile] = Relationship(back_populates="posts")
    campaign: Optional["Campaign"] = Relationship(back_populates="posts")
    type: Optional["Type"] = Relationship(back_populates="posts")


# ----------- Campaign Models -----------
class CampaignBase(SQLModel):
    """
    Base model for a marketing campaign.
    """

    name: str
    start_date: date
    end_date: date


class Campaign(CampaignBase, table=True):
    """
    Represents a row in the campaign table.
    """

    id: int = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    client: Optional["Client"] = Relationship(back_populates="campaigns")
    posts: List[Post] = Relationship(back_populates="campaign")
    teams: List["Team"] = Relationship(back_populates="campaign")


# ----------- Client Models -----------
class ClientBase(SQLModel):
    """
    Base model for a client.
    """

    name: str
    email: str
    phone: Optional[str] = None


class Client(ClientBase, table=True):
    """
    Represents a row in the client table.
    """

    id: int = Field(default=None, primary_key=True)
    campaigns: List[Campaign] = Relationship(back_populates="client")


# ----------- Type Models -----------
class TypeBase(SQLModel):
    """
    Base model for a post type.
    """

    name: str
    description: Optional[str] = None


class Type(TypeBase, table=True):
    """
    Represents a row in the type table.
    """

    id: int = Field(default=None, primary_key=True)
    posts: List[Post] = Relationship(back_populates="type")


# ----------- User Models -----------

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    email: str
    is_active: bool = True
    role: str = "viewer"

class UserCreate(SQLModel):
    username: str
    password: str
    email: str
    role: Optional[str] = "viewer"  # Default is "viewer", but can be overridden

class UserRead(SQLModel):
    id: Optional[int]
    username: str
    email: str
    role: str
    is_active: bool


# ----------- Team Models -----------
class TeamBase(SQLModel):
    """
    Base model for a team of people.
    """
    name: str
    description: Optional[str] = None
    active: bool = True


class Team(TeamBase, table=True):
    """
    Represents a row in the team table.
    Each team is associated with a campaign and has multiple profiles.
    """
    id: int = Field(default=None, primary_key=True)
    campaign_id: Optional[int] = Field(default=None, foreign_key="campaign.id")
    campaign: Optional[Campaign] = Relationship(back_populates="teams")
    profiles: List["Profile"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    """
    Model for validating data when creating a new team.
    """
    campaign_id: Optional[int] = None


class TeamRead(TeamBase):
    """
    Model for reading team data.
    """
    id: int
    campaign_id: Optional[int] = None


class TeamUpdate(SQLModel):
    """
    Model for updating team data.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None
    campaign_id: Optional[int] = None



