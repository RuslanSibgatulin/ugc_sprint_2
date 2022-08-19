from typing import List

from pydantic import BaseSettings


class Config(BaseSettings):
    MOVIE_PROGRESS_TOPIC = "movie_progress"
    KAFKA_HOST: str = "localhost"
    KAFKA_PORT: int = 9092
    SECRET_KEY: str = "extra secret"
    HASH_ALGORITHM: str = "SHA-256"

    @property
    def kafka_uri(self) -> List[str]:
        return [f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"]


config = Config()
