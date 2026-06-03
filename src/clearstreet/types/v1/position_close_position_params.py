# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PositionClosePositionParams"]


class PositionClosePositionParams(TypedDict, total=False):
    account_id: Required[int]

    cancel_orders: Optional[bool]
    """
    Whether to cancel existing open orders for the position before submitting
    closing orders.
    """
