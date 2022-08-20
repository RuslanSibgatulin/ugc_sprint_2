from uuid import UUID

from pydantic import BaseModel


class ViewEvent(BaseModel):
    user_id: UUID
    film_id: UUID
    viewed_frame: int
    total_frames: int
