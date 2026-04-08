# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .order import Order
from ....shared.base_response import BaseResponse

__all__ = ["OrderReplaceOrderResponse"]


class OrderReplaceOrderResponse(BaseResponse):
    data: Order
    """A trading order with its current state and execution details.

    This is the unified API representation of an order across its lifecycle,
    combining data from execution reports, order status queries, and parent/child
    tracking.
    """
