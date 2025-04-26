"""
This module defines the data models for the application, including representations
for platforms, clients, people, profiles, types, campaigns, posts, and replies.
Models are implemented using SQLModel for data validation and ORM capabilities.
"""

from typing import Optional
from datetime import UTC, datetime
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr, HttpUrl


from uuid import UUID, uuid4

# ----------- Platform Models -----------

class PlatformBase(SQLModel):
    """
    Base model for Platform, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    url: HttpUrl = Field(default=None)

class Platform(PlatformBase, table=True):
    """
    ORM model for the Platform table.
    """
    
   

class PlatformCreate(PlatformBase):
    pass

class PlatformRead(PlatformBase):
    """
    Model for reading Platform data, includes ID.
    """
    

class PlatformUpdate(PlatformBase):
    """
    Model for updating Platform data, includes ID.
    """
   
    

class PlatformDelete(PlatformBase):
    """
    Model for deleting Platform data, includes ID.
    """
    


# ----------- Client Models -----------

class ClientBase(SQLModel):
    """
    Base model for Client, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    phone: str = Field(default=None)

class Client(ClientBase, table=True):
    """
    ORM model for the Client table.
    Include all fields to create a complete representation of the Client.
    """
    

class ClientCreate(ClientBase):
    """
    Model for creating a new Client.
    """
    pass

class ClientRead(ClientBase):
    """
    Model for reading Client data, includes ID.
    """
    

class ClientUpdate(ClientBase):
    """
    Model for updating Client data, includes ID.
    """
    

class ClientDelete(ClientBase):
    """
    Model for deleting Client data, includes ID.
    """
    


# ----------- Person Models -----------

class PersonBase(SQLModel):
    """
    Base model for Person, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    phone: str = Field(default=None)
    
class Person(PersonBase, table=True):
    """
    ORM model for the Person table.
    """
    
    
class PersonCreate(PersonBase):
    """
    Model for creating a new Person.
    """
    pass

class PersonRead(PersonBase):
    """
    Model for reading Person data, includes ID.
    """
    

class PersonUpdate(PersonBase):
    """
    Model for updating Person data, includes ID.
    """
    

class PersonDelete(PersonBase):
    """
    Model for deleting Person data, includes ID.
    """
    


# ----------- Profile Models -----------

class ProfileBase(SQLModel):
    """
    Base model for Profile, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    profile_url: HttpUrl = Field(default=None)
    
    
    
class Profile(ProfileBase, table=True):
    """
    ORM model for the Profile table.
    """
    created_at: datetime = Field(default_factory=datetime.utcnow)
    person_id: UUID = Field(foreign_key="person.id")
    person: Optional["Person"] = Relationship(back_populates="person")
    platform_id: UUID = Field(foreign_key="platform.id")
    platform: Optional["Platform"] = Relationship(back_populates="platform")

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
    
    
class ProfileUpdate(ProfileBase):
    """
    Model for updating Profile data, includes ID.
    """
   
    

class ProfileDelete(ProfileBase):
    """
    Model for deleting Profile data, includes ID.
    """
    
    

# ----------- Type Models -----------

class TypeBase(SQLModel):
    """
    Base model for Type, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    description: str = Field(default=None)
    platform_id: UUID = Field(foreign_key="platform.id")

class Type(TypeBase, table=True):
    """
    ORM model for the Type table.
    """
    created_at: datetime = Field(default_factory=datetime.now(UTC))
    platform: Optional["Platform"] = Relationship(back_populates="platform")

class TypeCreate(TypeBase):
    """
    Model for creating a new Type.
    """
    pass

class TypeRead(SQLModel):
    """
    Model for reading Type data, includes ID.
    """
    ID = UUID

class TypeUpdate(TypeBase):
    """
    Model for updating Type data, includes ID.
    """


class TypeDelete(SQLModel):
    """
    Model for deleting Type data, includes ID.
    """

# ----------- Campaign Models -----------

class CampaignBase(SQLModel):
    """
    Base model for Campaign, includes common fields.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    description: str = Field(default=None)
    start_date: datetime = Field(default=None)
    end_date: datetime = Field(default=None)
    client_id: UUID = Field(foreign_key="client.id")

class Campaign(CampaignBase, table=True):
    """
    ORM model for the Campaign table.
    """
    created_at: datetime = Field(default_factory=datetime.now(UTC))
    client: Optional["Client"] = Relationship(back_populates="type")



# ----------- Post Models -----------



# ----------- Reply Models -----------

