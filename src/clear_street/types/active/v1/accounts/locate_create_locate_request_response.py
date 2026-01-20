# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locate_order_list import LocateOrderList
from ....shared.base_response import BaseResponse

__all__ = ["LocateCreateLocateRequestResponse"]


class LocateCreateLocateRequestResponse(BaseResponse):
    data: LocateOrderList
