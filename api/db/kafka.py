import asyncio
from typing import Optional

from aiokafka import AIOKafkaProducer
from core.config import config


class KafkaHandler:
    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic: str, value: bytes, key: bytes) -> None:
        await self.producer.send_and_wait(topic=topic, value=value, key=key)


kafka_handler: Optional[KafkaHandler] = None


async def get_kafka_handler() -> KafkaHandler:
    loop = asyncio.get_event_loop()
    kafka_producer = AIOKafkaProducer(loop=loop, bootstrap_servers=config.kafka_uri)
    await kafka_producer.start()
    return KafkaHandler(kafka_producer)
