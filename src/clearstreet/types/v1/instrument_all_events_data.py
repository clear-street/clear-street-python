# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .instrument_events_by_date import InstrumentEventsByDate

__all__ = ["InstrumentAllEventsData"]


class InstrumentAllEventsData(BaseModel):
    """All-events payload grouped by date."""

    event_dates: List[InstrumentEventsByDate]
    """Events grouped by date in descending order."""
