from pydantic.main import BaseModel


class MovieProgress(BaseModel):
    movie_id: str
    time: int
    total_time: int
    user_id: str = None
