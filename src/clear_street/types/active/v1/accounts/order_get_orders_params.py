# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ....._types import Base64FileInput
from ....._utils import PropertyInfo
from .order_status import OrderStatus
from ...security_type import SecurityType
from ...security_id_source import SecurityIDSource

__all__ = ["OrderGetOrdersParams"]


class OrderGetOrdersParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

    to: Required[str]
    """The end date and time for the query range, inclusive (ISO 8601 format)"""

    page_size: int
    """
    The number of items to return per page (only used when page_token is not
    provided)
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    security_id: str
    """Filter by security ID"""

    security_id_source: SecurityIDSource
    """Source for the security ID filter"""

    security_type: SecurityType
    """Security type filter (e.g., COMMON_STOCK, PREFERRED_STOCK)"""

    status: OrderStatus
    """Filter by order status"""

    symbol: str
    """Filter by symbol"""
