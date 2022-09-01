import logging
from functools import lru_cache
from typing import Optional
from uuid import uuid4

from core.config import config
from db.mongo import get_mongo_client
from fastapi import Depends
from models.like import MovieLike, ReviewLike
from models.review import ReviewFull
from motor.motor_asyncio import AsyncIOMotorClient

logger = logging.getLogger(__name__)


class RatingService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo
        self.db = self.mongo[config.MONGO_DB]

    async def add_review_like(self, like: ReviewLike) -> str:
        collection = self.db[config.MONGO_REVIEW_LIKES_COLLECTION_NAME]
        like = await collection.insert_one(like.dict())
        return like.inserted_id

    async def add_movie_like(self, like: MovieLike) -> str:
        collection = self.db[config.MONGO_MOVIE_LIKES_COLLECTION_NAME]
        like = await collection.insert_one(like.dict())
        return like.inserted_id

    async def get_avg_movie_rating(self, movie_id: str) -> Optional[float]:
        collection = self.db[config.MONGO_MOVIE_LIKES_COLLECTION_NAME]
        pipeline = [{"$match": {"movie_id": movie_id}}, {"$group": {"_id": "_id", "avg_score": {"$avg": "$score"}}}]
        async for result in collection.aggregate(pipeline):
            if result:
                return round(result["avg_score"], 2)
            return None

    async def add_review(self, review: ReviewFull) -> None:
        rewiew_like = review.like
        await self.add_movie_like(rewiew_like)
        collection = self.db[config.MONGO_REVIEWS_COLLECTION_NAME]
        review_dict = review.dict()
        review_dict["_id"] = str(uuid4())
        await collection.insert_one(review_dict)

    async def get_reviews(self, movie_id: str) -> list[ReviewFull]:
        collection = self.db[config.MONGO_REVIEWS_COLLECTION_NAME]
        reviews = []
        async for review in collection.find({"movie_id": movie_id}):
            reviews.append(ReviewFull(**review))
        return reviews


@lru_cache
def get_rating_service(
    mongo_storage: AsyncIOMotorClient = Depends(get_mongo_client),
) -> RatingService:
    return RatingService(mongo=mongo_storage)
