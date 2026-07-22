# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .cancel_order_request import CancelOrderRequest

__all__ = ["PrefillCancelOrderAction"]


class PrefillCancelOrderAction(BaseModel):
    """Cancel-order prefill action."""

    orders: List[CancelOrderRequest]
    """Orders to cancel using the same identifiers required by the cancel-order API."""
