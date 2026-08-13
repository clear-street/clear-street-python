# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .trailing_offset_type import TrailingOffsetType

__all__ = ["OrderReplaceOrderParams"]


class OrderReplaceOrderParams(TypedDict, total=False):
    account_id: Required[int]

    limit_offset: Optional[str]
    """New limit offset for trailing stop-limit orders (signed)"""

    limit_price: Optional[str]
    """New limit price for the order"""

    quantity: Optional[str]
    """New quantity for the order"""

    stop_price: Optional[str]
    """New stop price for the order"""

    trailing_offset: Optional[str]
    """New trailing offset for trailing orders"""

    trailing_offset_type: Optional[TrailingOffsetType]
    """New trailing offset type (PRICE or BPS)"""
