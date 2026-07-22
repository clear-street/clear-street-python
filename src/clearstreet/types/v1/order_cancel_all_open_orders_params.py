# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["OrderCancelAllOpenOrdersParams"]


class OrderCancelAllOpenOrdersParams(TypedDict, total=False):
    instrument_ids: SequenceNotStr[InstrumentIDOrSymbol]
    """
    Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
    symbols).
    """

    instrument_type: Literal["COMMON_STOCK", "INDEX", "OPTION", "CASH"]
    """Filter by instrument type (e.g., COMMON_STOCK, OPTION)"""

    side: Literal["BUY", "SELL", "SELL_SHORT", "OTHER"]
    """Filter by order side (BUY or SELL)"""

    type: Literal["MARKET", "LIMIT", "STOP", "STOP_LIMIT", "TRAILING_STOP", "TRAILING_STOP_LIMIT", "OTHER"]
    """Filter by order type (e.g., MARKET, LIMIT)"""
