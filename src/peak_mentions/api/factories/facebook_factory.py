from polyfactory.factories.pydantic_factory import ModelFactory
from src.peak_mentions.api.models.facebook import FacebookMention

class FacebookMentionFactory(ModelFactory[FacebookMention]):
    __model__ = FacebookMention