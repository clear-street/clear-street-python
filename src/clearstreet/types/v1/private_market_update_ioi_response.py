# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .private_markets.ioi_listing_resource import IoiListingResource

__all__ = ["PrivateMarketUpdateIoiResponse"]


class PrivateMarketUpdateIoiResponse(BaseResponse):
    data: IoiListingResource
    """IOI list item with the campaign identity needed to render it."""
