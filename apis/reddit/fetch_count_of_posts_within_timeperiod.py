from apis.reddit.utils import get_post_count_within_timeperiod
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class CountPostsRequest(BaseModel):
    subreddits: List[str]
    minutes: Optional[int] = 1440  # Default 24 hours
    limit: Optional[int] = 1000

@router.post("/fetch_count_of_posts_withinn_timeperiod")
async def fetch_count_of_posts_withinn_timeperiod(request: CountPostsRequest):
    """
    Fetch count of posts made in each subreddit within the given time period.
    Time period is passed in minutes (default: 1440 = 24 hours).
    """
    results = {}
    for subreddit in request.subreddits:
        try:
            count = await get_post_count_within_timeperiod(
                subreddit_name=subreddit,
                minutes=request.minutes,
                limit=request.limit
            )
            results[subreddit] = {"post_count": count}
        except Exception as e:
            results[subreddit] = {"error": str(e)}
    return results
