from apis.reddit.utils import get_top_posters
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class TopPostersRequest(BaseModel):
    subreddits: List[str]
    top_n: Optional[int] = 60
    days: Optional[int] = 30
    limit: Optional[int] = 1000

@router.post("/top_posters")
async def top_posters_endpoint(request: TopPostersRequest):
    """
    Get top posters for one or more subreddits.
    """
    results = {}
    for subreddit in request.subreddits:
        try:
            top_authors = await get_top_posters(
                subreddit_name=subreddit,
                days=request.days,
                top_n=request.top_n,
                limit=request.limit
            )
            results[subreddit] = [{"user": user, "posts": count} for user, count in top_authors]
        except Exception as e:
            results[subreddit] = {"error": str(e)}
    return results
