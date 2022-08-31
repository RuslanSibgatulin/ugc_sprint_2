from pydantic.main import BaseModel

from models.mixins import CreeateMixin


class MovieProgressBase(BaseModel):
    movie_id: str
    time: int
    total_time: int


class MovieProgress(MovieProgressBase, CreeateMixin):
    user_id: str
