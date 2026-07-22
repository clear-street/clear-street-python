# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["WatchlistAddWatchlistItemParams"]


class WatchlistAddWatchlistItemParams(TypedDict, total=False):
    instrument_id: Required[InstrumentIDOrSymbol]
    """Instrument identifier"""
