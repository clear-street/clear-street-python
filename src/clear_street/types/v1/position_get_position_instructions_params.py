# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["PositionGetPositionInstructionsParams"]


class PositionGetPositionInstructionsParams(TypedDict, total=False):
    instrument_id: InstrumentIDOrSymbol
    """Filter by OEMS instrument id or symbol (CMS / OSI)."""
