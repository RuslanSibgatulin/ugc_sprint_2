import asyncio
from logging import getLogger
from typing import Optional

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaConnectionError
from core.config import config

logger = getLogger(__name__)


class KafkaHandler:
    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic: str, value: bytes, key: bytes) -> None:
        await self.producer.send_and_wait(topic=topic, value=value, key=key)


kafka_handler: Optional[KafkaHandler] = None


async def get_kafka_handler() -> KafkaHandler:
    loop = asyncio.get_event_loop()
    kafka_producer = AIOKafkaProducer(loop=loop, bootstrap_servers=config.kafka_uri)
    try_ = 1
    while True:
        try:
            await kafka_producer.start()
            break
        except KafkaConnectionError:
            logger.error(f"Can`t connect to kafka. Try {try_}")
            try_ += 1
            await asyncio.sleep(5)
    return KafkaHandler(kafka_producer)
