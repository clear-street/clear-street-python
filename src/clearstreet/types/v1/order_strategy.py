# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["OrderStrategy", "Type", "UnionMember1", "UnionMember2"]


class Type(BaseModel):
    """Smart Order Router. Routes the order to the best available venue(s)."""

    type: Literal["SOR"]
    """Execution strategy type."""


class UnionMember1(BaseModel):
    """Volume-Weighted Average Price.

    Works the order to track the volume-weighted average price over the execution window.
    """

    type: Literal["VWAP"]
    """Execution strategy type."""

    end_at: Optional[datetime] = None
    """UTC timestamp (RFC 3339) by which to finish working the order.

    Defaults to market close.
    """

    start_at: Optional[datetime] = None
    """UTC timestamp (RFC 3339) at which to begin working the order.

    Defaults to the time the order is received.
    """


class UnionMember2(BaseModel):
    """Time-Weighted Average Price.

    Spreads execution evenly across the execution window.
    """

    type: Literal["TWAP"]
    """Execution strategy type."""

    end_at: Optional[datetime] = None
    """UTC timestamp (RFC 3339) by which to finish working the order.

    Defaults to market close.
    """

    start_at: Optional[datetime] = None
    """UTC timestamp (RFC 3339) at which to begin working the order.

    Defaults to the time the order is received.
    """


OrderStrategy: TypeAlias = Union[Type, UnionMember1, UnionMember2]
