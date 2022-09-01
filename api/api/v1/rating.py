from typing import List

from fastapi import APIRouter, Depends, Security
from models.like import MovieLike, MovieLikeBase, ReviewLike, ReviewLikeBase
from models.review import ReviewBase, ReviewFull
from services.rating import RatingService, get_rating_service
from users.security import get_user

router = APIRouter(tags=["Rating"])


@router.post("/reviews")
async def add_review(
    review: ReviewBase,
    event_sender: RatingService = Depends(get_rating_service),
    user_id: str = Security(get_user),
) -> None:
    review_full = ReviewFull.get_object(review, user_id)
    await event_sender.add_review(review_full)


@router.get("/reviews/{movie_id}")
async def get_reviews(
    movie_id: str,
    event_sender: RatingService = Depends(get_rating_service),
) -> List[ReviewFull]:
    return await event_sender.get_reviews(movie_id)


@router.post("/movie-likes")
async def add_movie_like(
    like: MovieLikeBase,
    event_sender: RatingService = Depends(get_rating_service),
    user_id: str = Security(get_user),
) -> None:
    like_full = MovieLike.get_object(like, user_id)
    await event_sender.add_movie_like(like_full)


@router.get("/movie-likes/avg/{movie_id}")
async def get_avg_movie_rating(
    movie_id: str,
    event_sender: RatingService = Depends(get_rating_service),
) -> float:
    return await event_sender.get_avg_movie_rating(movie_id)


@router.post("/review-likes")
async def add_review_like(
    like: ReviewLikeBase,
    event_sender: RatingService = Depends(get_rating_service),
    user_id: str = Security(get_user),
) -> None:
    like_full = ReviewLike.get_object(like, user_id)
    await event_sender.add_review_like(like_full)
