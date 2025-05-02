"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
import tweepy  # type: ignore
import os
from sqlmodel import select
from app.database import SessionDep
from app.models import Profile

class TwitterService:
    """
    Servicio para obtener publicaciones de Twitter usando la API v2 y Tweepy.
    Metodos:
    Inicializador: Construye la instacia del servicio inicializando el cliente de tweepy
    utilizando en Bearer Token.
    Posts_Query_Builder: Construye el query utilizado para buscar los posts de usuarios

    """
    def __init__(self):
        """
        Inicializa el cliente de Tweepy usando el Bearer Token de las variables de entorno.
        """
        self.client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))

    def get_user_tweets(self, username: str, max_results: int = 10):
        """
        Obtiene los tweets más recientes de un usuario por su nombre de usuario.

        Args:
            username (str): Nombre de usuario de Twitter (sin @).
            max_results (int): Número máximo de tweets a obtener (por defecto 10).

        Returns:
            list[str]: Lista de textos de los tweets encontrados.
        """
        user = self.client.get_user(username=username)
        tweets = self.client.get_users_tweets(user.data.id, max_results=max_results)
        return [tweet.text for tweet in tweets.data] if tweets.data else []

    @staticmethod
    def posts_query_builder(accounts: list[str], start_date: str, end_date: str, keyword: str) -> str:
        """
        Build a query to retrieve posts from specified accounts, within a date range,
        that include a certain keyword or hashtag.

        Args:
            accounts (list): List of account names (strings) to filter posts.
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            keyword (str): The keyword or hashtag to search for.
        
        Returns:
            str: The constructed query string.
        """
        # Build accounts filter.
        accounts_filter = " OR ".join([f"from:{account}" for account in accounts])
        accounts_filter = f"({accounts_filter})"
        
        # Build date range filter.
        date_filter = f"since:{start_date} until:{end_date}"
        
        # Combine everything with the keyword.
        query = f"{accounts_filter} {keyword} {date_filter}"
        return query
    
    def get_user_from_db(self, db: SessionDep, username: Profile):
        """
        Obtiene el nombre de usuario de la base de datos.

        Args:
            db: Sesión de la base de datos.
            username (Profile): Nombre de usuario a buscar.

        Returns:
            str: Nombre de usuario encontrado o None si no existe.
        """
        stmt = select(Profile).where(Profile.handle == username.handle)
        user = db.exec(stmt).first()
        return user.handle if user else None