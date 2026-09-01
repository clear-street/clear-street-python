# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .feed_item_kind import FeedItemKind
from .feed_item_metric import FeedItemMetric

__all__ = ["FeedItem"]


class FeedItem(BaseModel):
    """One item in the caller's feed."""

    id: str
    """Unique item id.

    Also the pagination cursor: pass it as `cursor` to fetch the items that follow
    it.
    """

    headline: str
    """Headline text."""

    kind: FeedItemKind
    """What the item is about."""

    published_at: datetime
    """When the item's content was published."""

    summary: str
    """Summary text."""

    metric: Optional[FeedItemMetric] = None
    """
    The item's headline number. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    occurs_at: Optional[datetime] = None
    """
    When the underlying event is expected to occur, for items about an upcoming
    event. When a null/undefined value is observed, it indicates it does not apply.
    """
