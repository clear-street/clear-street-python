# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrderReplaceOrderParams"]


class OrderReplaceOrderParams(TypedDict, total=False):
    account_id: Required[int]

    limit_price: Optional[str]
    """New limit price for the order"""

    quantity: Optional[str]
    """New quantity for the order"""

    stop_price: Optional[str]
    """New stop price for the order"""

    time_in_force: Literal[
        "DAY",
        "GOOD_TILL_CANCEL",
        "IMMEDIATE_OR_CANCEL",
        "FILL_OR_KILL",
        "GOOD_TILL_DATE",
        "AT_THE_OPENING",
        "AT_THE_CLOSE",
        "GOOD_TILL_CROSSING",
        "GOOD_THROUGH_CROSSING",
        "AT_CROSSING",
    ]
    """New time in force for the order"""
