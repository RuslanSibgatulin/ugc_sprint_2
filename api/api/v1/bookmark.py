from fastapi import APIRouter, Depends, Security

from models.bookmark import Bookmark, BookmarkBase, BookmarkFull
from services.bookmarks import BookmarkService, get_bookmark_service
from users.security import get_user

router = APIRouter(tags=["Bookmark"])


@router.post("/bookmarks")
async def add_bookmark(
        bookmark: BookmarkBase,
        event_sender: BookmarkService = Depends(get_bookmark_service),
        user_id: str = Security(get_user),
) -> None:
    review_full = Bookmark.get_object(bookmark, user_id)
    await event_sender.add_bookmark(review_full)


@router.delete("/bookmarks/{bookmark_id}")
async def delete_bookmark(
        bookmark_id: str,
        event_sender: BookmarkService = Depends(get_bookmark_service),
        user_id: str = Security(get_user),
) -> None:
    await event_sender.delete_bookmark(bookmark_id, user_id)


@router.get("/bookmarks")
async def get_bookmarks(
        event_sender: BookmarkService = Depends(get_bookmark_service),
        user_id: str = Security(get_user),
) -> list[BookmarkFull]:
    bookmarks = await event_sender.get_bookmarks(user_id)
    return bookmarks
