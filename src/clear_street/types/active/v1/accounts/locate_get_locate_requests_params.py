# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ....._types import Base64FileInput
from ....._utils import PropertyInfo
from .locate_order_status import LocateOrderStatus

__all__ = ["LocateGetLocateRequestsParams"]


class LocateGetLocateRequestsParams(TypedDict, total=False):
    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    reference_id: str
    """Filter by client reference ID"""

    status: LocateOrderStatus
    """Filter by locate order status"""
