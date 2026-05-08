# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AddWatchlistItemData"]


class AddWatchlistItemData(BaseModel):
    """Response data for adding a watchlist item"""

    item_id: str
    """ID of the created item"""
