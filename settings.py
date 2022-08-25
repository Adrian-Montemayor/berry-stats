from functools import lru_cache
from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    """Settings management class"""
    flask_app: str
    flask_debug: str
    base_url = "https://pokeapi.co/api/v2/berry/?offset=0&limit=64"
    sprites_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    """One instance and re-use the same settings object"""
    return Settings()

settings = get_settings()