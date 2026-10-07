# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["LocateGetLocateRatesParams"]


class LocateGetLocateRatesParams(TypedDict, total=False):
    instrument_ids: Required[SequenceNotStr[InstrumentIDOrSymbol]]
    """Comma-separated instrument IDs (UUID) or symbols; at least one, at most 1,000."""
