"""Service for handling authentication-related operations."""


from app.models import User, UserCreate
from app.database import SessionDep
from sqlmodel import select
from fastapi import HTTPException
from passlib.hash import bcrypt

class AuthService:
    """Service class for authentication-related operations."""

    @staticmethod
    def register_user(new_user: UserCreate, session: SessionDep) -> User:
        """Register a new user.
        """
        # Check if user already exists
        email = new_user.email
        stmt = select(User).where(User.email == email)
        user = session.exec(stmt).first()
        if user:
            raise HTTPException(status_code=409, detail="User already exists with this email.")
        # Hash the password
        hashed_password = bcrypt.hash(new_user.password)
        # Use provided role or default to "viewer"
        user = User(
            username=new_user.username,
            hashed_password=hashed_password,
            email=email,
            is_active=True,
            role=new_user.role or "viewer"
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
           

    @staticmethod
    def authenticate_user(username: str, password: str, session: SessionDep) -> User | None:
        """Authenticate an existing user."""
        stmt = select(User).where(User.username == username)
        user = session.exec(stmt).first()
        if not user:
            return None
        if not bcrypt.verify(password, user.hash_password):
            return None
        return user