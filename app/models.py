"""
This module defines the data models for the application, including representations
for platforms, clients, people, profiles, types, campaigns, posts, and replies.
Models are implemented using SQLModel for data validation and ORM capabilities.
"""

from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from pydantic import EmailStr, constr, HttpUrl


from uuid import UUID, uuid4

# ----------- Platform Models -----------

class PlatformBase(SQLModel):
    """
    Base model for Platform, includes common fields.
    """
    name: str
    url: HttpUrl

class Platform(PlatformBase, table=True):
    """
    ORM model for the Platform table.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
   

class PlatformCreate(PlatformBase):
    pass

class PlatformRead(PlatformBase):
    """
    Model for reading Platform data, includes ID.
    """
    id: UUID

class PlatformUpdate(PlatformBase):
    """
    Model for updating Platform data, includes ID.
    """
    id: UUID
    

class PlatformDelete(PlatformBase):
    """
    Model for deleting Platform data, includes ID.
    """
    id: UUID

class ClientBase(SQLModel):
    """
    Base model for Client, includes common fields.
    """
    name: str
    email: EmailStr
    phone: str

class Client(ClientBase, table=True):
    """
    ORM model for the Client table.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)

class ClientCreate(ClientBase):
    """
    Model for creating a new Client.
    """
    pass

class ClientRead(ClientBase):
    """
    Model for reading Client data, includes ID.
    """
    id: UUID

class ClientUpdate(ClientBase):
    """
    Model for updating Client data, includes ID.
    """
    id: UUID

class ClientDelete(ClientBase):
    """
    Model for deleting Client data, includes ID.
    """
    id: UUID


# ----------- Person Models -----------

class PersonBase(SQLModel):
    """
    Base model for Person, includes common fields.
    """
    name: str

class PersonCreate(PersonBase):
    """
    Model for creating a new Person.
    """
    ...

class PersonRead(PersonBase):
    """
    Model for reading Person data, includes ID.
    """
    id: int

class Person(SQLModel, table=True):
    """
    ORM model for the Person table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

# ----------- Profile Models -----------

class ProfileBase(SQLModel):
    """
    Base model for Profile, includes common fields.
    """
    person_id: int

class ProfileCreate(ProfileBase):
    """
    Model for creating a new Profile.
    """
    ...

class ProfileRead(ProfileBase):
    """
    Model for reading Profile data, includes ID.
    """
    id: int

class Profile(SQLModel, table=True):
    """
    ORM model for the Profile table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")

# ----------- Type Models -----------

class TypeBase(SQLModel):
    """
    Base model for Type, includes common fields.
    """
    name: str

class TypeCreate(TypeBase):
    """
    Model for creating a new Type.
    """
    ...

class TypeRead(TypeBase):
    """
    Model for reading Type data, includes ID.
    """
    id: int

class Type(SQLModel, table=True):
    """
    ORM model for the Type table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

# ----------- Campaign Models -----------

class CampaignBase(SQLModel):
    """
    Base model for Campaign, includes common fields.
    """
    name: str
    client_id: int

class CampaignCreate(CampaignBase):
    """
    Model for creating a new Campaign.
    """
    ...

class CampaignRead(CampaignBase):
    """
    Model for reading Campaign data, includes ID.
    """
    id: int

class Campaign(SQLModel, table=True):
    """
    ORM model for the Campaign table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    client_id: int = Field(foreign_key="client.id")

# ----------- Post Models -----------

class PostBase(SQLModel):
    """
    Base model for Post, includes common fields.
    """
    platform_id: int
    type_id: int
    profile_id: int
    campaign_id: int
    likes_count: Optional[int] = 0
    reply_count: Optional[int] = 0
    created_at: Optional[datetime] = None

class PostCreate(PostBase):
    """
    Model for creating a new Post.
    """
    ...

class PostRead(PostBase):
    """
    Model for reading Post data, includes ID.
    """
    id: int

class Post(SQLModel, table=True):
    """
    ORM model for the Post table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    platform_id: int = Field(foreign_key="platform.id")
    type_id: int = Field(foreign_key="type.id")
    profile_id: int = Field(foreign_key="profile.id")
    campaign_id: int = Field(foreign_key="campaign.id")
    likes_count: Optional[int] = 0
    reply_count: Optional[int] = 0
    created_at: Optional[datetime] = None

# ----------- Reply Models -----------

class ReplyBase(SQLModel):
    """
    Base model for Reply, includes common fields.
    """
    post_id: int
    content: Optional[dict] = None

class ReplyCreate(ReplyBase):
    """
    Model for creating a new Reply.
    """
    ...

class ReplyRead(ReplyBase):
    """
    Model for reading Reply data, includes ID.
    """
    id: int

class Reply(SQLModel, table=True):
    """
    ORM model for the Reply table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    content: Optional[dict] = None
