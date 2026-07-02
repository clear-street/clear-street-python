# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .new_order_request_param import NewOrderRequestParam

__all__ = ["OrderSubmitOrdersParams"]


class OrderSubmitOrdersParams(TypedDict, total=False):
    orders: Required[Iterable[NewOrderRequestParam]]
