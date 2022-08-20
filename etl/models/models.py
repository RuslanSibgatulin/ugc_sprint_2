from dataclasses import Field
from uuid import UUID

from pydantic import BaseModel


class ViewEvent(BaseModel):
    user_id: UUID
    film_id: UUID = Field(alias='movie_id')
    viewed_frame: int = Field(alias='time')
    total_frames: int = Field(alias='total_time')
