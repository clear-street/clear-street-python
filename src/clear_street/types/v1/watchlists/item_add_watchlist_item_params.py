# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..accounts.instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["ItemAddWatchlistItemParams"]


class ItemAddWatchlistItemParams(TypedDict, total=False):
    instrument_id: Required[InstrumentIDOrSymbol]
    """OEMS instrument UUID"""
