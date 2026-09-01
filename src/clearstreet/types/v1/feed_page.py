# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .feed_item import FeedItem

__all__ = ["FeedPage"]


class FeedPage(BaseModel):
    """One page of the caller's feed."""

    items: List[FeedItem]
    """Feed items, in feed order."""

    next_cursor: Optional[str] = None
    """Cursor for the page after this one: the last item's id.

    Absent only when there are no items to serve. When a null/undefined value is
    observed, it indicates that there is no available data.
    """
