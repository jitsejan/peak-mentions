from fastapi import APIRouter
from src.peak_mentions.api.factories.x_factory import XMentionFactory
from src.peak_mentions.api.factories.scraped.x_scraped import generate_scraped_x_mention

router = APIRouter()

@router.get("/api/x")
def get_x():
    return XMentionFactory.batch(5)

@router.get("/scraped/x")
def get_scraped_x():
    return [generate_scraped_x_mention() for _ in range(5)]