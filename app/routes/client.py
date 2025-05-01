"""
This module contains the routes for client-related operations.
"""

from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models import Client, ClientBase
from app.database import SessionDep

router = APIRouter()

# List all registered clients
@router.get("/clients", response_model=list[Client])
def list_clients(session: SessionDep):
    """
    List all registered clients.

    Args:
        session (SessionDep): Database session.

    Returns:
        list[Client]: List of all registered clients.
    """
    stmt = select(Client)
    clients = session.exec(stmt).all()
    return clients

# Get a specific client by ID
@router.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int, session: SessionDep):
    """
    Get a specific client by ID.

    Args:
        client_id (int): ID of the client to retrieve.
        session (SessionDep): Database session.

    Returns:
        Client: The requested client.
    """
    stmt = select(Client).where(Client.id == client_id)
    client = session.exec(stmt).first()
    if not client:
        raise HTTPException(404, "Client not found")
    return client

# Create a new client
@router.post("/clients", response_model=Client)
def create_client(client: ClientBase, session: SessionDep):
    """
    Create a new client.

    Args:
        client (ClientBase): The client to create.
        session (SessionDep): Database session.

    Returns:
        Client: The created client.
    """
    db_client = Client.model_validate(client)
    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client

# Update an existing client
@router.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientBase, session: SessionDep):
    """
    Update an existing client.

    Args:
        client_id (int): ID of the client to update.
        client (ClientBase): The updated client data.
        session (SessionDep): Database session.

    Returns:
        Client: The updated client.
    """
    db_client = session.get(Client, client_id)
    if not db_client:
        raise HTTPException(404, "Client not found")
    
    db_client_data = Client.model_validate(client)
    db_client.name = db_client_data.name
    db_client.email = db_client_data.email
    session.commit()
    session.refresh(db_client)
    return db_client

# Delete a client
@router.delete("/clients/{client_id}", response_model=Client)
def delete_client(client_id: int, session: SessionDep):
    """
    Delete a client.

    Args:
        client_id (int): ID of the client to delete.
        session (SessionDep): Database session.

    Returns:
        Client: The deleted client.
    """
    db_client = session.get(Client, client_id)
    if not db_client:
        raise HTTPException(404, "Client not found")
    
    session.delete(db_client)
    session.commit()
    return db_client

