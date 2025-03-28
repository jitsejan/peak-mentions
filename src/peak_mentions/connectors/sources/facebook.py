import dlt
import requests
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)
BASE_URL = "http://localhost:8000"

def _get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "PeakMentions-FacebookBot/1.0"
    })
    return session

@dlt.source
def facebook_source():
    """
    A DLT source for extracting Facebook data from structured and scraped endpoints.
    """
    session = _get_session()

    @dlt.resource(name="facebook_structured")
    def structured() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/api/facebook")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching structured Facebook data: {e}")
            yield from []

    @dlt.resource(name="facebook_scraped")
    def scraped() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/scraped/facebook")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching scraped Facebook data: {e}")
            yield from []

    return [structured(), scraped()]