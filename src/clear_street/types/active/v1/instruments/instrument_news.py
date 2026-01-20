# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["InstrumentNews"]


class InstrumentNews(BaseModel):
    """A news or press release item related to an instrument"""

    published_at: datetime
    """The published date/time of the article in UTC"""

    symbol: str
    """The trading symbol associated with the news item"""

    title: str
    """The headline/title of the article"""

    type: Literal["NEWS", "PRESS_RELEASE"]
    """Classification of the item"""

    url: str
    """Canonical URL to the full article"""

    image_url: Optional[str] = None
    """URL of an associated image if provided by the source"""

    publisher: Optional[str] = None
    """The publisher or newswire source"""

    site: Optional[str] = None
    """The primary domain/site of the publisher"""

    text: Optional[str] = None
    """The full or excerpted article body"""
