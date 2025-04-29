from fastapi import APIRouter, HTTPException
from app.models import Person, PersonCreate
from app.database import SessionDep

router = APIRouter()

@router.post("/people", response_model=Person)
async def create_person(person: PersonCreate, session: SessionDep):
    """
    Create a new person.

    Args:
        person (dict): The person data to be created.

    Returns:
        dict: The created person data.
    """
    # Implement the logic to create a new person
    # Check if the person already exists
    # Add the person to the session
    session.add(person)
    session.commit()
    session.refresh(person)
    
    return person