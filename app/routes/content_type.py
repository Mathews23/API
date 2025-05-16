"""
This module handles the routing for type-related operations.
"""

from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models import Type, TypeBase
from app.database import SessionDep

router = APIRouter()


# List all registered types
@router.get("/types", response_model=list[Type])
def list_types(session: SessionDep):
    """
    List all registered types.

    Args:
        session (SessionDep): Database session.

    Returns:
        list[Type]: List of all registered types.
    """
    stmt = select(Type)
    types = session.exec(stmt).all()
    return types

# Get a specific type by ID
@router.get("/types/{type_id}", response_model=Type)
def get_type(type_id: int, session: SessionDep):
    """
    Get a specific type by ID.

    Args:
        type_id (int): ID of the type to retrieve.
        session (SessionDep): Database session.

    Returns:
        Type: The requested type.
    """
    stmt = select(Type).where(Type.id == type_id)
    type = session.exec(stmt).first()
    if not type:
        raise HTTPException(404, "Type not found")
    return type

# Create a new type
@router.post("/types", response_model=Type)
def create_type(type: TypeBase, session: SessionDep):
    """
    Create a new type.

    Args:
        type (TypeBase): The type to create.
        session (SessionDep): Database session.

    Returns:
        Type: The created type.
    """
    db_type = Type.model_validate(type)
    session.add(db_type)
    session.commit()
    session.refresh(db_type)
    return db_type

# Update an existing type
@router.put("/types/{type_id}", response_model=Type)
def update_type(type_id: int, type: TypeBase, session: SessionDep):
    """
    Update an existing type.

    Args:
        type_id (int): ID of the type to update.
        type (TypeBase): The updated type data.
        session (SessionDep): Database session.

    Returns:
        Type: The updated type.
    """
    db_type = session.get(Type, type_id)
    if not db_type:
        raise HTTPException(404, "Type not found")
    
    db_type_data = Type.model_validate(type)
    db_type.name = db_type_data.name
    session.commit()
    session.refresh(db_type)
    return db_type

# Delete a type
@router.delete("/types/{type_id}", response_model=Type)
def delete_type(type_id: int, session: SessionDep):
    """
    Delete a type.

    Args:
        type_id (int): ID of the type to delete.
        session (SessionDep): Database session.

    Returns:
        Type: The deleted type.
    """
    db_type = session.get(Type, type_id)
    if not db_type:
        raise HTTPException(404, "Type not found")
    
    session.delete(db_type)
    session.commit()
    return db_type