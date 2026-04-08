# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ....._types import SequenceNotStr
from .all_events_event_type import AllEventsEventType

__all__ = ["EventGetAllInstrumentEventsParams"]


class EventGetAllInstrumentEventsParams(TypedDict, total=False):
    event_types: List[AllEventsEventType]
    """Filter by event type(s).

    Comma-delimited list. Example: `event_types=EARNINGS,IPO`.
    """

    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    instrument_ids: SequenceNotStr[str]
    """Filter by OEMS instrument ID(s).

    Comma-delimited list of UUIDs. Example:
    `instrument_ids=550e8400-e29b-41d4-a716-446655440000`.
    """

    security_id: SequenceNotStr[str]
    """Filter by security ID(s). Accepts single value or indexed array.

    Examples:

    - Single: `security_id=037833100`
    - Multiple: `security_id[0]=037833100&security_id[1]=594918104`
    """

    security_id_source: SequenceNotStr[str]
    """Source(s) for the security ID filter.

    Must match the count and order of security_id.

    Examples:

    - Single: `security_id_source=CUSIP`
    - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`
    """

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""
