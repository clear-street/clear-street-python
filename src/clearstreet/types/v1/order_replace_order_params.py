# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OrderReplaceOrderParams"]


class OrderReplaceOrderParams(TypedDict, total=False):
    account_id: Required[int]

    limit_price: Optional[str]
    """New limit price for the order"""

    quantity: Optional[str]
    """New quantity for the order"""

    stop_price: Optional[str]
    """New stop price for the order"""
