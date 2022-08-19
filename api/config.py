from typing import List

from pydantic import BaseSettings


class Config(BaseSettings):
    MOVIE_PROGRESS_TOPIC = "movie_progress"
    KAFKA_URI: List = ["localhost:9092"]
    SECRET_KEY: str = "extra secret"
    HASH_ALGORITHM: str = "SHA-256"


config = Config()
