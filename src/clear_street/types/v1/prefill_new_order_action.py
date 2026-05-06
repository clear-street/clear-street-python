# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .accounts.new_order_request import NewOrderRequest

__all__ = ["PrefillNewOrderAction"]


class PrefillNewOrderAction(BaseModel):
    """New-order prefill action."""

    orders: List[NewOrderRequest]
    """Orders to prefill using the same shape accepted by the orders API."""
