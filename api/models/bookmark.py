from models.mixins import CreeateMixin
from pydantic import BaseModel


class BookmarkBase(BaseModel):
    movie_id: str


class Bookmark(BookmarkBase, CreeateMixin):
    user_id: str


class BookmarkFull(Bookmark):
    id: str
