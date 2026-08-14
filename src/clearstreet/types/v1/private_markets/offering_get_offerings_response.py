# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .offering_card_list import OfferingCardList
from ...shared.base_response import BaseResponse

__all__ = ["OfferingGetOfferingsResponse"]


class OfferingGetOfferingsResponse(BaseResponse):
    data: OfferingCardList
