# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TimeInForce"]

TimeInForce: TypeAlias = Literal[
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
    "OTHER",
]
