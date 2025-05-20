import asyncio
from app.services.twitter_service import TwitterService

# Parámetros de prueba (ajusta según tus datos reales)
TEAM = ["XDevelopers"]  # Lista de handles de Twitter
START_DATE = "2025-05-01"
END_DATE = "2025-05-20"
MAX_RESULTS = 10
PROFILE_ID = 1
CAMPAIGN_ID = 1
TYPE_ID = 1

async def main():
    service = TwitterService()
    query = service.create_query(TEAM)
    try:
        inserted = await service.fetch_and_store_tweets(
            query=query,
            max_results=MAX_RESULTS,
            profile_id=PROFILE_ID,
            campaign_id=CAMPAIGN_ID,
            type_id=TYPE_ID
        )
        print(f"Tweets insertados: {inserted}")
    except Exception as e:
        print(f"Error al insertar tweets: {e}")

if __name__ == "__main__":
    asyncio.run(main())
