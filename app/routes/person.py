from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models import Person, PersonCreate
from app.database import get_session

router = APIRouter()

# Listar todas las personas
@router.get("/people", response_model=list[Person])
def list_people(session: Session = Depends(get_session)):
    """
    List all registered people.

    Args:
        session (Session): Database session.

    Returns:
        list[Person]: List of all registered people.
    """
    stmt = select(Person)
    return session.exec(stmt).all()

# Buscar persona por ID
@router.get("/people/{person_id}", response_model=Person)
def get_person(person_id: int, session: Session = Depends(get_session)):
    """
    Get a specific person by ID.

    Args:
        person_id (int): ID of the person to retrieve.
        session (Session): Database session.

    Returns:
        Person: The requested person.
    """
    stmt = select(Person).where(Person.id == person_id)
    person = session.exec(stmt).first()
    if not person:
        raise HTTPException(404, "Persona no encontrada")
    return person

# Crear una persona
@router.post("/people", response_model=Person)
def create_person(person: PersonCreate, session: Session = Depends(get_session)):
    """
    Create a new person.

    Args:
        person (PersonCreate): The person to create.
        session (Session): Database session.

    Returns:
        Person: The created person.
    """
    db_person = Person.model_validate(person)
    session.add(db_person)
    session.commit()
    session.refresh(db_person)
    return db_person

# Actualizar persona
@router.put("/people/{person_id}", response_model=Person)
def update_person(person_id: int, person: PersonCreate, session: Session = Depends(get_session)):
    """
    Update an existing person.

    Args:
        person_id (int): ID of the person to update.
        person (PersonCreate): The updated person data.
        session (Session): Database session.

    Returns:
        Person: The updated person.
    """
    db_person = session.get(Person, person_id)
    if not db_person:
        raise HTTPException(404, "Persona no encontrada")
    db_person_data = person.model_dump(exclude_unset=True)
    for key, value in db_person_data.items():
        setattr(db_person, key, value)
    session.add(db_person)
    session.commit()
    session.refresh(db_person)
    return db_person

# Eliminar persona
@router.delete("/people/{person_id}", response_model=Person)
def delete_person(person_id: int, session: Session = Depends(get_session)):
    """
    Delete a person by ID.

    Args:
        person_id (int): ID of the person to delete.
        session (Session): Database session.

    Returns:
        Person: The deleted person.
    """
    db_person = session.get(Person, person_id)
    if not db_person:
        raise HTTPException(404, "Persona no encontrada")
    session.delete(db_person)
    session.commit()
    return db_person