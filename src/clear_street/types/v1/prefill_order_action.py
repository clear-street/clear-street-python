# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .accounts.new_order_request import NewOrderRequest
from .accounts.cancel_order_request import CancelOrderRequest

__all__ = ["PrefillOrderAction", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    """Create one or more new orders."""

    action_type: Literal["NEW"]

    orders: List[NewOrderRequest]
    """Orders to prefill using the same shape accepted by the orders API."""


class UnionMember1(BaseModel):
    """Cancel one or more existing orders."""

    action_type: Literal["CANCEL"]

    orders: List[CancelOrderRequest]
    """Orders to cancel using the same identifiers required by the cancel-order API."""


PrefillOrderAction: TypeAlias = Union[UnionMember0, UnionMember1]
