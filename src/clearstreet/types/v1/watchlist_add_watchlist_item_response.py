# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .add_watchlist_item_data import AddWatchlistItemData

__all__ = ["WatchlistAddWatchlistItemResponse"]


class WatchlistAddWatchlistItemResponse(BaseResponse):
    data: AddWatchlistItemData
    """Response data for adding a watchlist item"""
