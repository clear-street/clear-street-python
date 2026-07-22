# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .prefill_modify_order_request import PrefillModifyOrderRequest

__all__ = ["PrefillModifyOrderAction"]


class PrefillModifyOrderAction(BaseModel):
    """Modify-order prefill action."""

    orders: List[PrefillModifyOrderRequest]
    """Modification targets and deltas needed to construct replace-order API requests."""
