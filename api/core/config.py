from typing import List

from pydantic import BaseSettings


class Config(BaseSettings):
    MOVIE_PROGRESS_TOPIC = "movie_progress"
    KAFKA_HOST: str = "localhost"
    KAFKA_PORT: int = 9092
    SECRET_KEY: str = "extra secret"
    HASH_ALGORITHM: str = "SHA-256"
    MONGO_HOST: str = "127.0.0.1"
    MONGO_PORT: int = 27017

    @property
    def kafka_uri(self) -> List[str]:
        return [f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"]

    @property
    def mongo_uri(self) -> str:
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"


config = Config()
