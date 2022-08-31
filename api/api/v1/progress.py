from fastapi import APIRouter, Depends, Security

from models.progress import MovieProgress, MovieProgressBase
from services.progress import ProgressService, get_progress_service
from users.security import get_user

router = APIRouter(tags=['Events'])


@router.post("/progress")
async def send_view_progress(
    movie_progress: MovieProgressBase,
    event_sender: ProgressService = Depends(get_progress_service),
    user_id: str = Security(get_user),
):
    user_movie_progress = MovieProgress.get_object(movie_progress, user_id)
    await event_sender.send_movie_progress(user_movie_progress)
