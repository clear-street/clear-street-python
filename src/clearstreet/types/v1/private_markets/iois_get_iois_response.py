# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .ioi_listing_resource_list import IoiListingResourceList

__all__ = ["IoisGetIoisResponse"]


class IoisGetIoisResponse(BaseResponse):
    data: IoiListingResourceList
