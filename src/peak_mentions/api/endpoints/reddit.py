from fastapi import APIRouter
from src.peak_mentions.api.factories.reddit_factory import RedditMentionFactory
from src.peak_mentions.api.factories.scraped.reddit_scraped import generate_scraped_reddit_mention

router = APIRouter()

@router.get("/api/reddit")
def get_reddit():
    return RedditMentionFactory.batch(5)

@router.get("/scraped/reddit")
def get_scraped_reddit():
    return [generate_scraped_reddit_mention() for _ in range(5)]
