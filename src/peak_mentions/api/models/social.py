from .base import BaseMention

from datetime import datetime

class SocialMention(BaseMention):
    publish_date: datetime
    likes: int
    is_forwarded_post: bool