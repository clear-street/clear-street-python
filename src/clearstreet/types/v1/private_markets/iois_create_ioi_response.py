# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ioi_listing_resource import IoiListingResource
from ...shared.base_response import BaseResponse

__all__ = ["IoisCreateIoiResponse"]


class IoisCreateIoiResponse(BaseResponse):
    data: IoiListingResource
    """IOI list item with the campaign identity needed to render it."""
