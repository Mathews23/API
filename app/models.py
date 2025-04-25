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


# ----------- Client Models -----------

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
    email: EmailStr
    phone: str
    
class Persosn(PersonBase, table=True):
    """
    ORM model for the Person table.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    
class PersonCreate(PersonBase):
    """
    Model for creating a new Person.
    """
    pass

class PersonRead(PersonBase):
    """
    Model for reading Person data, includes ID.
    """
    id: UUID

class PersonUpdate(PersonBase):
    """
    Model for updating Person data, includes ID.
    """
    id: UUID

class PersonDelete(PersonBase):
    """
    Model for deleting Person data, includes ID.
    """
    id: UUID


# ----------- Profile Models -----------

class ProfileBase(SQLModel):
    """
    Base model for Profile, includes common fields.
    """
    name: str
    url: HttpUrl
    person_id: Optional[UUID]
    platform_id: Optional[UUID]
    
    
class Profile(ProfileBase, table=True):
    """
    ORM model for the Profile table.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ProfileCreate(ProfileBase):
    """
    Model for creating a new Profile.
    """
    person_id: UUID
    platform_id: UUID

class ProfileRead(ProfileBase):
    """
    Model for reading Profile data, includes ID.
    """
    id: UUID
    
class ProfileUpdate(ProfileBase):
    """
    Model for updating Profile data, includes ID.
    """
    id: UUID
    

class ProfileDelete(ProfileBase):
    """
    Model for deleting Profile data, includes ID.
    """
    id: UUID
    

# ----------- Type Models -----------



# ----------- Campaign Models -----------



# ----------- Post Models -----------



# ----------- Reply Models -----------

