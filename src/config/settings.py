from functools import lru_cache
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "users"
    PROJECT_VERSION: str = "0.1.0"
    OPEN_API_URL: str = "/api/v1/openapi.json"

    # database
    DB_ENGINE: str = os.environ.get("DB_ENGINE", "postgresql")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
    DB_SERVER: str = os.getenv("DB_SERVER", "postgres-users")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "users")

    DB_URI: str = (
        f"//{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    )
    DB_URL: str = f"{DB_ENGINE}:{DB_URI}"


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()


settings = get_settings()

print(settings.DB_URL)