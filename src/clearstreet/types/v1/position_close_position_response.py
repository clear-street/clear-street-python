# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .order_list import OrderList
from ..shared.base_response import BaseResponse

__all__ = ["PositionClosePositionResponse"]


class PositionClosePositionResponse(BaseResponse):
    data: OrderList
