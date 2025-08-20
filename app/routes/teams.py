"""
This module contains the routes for team-related operations.
"""

from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models import Team, TeamBase, TeamCreate, TeamRead, TeamUpdate, Profile
from app.database import SessionDep

router = APIRouter()


# List all registered teams
@router.get("/", response_model=list[TeamRead])
def list_teams(session: SessionDep):
    """
    List all registered teams.

    Args:
        session (SessionDep): Database session.

    Returns:
        list[TeamRead]: List of all registered teams.
    """
    stmt = select(Team)
    teams = session.exec(stmt).all()
    return teams


# Get a specific team by ID
@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: int, session: SessionDep):
    """
    Get a specific team by ID.

    Args:
        team_id (int): ID of the team to retrieve.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The requested team.
    """
    stmt = select(Team).where(Team.id == team_id)
    team = session.exec(stmt).first()
    if not team:
        raise HTTPException(404, "Team not found")
    return team


# Create a new team
@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, session: SessionDep):
    """
    Create a new team.

    Args:
        team (TeamCreate): The team to create.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The created team.
    """
    db_team = Team.model_validate(team)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


# Update an existing team
@router.put("/{team_id}", response_model=TeamRead)
def update_team(team_id: int, team: TeamUpdate, session: SessionDep):
    """
    Update an existing team.

    Args:
        team_id (int): ID of the team to update.
        team (TeamUpdate): The updated team data.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The updated team.
    """
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(404, "Team not found")
    
    team_data = team.model_dump(exclude_unset=True)
    for key, value in team_data.items():
        setattr(db_team, key, value)
    
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


# Delete a team
@router.delete("/{team_id}", response_model=TeamRead)
def delete_team(team_id: int, session: SessionDep):
    """
    Delete a team.

    Args:
        team_id (int): ID of the team to delete.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The deleted team.
    """
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(404, "Team not found")
    
    session.delete(db_team)
    session.commit()
    return db_team


# Add a profile to a team
@router.post("/{team_id}/profiles/{profile_id}", response_model=TeamRead)
def add_profile_to_team(team_id: int, profile_id: int, session: SessionDep):
    """
    Add a profile to a team.

    Args:
        team_id (int): ID of the team.
        profile_id (int): ID of the profile to add.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The updated team.
    """
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(404, "Team not found")
    
    profile = session.get(Profile, profile_id)
    if not profile:
        raise HTTPException(404, "Profile not found")
    
    profile.team_id = team_id
    session.add(profile)
    session.commit()
    session.refresh(team)
    return team


# Remove a profile from a team
@router.delete("/{team_id}/profiles/{profile_id}", response_model=TeamRead)
def remove_profile_from_team(team_id: int, profile_id: int, session: SessionDep):
    """
    Remove a profile from a team.

    Args:
        team_id (int): ID of the team.
        profile_id (int): ID of the profile to remove.
        session (SessionDep): Database session.

    Returns:
        TeamRead: The updated team.
    """
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(404, "Team not found")
    
    profile = session.get(Profile, profile_id)
    if not profile:
        raise HTTPException(404, "Profile not found")
    
    if profile.team_id != team_id:
        raise HTTPException(400, "Profile is not in this team")
    
    profile.team_id = None
    session.add(profile)
    session.commit()
    session.refresh(team)
    return team