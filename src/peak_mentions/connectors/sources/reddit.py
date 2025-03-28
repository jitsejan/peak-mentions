import dlt
import requests
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)
BASE_URL = "http://localhost:8000"

def _get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "PeakMentions-RedditBot/1.0"
    })
    return session

@dlt.source
def reddit_source():
    """
    A DLT source for extracting Reddit data from structured and scraped endpoints.
    """
    session = _get_session()

    @dlt.resource(name="reddit_structured")
    def structured() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/api/reddit")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching structured Reddit data: {e}")
            yield from []

    @dlt.resource(name="reddit_scraped")
    def scraped() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/scraped/reddit")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching scraped Reddit data: {e}")
            yield from []

    return [structured(), scraped()]