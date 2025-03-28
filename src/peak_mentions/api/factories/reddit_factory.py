from polyfactory.factories.pydantic_factory import ModelFactory
from src.peak_mentions.api.models.reddit import RedditMention

class RedditMentionFactory(ModelFactory[RedditMention]):
    __model__ = RedditMention