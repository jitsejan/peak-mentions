import dlt
import requests
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)
BASE_URL = "http://localhost:8000"

def _get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "PeakMentions-XBot/1.0"
    })
    return session

@dlt.source
def x_source():
    """
    A DLT source for extracting X data from structured and scraped endpoints.
    """
    session = _get_session()

    @dlt.resource(name="x_structured")
    def structured() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/api/x")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching structured X data: {e}")
            yield from []

    @dlt.resource(name="x_scraped")
    def scraped() -> List[Dict]:
        try:
            res = session.get(f"{BASE_URL}/scraped/x")
            res.raise_for_status()
            yield from res.json()
        except requests.RequestException as e:
            logger.warning(f"Error fetching scraped X data: {e}")
            yield from []

    return [structured(), scraped()]