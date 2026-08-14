# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .prefill_cancel_order_request import PrefillCancelOrderRequest

__all__ = ["PrefillCancelOrderAction"]


class PrefillCancelOrderAction(BaseModel):
    """Cancel-order prefill action."""

    orders: List[PrefillCancelOrderRequest]
    """Orders to cancel using the same identifiers required by the cancel-order API."""
