"""
Endpoints for platform-related operations.
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionDep
from app.models import Platform, PlatformBase

router = APIRouter()


# Crear Platform
@router.post("/platforms", response_model=Platform)
def create_platform(platform: PlatformBase, session: SessionDep):
    """
    Create a new platform.

    Args:
        platform (PlatformBase): The platform to create.
        session (SessionDep): Database session.

    Returns:
        Platform: The created platform.
    """
    db_platform = Platform.model_validate(platform)
    session.add(db_platform)
    session.commit()
    session.refresh(db_platform)
    return db_platform

# Leer todas las Platforms registradas
@router.get("/platforms", response_model=List[Platform])
def read_platforms(session: SessionDep):
    """
    Retrieve all registered platforms.

    Args:
        session (SessionDep): Database session.

    Returns:
        List[Platform]: A list of registered platforms.
    """
    platforms = session.query(Platform).all()
    return platforms

# Leer Platform especifica
@router.get("/platforms/{platform_id}", response_model=Platform)
def read_platform(platform_id: int, session: SessionDep):
    """
    Retrieve a specific platform by ID.

    Args:
        platform_id (int): ID of the platform to retrieve.
        session (SessionDep): Database session.

    Returns:
        Platform: The requested platform.
    """
    platform = session.get(Platform, platform_id)
    if not platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    return platform

# Actualizar Platform
@router.put("/platforms/{platform_id}", response_model=Platform)
def update_platform(platform_id: int, platform: PlatformBase, session: SessionDep):
    """
    Update an existing platform.

    Args:
        platform_id (int): ID of the platform to update.
        platform (PlatformBase): The updated platform data.
        session (SessionDep): Database session.

    Returns:
        Platform: The updated platform.
    """
    db_platform = session.get(Platform, platform_id)
    if not db_platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    
    for key, value in platform.model_dump().items():
        setattr(db_platform, key, value)
    
    session.commit()
    session.refresh(db_platform)
    return db_platform

# Eliminar Platform
@router.delete("/platforms/{platform_id}", response_model=Platform)
def delete_platform(platform_id: int, session: SessionDep):
    """
    Delete a platform by ID.

    Args:
        platform_id (int): ID of the platform to delete.
        session (SessionDep): Database session.

    Returns:
        Platform: The deleted platform.
    """
    db_platform = session.get(Platform, platform_id)
    if not db_platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    
    session.delete(db_platform)
    session.commit()
    return db_platform


# Cambiar registro de Platform
