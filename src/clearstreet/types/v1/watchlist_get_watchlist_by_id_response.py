# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .watchlist_detail import WatchlistDetail
from ..shared.base_response import BaseResponse

__all__ = ["WatchlistGetWatchlistByIDResponse"]


class WatchlistGetWatchlistByIDResponse(BaseResponse):
    data: WatchlistDetail
    """Detailed watchlist with all items"""
