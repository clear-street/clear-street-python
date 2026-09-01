# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .feed_page import FeedPage
from ..shared.base_response import BaseResponse

__all__ = ["OmniFeedGetFeedResponse"]


class OmniFeedGetFeedResponse(BaseResponse):
    data: FeedPage
    """One page of the caller's feed."""
