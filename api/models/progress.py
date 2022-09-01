from models.mixins import CreeateMixin
from pydantic.main import BaseModel


class MovieProgressBase(BaseModel):
    movie_id: str
    time: int
    total_time: int


class MovieProgress(MovieProgressBase, CreeateMixin):
    user_id: str
