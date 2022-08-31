from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from core.config import config


mongo_client: Optional[AsyncIOMotorClient] = None


async def get_mongo() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(config.mongo_uri)
    return client


async def get_mongo_client() -> AsyncIOMotorClient:
    return mongo_client
