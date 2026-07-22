# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OrderStatus"]

OrderStatus: TypeAlias = Literal[
    "PENDING_NEW",
    "NEW",
    "PARTIALLY_FILLED",
    "FILLED",
    "CANCELED",
    "REJECTED",
    "EXPIRED",
    "PENDING_CANCEL",
    "PENDING_REPLACE",
    "REPLACED",
    "DONE_FOR_DAY",
    "STOPPED",
    "SUSPENDED",
    "CALCULATED",
    "OTHER",
]
