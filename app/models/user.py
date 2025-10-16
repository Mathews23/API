
from sqlmodel import SQLModel, Field
from typing import Optional


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
