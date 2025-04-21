"""
Servicio para interactuar con la API de Twitter usando Tweepy.
Obtiene tweets de usuarios autenticándose con el Bearer Token.
"""
import tweepy  # type: ignore
import os

class TwitterService:
    """
    Servicio para obtener publicaciones de Twitter usando la API v2 y Tweepy.
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
    