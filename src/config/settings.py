from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "users"
    PROJECT_VERSION: str = "0.1.0"
    OPEN_API_URL: str = "/openapi.json"


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()


settings = get_settings()
