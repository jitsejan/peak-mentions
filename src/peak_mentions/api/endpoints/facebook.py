from fastapi import APIRouter
from src.peak_mentions.api.factories.facebook_factory import FacebookMentionFactory
from src.peak_mentions.api.factories.scraped.facebook_scraped import generate_scraped_facebook_mention

router = APIRouter()

@router.get("/api/facebook")
def get_facebook():
    return FacebookMentionFactory.batch(5)

@router.get("/scraped/facebook")
def get_scraped_facebook():
    return [generate_scraped_facebook_mention() for _ in range(5)]
