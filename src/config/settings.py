from functools import lru_cache
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "users"
    PROJECT_VERSION: str = "0.1.0"
    OPEN_API_URL: str = "/openapi.json"

    # database
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_USER", "postgres")
    DB_SERVER: str = os.getenv("DB_USER", "localhost")
    DB_PORT: str = os.getenv("DB_USER", "5432")
    DB_NAME: str = os.getenv("DB_USER", "usersdb")


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()


settings = get_settings()
