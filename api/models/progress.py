from pydantic.main import BaseModel


class MovieProgressBase(BaseModel):
    movie_id: str
    time: int
    total_time: int


class MovieProgress(MovieProgressBase):
    user_id: str

    @classmethod
    def get_progress(cls, user_id: str, base_progress: MovieProgressBase):
        payload = base_progress.dict()
        payload["user_id"] = user_id
        return cls(**payload)
