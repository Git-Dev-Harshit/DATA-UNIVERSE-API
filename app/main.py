from apis.router import api_router
from fastapi import FastAPI

app = FastAPI(title="Multi-Platform API Aggregator for Data Scraping")

app.include_router(api_router, prefix="/api/v1")
