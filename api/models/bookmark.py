from pydantic import BaseModel

from models.mixins import CreeateMixin


class BookmarkBase(BaseModel):
    movie_id: str


class Bookmark(BookmarkBase, CreeateMixin):
    user_id: str


class BookmarkFull(Bookmark):
    id: str
