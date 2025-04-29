from fastapi import APIRouter, HTTPException
from app.models import Person, PersonCreate
from app.database import SessionDep

router = APIRouter()

@router.post("/people", response_model=Person)
async def create_person(person: PersonCreate, session: SessionDep):
    # Implement the logic to create a new person
    # Check if the person already exists
        # Check if the persons name is already in the database
        #
    # If the person already exists, raise an HTTPException
    # If the person does not exist, create a new person

    # Add the person to the session
    session.add(person)
    # Commit the session to save the changes
    session.commit()
    # Refresh the session to get the latest data
    session.refresh(person)
    
    return person