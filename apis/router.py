from apis.reddit import (
    fetch_top_poster, fetch_count_of_posts_within_timeperiod
)
from fastapi import APIRouter


api_router = APIRouter()

# Reddit endpoints
api_router.include_router(fetch_top_poster.router, prefix="/reddit", tags=["Reddit"])
api_router.include_router(fetch_count_of_posts_within_timeperiod.router, prefix="/reddit", tags=["Reddit"])