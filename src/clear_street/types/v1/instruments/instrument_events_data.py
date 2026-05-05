# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ..instrument_earnings import InstrumentEarnings
from .instrument_split_event import InstrumentSplitEvent
from .instrument_dividend_event import InstrumentDividendEvent

__all__ = ["InstrumentEventsData"]


class InstrumentEventsData(BaseModel):
    """Grouped instrument events by type"""

    dividends: List[InstrumentDividendEvent]
    """Dividend distribution events"""

    earnings: List[InstrumentEarnings]
    """Earnings announcement events"""

    instrument_id: str
    """OEMS instrument UUID from the request"""

    splits: List[InstrumentSplitEvent]
    """Stock split events"""
