# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .all_events_event_type import AllEventsEventType

__all__ = ["InstrumentDataGetInstrumentEventsParams"]


class InstrumentDataGetInstrumentEventsParams(TypedDict, total=False):
    event_types: List[AllEventsEventType]
    """Filter by event type(s).

    Comma-delimited list. Example: `event_types=EARNINGS,IPO`.
    """

    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""
