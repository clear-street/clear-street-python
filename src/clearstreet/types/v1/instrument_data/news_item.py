# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .news_type import NewsType
from ...._models import BaseModel
from .news_instrument import NewsInstrument

__all__ = ["NewsItem"]


class NewsItem(BaseModel):
    """A single news item and its associated instruments."""

    instruments: List[NewsInstrument]
    """Instruments associated with this news item."""

    news_type: NewsType
    """Classification of the item."""

    published_at: datetime
    """The published date/time of the article in UTC."""

    publisher: str
    """The publisher or newswire source."""

    title: str
    """The headline/title of the article."""

    url: str
    """Canonical URL to the full article."""

    image_url: Optional[str] = None
    """
    URL of an associated image if provided by the source. When a null/undefined
    value is observed, it indicates that there is no available data.
    """

    site: Optional[str] = None
    """
    The primary domain/site of the publisher. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    text: Optional[str] = None
    """
    The full or excerpted article body. When a null/undefined value is observed, it
    indicates that there is no available data.
    """
