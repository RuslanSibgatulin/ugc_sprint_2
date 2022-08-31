from pydantic.main import BaseModel

from models.mixins import CreeateMixin


class MovieLikeBase(BaseModel):
    movie_id: str
    score: int


class ReviewLikeBase(BaseModel):
    review_id: str
    score: int


class MovieLike(MovieLikeBase, CreeateMixin):
    user_id: str


class ReviewLike(ReviewLikeBase, CreeateMixin):
    user_id: str
