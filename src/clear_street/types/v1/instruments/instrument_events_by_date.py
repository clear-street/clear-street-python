# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List

from ...._models import BaseModel
from .instrument_event_envelope import InstrumentEventEnvelope

__all__ = ["InstrumentEventsByDate"]


class InstrumentEventsByDate(BaseModel):
    """Instrument events for a single date."""

    date: datetime.date
    """Event date."""

    events: List[InstrumentEventEnvelope]
    """Flat event envelopes for this date."""
