from fastapi import APIRouter, Depends, Security
from models.progress import MovieProgress
from services.progress import ProgressService, get_progress_service
from users.security import get_user

router = APIRouter(tags=['Events'])


@router.post("/progress")
async def send_view_progress(
    movie_progress: MovieProgress,
    event_sender: ProgressService = Depends(get_progress_service),
    user_id: str = Security(get_user),
):
    movie_progress.user_id = user_id
    await event_sender.send_movie_progress(movie_progress)
