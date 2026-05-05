# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .instrument_all_events_data import InstrumentAllEventsData

__all__ = ["EventGetAllInstrumentEventsResponse"]


class EventGetAllInstrumentEventsResponse(BaseResponse):
    data: InstrumentAllEventsData
    """All-events payload grouped by date."""
