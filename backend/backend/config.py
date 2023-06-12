from pydantic import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv(".env")


class Settings(BaseSettings):
    """Class to store settings for the application"""

    app_name: str = "Bug Tracker"
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = "a8be7e720623623ee4f9e91a48b0bc46aea2643f59a7e16852795f0675f47cef"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440

    class Config:
        env_file = ".env"
