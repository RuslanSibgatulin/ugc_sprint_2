from datetime import datetime

from models.like import MovieLike
from models.mixins import CreeateMixin
from pydantic.main import BaseModel


class ReviewBase(BaseModel):
    movie_id: str
    text: str
    score: int


class ReviewFull(ReviewBase, CreeateMixin):
    user_id: str
    time: datetime

    @property
    def like(self) -> MovieLike:
        return MovieLike(score=self.score, movie_id=self.movie_id, user_id=self.user_id)
