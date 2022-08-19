from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    KAFKA_URI: List = ['localhost:9092']
    SECRET_KEY: str = "extra secret"
    HASH_ALGORITHM: str = 'sha256'


settings = Settings()
