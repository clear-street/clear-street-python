# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from ...security_id_source import SecurityIDSource
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

    security_id: str
    """The security ID from the request"""

    security_id_source: SecurityIDSource
    """The security ID source from the request"""

    splits: List[InstrumentSplitEvent]
    """Stock split events"""
