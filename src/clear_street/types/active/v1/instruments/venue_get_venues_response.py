# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .venue_list import VenueList
from ....shared.base_response import BaseResponse

__all__ = ["VenueGetVenuesResponse"]


class VenueGetVenuesResponse(BaseResponse):
    data: VenueList
