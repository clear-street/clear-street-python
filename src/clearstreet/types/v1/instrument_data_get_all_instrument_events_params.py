# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo
from .all_events_event_type import AllEventsEventType
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["InstrumentDataGetAllInstrumentEventsParams"]


class InstrumentDataGetAllInstrumentEventsParams(TypedDict, total=False):
    event_types: List[AllEventsEventType]
    """Filter by event type(s).

    Comma-delimited list. Example: `event_types=EARNINGS,IPO`.
    """

    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    instrument_ids: SequenceNotStr[InstrumentIDOrSymbol]
    """Filter by instrument.

    Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
    symbols). Example: `instrument_ids=550e8400-e29b-41d4-a716-446655440000,AAPL`.
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""
