import tweepy
from dotenv import load_dotenv
from os import getenv
import sys

load_dotenv()

def check_twitter_credentials():
    bearer_token = getenv("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        print("Error: No se encontró TWITTER_BEARER_TOKEN en las variables de entorno")
        print("Por favor, configura la variable de entorno TWITTER_BEARER_TOKEN")
        sys.exit(1)
    return bearer_token

# def convert_to_post(tweets_list: list[])

def tweet_query_builder(accounts: list[str], keyword: str) -> str:
    # Build accounts filter.
    accounts_filter = " OR ".join([f"from:{account}" for account in accounts])
    accounts_filter = f"({accounts_filter})"

    # Combine everything with the keyword.
    query = f"{accounts_filter} {keyword}"
    return query

def main():
    try:
        # Verificar credenciales
        bearer_token = check_twitter_credentials()

        # Inicializar cliente
        client = tweepy.Client(bearer_token=bearer_token)

        accounts = [
            "DarioAlexander1",
            "KeylinAcosta",
            "kpininimemes"
        ]

        start_date = "2025-04-30"
        end_date = "2025-05-1"
        keyword = "barrick"

        query = tweet_query_builder(accounts, keyword)
        print(f"Consulta generada: {query}")

        response = client.search_recent_tweets(
            query,
            tweet_fields=["public_metrics", "author_id", "created_at"]
        )

        for tweet in response.data:
            print(f"Tweet: {tweet.text}")
            print(f"Metrics: {tweet.public_metrics}")



    except tweepy.errors.Unauthorized:
        print("Error: Token de autenticación inválido o expirado")
        print("Por favor, verifica que tu TWITTER_BEARER_TOKEN sea válido")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()