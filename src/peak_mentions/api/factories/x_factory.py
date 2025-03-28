from polyfactory.factories.pydantic_factory import ModelFactory
from src.peak_mentions.api.models.x import XMention

class XMentionFactory(ModelFactory[XMention]):
    __model__ = XMention