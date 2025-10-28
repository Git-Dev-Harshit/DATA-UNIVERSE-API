from datetime import datetime, timedelta, timezone
from collections import Counter
from dotenv import load_dotenv
import asyncpraw
import os

load_dotenv()

USER_AGENT = f"python:top_posters_bot:0.1 (by /{os.getenv('REDDIT_USERNAME')})"

async def get_top_posters(subreddit_name: str, days: int = 30, top_n: int = 60, limit: int = 1000):
    """
    Fetch top posters in a subreddit within a given time frame.
    """
    after_time = datetime.now(timezone.utc) - timedelta(days=days)
    authors = []

    async with asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=USER_AGENT,
    ) as reddit:
        
        subreddit = await reddit.subreddit(subreddit_name)
        async for submission in subreddit.new(limit=limit):
            if submission.created_utc >= after_time.timestamp() and submission.author:
                authors.append(submission.author.name)

    top_authors = Counter(authors).most_common(top_n)
    return top_authors
