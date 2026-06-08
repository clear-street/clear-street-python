# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .instrument_earnings import InstrumentEarnings
from .all_events_event_type import AllEventsEventType
from .instrument_split_event import InstrumentSplitEvent
from .instrument_dividend_event import InstrumentDividendEvent
from .instrument_event_ipo_item import InstrumentEventIpoItem

__all__ = ["InstrumentEventEnvelope"]


class InstrumentEventEnvelope(BaseModel):
    """Unified envelope for the all-events response."""

    symbol: str
    """Symbol associated with the event."""

    type: AllEventsEventType
    """Event type discriminator."""

    dividend_event_data: Optional[InstrumentDividendEvent] = None
    """Dividend payload when type is DIVIDEND."""

    earnings_event_data: Optional[InstrumentEarnings] = None
    """Earnings payload when type is EARNINGS."""

    instrument_id: Optional[str] = None
    """Instrument identifier, when available."""

    ipo_event_data: Optional[InstrumentEventIpoItem] = None
    """IPO payload when type is IPO."""

    name: Optional[str] = None
    """Instrument name associated with the event, when available."""

    reporting_currency: Optional[str] = None
    """The currency used for reporting financial data."""

    stock_split_event_data: Optional[InstrumentSplitEvent] = None
    """Stock split payload when type is STOCK_SPLIT."""
