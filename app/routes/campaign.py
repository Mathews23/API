"""
This module defines the routes for managing campaigns in the application.
"""


from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models import Campaign, CampaignBase
from app.database import SessionDep


router = APIRouter()


# List all registered campaigns
@router.get("/campaigns", response_model=list[Campaign])
def list_campaigns(session: SessionDep):
    """
    List all registered campaigns.

    Args:
        session (SessionDep): Database session.

    Returns:
        list[Campaign]: List of all registered campaigns.
    """
    stmt = select(Campaign)
    campaigns = session.exec(stmt).all()
    return campaigns

# Get a specific campaign by ID
@router.get("/campaigns/{campaign_id}", response_model=Campaign)
def get_campaign(campaign_id: int, session: SessionDep):
    """
    Get a specific campaign by ID.

    Args:
        campaign_id (int): ID of the campaign to retrieve.
        session (SessionDep): Database session.

    Returns:
        Campaign: The requested campaign.
    """
    stmt = select(Campaign).where(Campaign.id == campaign_id)
    campaign = session.exec(stmt).first()
    if not campaign:
        raise HTTPException(404, "Campaign not found")
    return campaign

# Create a new campaign
@router.post("/campaigns", response_model=Campaign)
def create_campaign(campaign: CampaignBase, session: SessionDep):
    """
    Create a new campaign.

    Args:
        campaign (CampaignBase): The campaign to create.
        session (SessionDep): Database session.

    Returns:
        Campaign: The created campaign.
    """
    db_campaign = Campaign.model_validate(campaign)
    session.add(db_campaign)
    session.commit()
    session.refresh(db_campaign)
    return db_campaign


# Update an existing campaign
@router.put("/campaigns/{campaign_id}", response_model=Campaign)
def update_campaign(campaign_id: int, campaign: CampaignBase, session: SessionDep):
    """
    Update an existing campaign.

    Args:
        campaign_id (int): ID of the campaign to update.
        campaign (CampaignBase): The updated campaign data.
        session (SessionDep): Database session.

    Returns:
        Campaign: The updated campaign.
    """
    db_campaign = session.get(Campaign, campaign_id)
    if not db_campaign:
        raise HTTPException(404, "Campaign not found")
    
    db_campaign_data = Campaign.model_validate(campaign)
    for key, value in db_campaign_data.dict(exclude_unset=True).items():
        setattr(db_campaign, key, value)
    
    session.commit()
    session.refresh(db_campaign)
    return db_campaign

# Delete a campaign
@router.delete("/campaigns/{campaign_id}", response_model=Campaign)
def delete_campaign(campaign_id: int, session: SessionDep):
    """
    Delete a campaign.

    Args:
        campaign_id (int): ID of the campaign to delete.
        session (SessionDep): Database session.

    Returns:
        Campaign: The deleted campaign.
    """
    db_campaign = session.get(Campaign, campaign_id)
    if not db_campaign:
        raise HTTPException(404, "Campaign not found")
    
    session.delete(db_campaign)
    session.commit()
    return db_campaign