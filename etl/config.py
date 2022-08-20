from typing import List
from pydantic import BaseSettings, Field


class ETLSettings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    BATCH_SIZE: int = 10
    READ_TIMEOUT: int = 1000
    CLICKHOUSE_SERVER: str = "127.0.0.1"
    KAFKA_TOPIC: str = Field('movie_progress', env='MOVIE_PROGRESS_TOPIC')
    KAFKA_HOST: str = "localhost"
    KAFKA_PORT: int = 9092

    @property
    def kafka_uri(self) -> List[str]:
        return f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"


settings = ETLSettings()
