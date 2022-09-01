from models.mixins import CreeateMixin
from pydantic.main import BaseModel


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
