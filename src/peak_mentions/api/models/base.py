from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class BaseMention(BaseModel):
    text: str
    author: str
    created_date: datetime
    media: Optional[List[HttpUrl]] = []