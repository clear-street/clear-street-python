# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .watchlist_entry_list import WatchlistEntryList
from ..shared.base_response import BaseResponse

__all__ = ["WatchlistGetWatchlistsResponse"]


class WatchlistGetWatchlistsResponse(BaseResponse):
    data: WatchlistEntryList
