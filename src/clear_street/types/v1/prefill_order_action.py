# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .order_payload import OrderPayload
from .prefill_order_action_type import PrefillOrderActionType

__all__ = ["PrefillOrderAction"]


class PrefillOrderAction(BaseModel):
    """Action to prefill order details for user confirmation.

    The user must review and authorize the order before submission to the trading API.
    This action provides parsed order data that can be used to prefill an order ticket UI
    or submitted directly via the orders API after user confirmation.
    """

    action_type: PrefillOrderActionType
    """Order operation represented by this prefill action."""

    orders: List[OrderPayload]
    """The orders to prefill"""
