# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr
from ..instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["MarketDataGetSnapshotsParams"]


class MarketDataGetSnapshotsParams(TypedDict, total=False):
    instrument_ids: SequenceNotStr[InstrumentIDOrSymbol]
    """
    Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
    symbols).
    """
