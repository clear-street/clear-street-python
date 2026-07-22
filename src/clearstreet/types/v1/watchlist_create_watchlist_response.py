# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .watchlist_entry import WatchlistEntry
from ..shared.base_response import BaseResponse

__all__ = ["WatchlistCreateWatchlistResponse"]


class WatchlistCreateWatchlistResponse(BaseResponse):
    data: WatchlistEntry
    """Represents a user watchlist."""
