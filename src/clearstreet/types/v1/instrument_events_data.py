# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .instrument_earnings import InstrumentEarnings
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
    """Instrument identifier"""

    splits: List[InstrumentSplitEvent]
    """Stock split events"""

    reporting_currency: Optional[str] = None
    """
    The currency used for reporting financial data When a null/undefined value is
    observed, it indicates that there is no available data.
    """
