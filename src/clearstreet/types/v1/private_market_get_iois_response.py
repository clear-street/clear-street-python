# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .private_markets.ioi_listing_resource_list import IoiListingResourceList

__all__ = ["PrivateMarketGetIoisResponse"]


class PrivateMarketGetIoisResponse(BaseResponse):
    data: IoiListingResourceList
