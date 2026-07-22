# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstrumentDataGetInstrumentEventsParams"]


class InstrumentDataGetInstrumentEventsParams(TypedDict, total=False):
    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""
