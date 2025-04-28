"""
Endpoints for platform-related operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from models import Platform, PlatformCreate
from database import SessionDep

router = APIRouter()


# Crear Platform
@router.post("/platforms", response_model=Platform)
async def create_platform(platform: PlatformCreate, session: SessionDep):
    """
    Create a new platform.

    Args:
        platform (dict): The platform data to be created.

    Returns:
        dict: The created platform data.
    """
    # Implement the logic to create a new platform
    session.add(platform)
    session.commit()
    session.refresh(platform)
    
    return platform

# Leer todas las Plataforms registradas

# Leer Plataform especifica

# Actualizar Plataform

# Eliminar Plataform

# Cambiar registro de Plataform