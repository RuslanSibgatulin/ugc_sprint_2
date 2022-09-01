import json
import logging
from functools import lru_cache

from core.config import config
from db.kafka import KafkaHandler, get_kafka_handler
from fastapi import Depends
from models.progress import MovieProgress

logger = logging.getLogger(__name__)


class ProgressService:
    def __init__(self, storage: KafkaHandler):
        self.storage = storage

    async def send_movie_progress(self, view_progress: MovieProgress):
        value = json.dumps(view_progress.dict()).encode()
        key = f"{view_progress.user_id}::{view_progress.movie_id}".encode()
        await self.storage.send(topic=config.MOVIE_PROGRESS_TOPIC, value=value, key=key)


@lru_cache()
def get_progress_service(
    event_storage: KafkaHandler = Depends(get_kafka_handler),
) -> ProgressService:
    return ProgressService(storage=event_storage)
