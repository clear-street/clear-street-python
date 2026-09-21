# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrderStrategyParam", "Type", "UnionMember1", "UnionMember2"]


class Type(TypedDict, total=False):
    """Smart Order Router. Routes the order to the best available venue(s)."""

    type: Required[Literal["SOR"]]
    """Execution strategy type."""


class UnionMember1(TypedDict, total=False):
    """Volume-Weighted Average Price.

    Works the order to track the volume-weighted average price over the execution window.
    """

    type: Required[Literal["VWAP"]]
    """Execution strategy type."""

    end_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC timestamp (RFC 3339) by which to finish working the order.

    Defaults to market close.
    """

    start_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC timestamp (RFC 3339) at which to begin working the order.

    Defaults to the time the order is received.
    """


class UnionMember2(TypedDict, total=False):
    """Time-Weighted Average Price.

    Spreads execution evenly across the execution window.
    """

    type: Required[Literal["TWAP"]]
    """Execution strategy type."""

    end_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC timestamp (RFC 3339) by which to finish working the order.

    Defaults to market close.
    """

    start_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC timestamp (RFC 3339) at which to begin working the order.

    Defaults to the time the order is received.
    """


OrderStrategyParam: TypeAlias = Union[Type, UnionMember1, UnionMember2]
