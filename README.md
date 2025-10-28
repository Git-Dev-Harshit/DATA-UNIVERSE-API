🧠 DATA-UNIVERSE-API — Reddit Top Posters API

This project provides a FastAPI-based API to fetch the top posters from one or more subreddits within a given time period.
It uses asyncpraw to interact with Reddit asynchronously, following a clean modular structure that can scale to other platforms (e.g., YouTube, Twitter, etc.).

🔹 Features

Fetch top posters for multiple subreddits simultaneously

Fully asynchronous for better performance

Configurable parameters:

top_n → number of top users to return (default: 60)

days → time window in days (default: 30)

limit → number of recent posts to scan (default: 1000)

JSON-based API response


🔹 Project Structure
DATA-UNIVERSE-API
│
├── app
│   └── main.py
│
└── apis
    ├── router.py
    │
    └── reddit
        ├── __init__.py
        ├── fetch_posts.py      # Reddit routes
        └── utils.py             # Helper functions


🔹 Prerequisites

Python 3.10+

Reddit API credentials
Obtain them by creating a Reddit app: https://www.reddit.com/prefs/apps

Add your credentials to a .env file in the project root:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# Optional
HOST=127.0.0.1
PORT=8000

🔹 Installation

Install required dependencies:

pip install fastapi uvicorn asyncpraw python-dotenv

🔹 Running the Server

Run the FastAPI app with:

uvicorn app.main:app --reload


The API will be available at:
👉 http://127.0.0.1:8000

Swagger Docs (API UI):
👉 http://127.0.0.1:8000/docs