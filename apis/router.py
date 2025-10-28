from apis.reddit import fetch_top_poster
from fastapi import APIRouter


api_router = APIRouter()

# Reddit endpoints
api_router.include_router(fetch_top_poster.router, prefix="/reddit", tags=["Reddit"])
