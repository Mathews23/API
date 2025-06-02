from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from datetime import datetime
from app.models import Campaign, Team, Profile, Post
from app.database import get_session
from app.services.twitter_service import TwitterService

router = APIRouter()

@router.post("/fetch-campaign-tweets/")
async def fetch_campaign_tweets(
    campaign_id: int,
    keyword: str = "",
    max_results: int = 10,
    type_id: int = 1,
    session: Session = Depends(get_session)
):
    # 1. Verificar si la campaña está vigente
    campaign = session.exec(select(Campaign).where(Campaign.id == campaign_id)).first()
    now = datetime.utcnow().date()
    if not campaign or not (campaign.start_date <= now <= campaign.end_date):
        raise HTTPException(status_code=400, detail="Campaña no vigente")

    # 2. Extraer los equipos y sus perfiles asociados
    teams = session.exec(select(Team).where(Team.campaign_id == campaign_id)).all()
    handles = []
    profile_ids = []
    for team in teams:
        # Asumiendo que existe una relación de team a profile (ajusta si tu modelo es diferente)
        profiles = session.exec(select(Profile).where(Profile.team_id == team.id)).all()
        for profile in profiles:
            handles.append(profile.handle)
            profile_ids.append(profile.id)

    if not handles:
        raise HTTPException(status_code=404, detail="No hay perfiles asociados a equipos para esta campaña")

    # 3. Armar el query con palabra clave o hashtag
    query = TwitterService.create_query(handles)
    if keyword:
        query += f" {keyword}"

    # 4. Llamar al servicio para traer e insertar tweets (uno por cada perfil)
    service = TwitterService()
    total_inserted = 0
    for profile_id in profile_ids:
        inserted = await service.fetch_and_store_tweets(
            query=query,
            max_results=max_results,
            profile_id=profile_id,
            campaign_id=campaign_id,
            type_id=type_id,
            session=session
        )
        total_inserted += inserted
    return {"tweets_inserted": total_inserted}
