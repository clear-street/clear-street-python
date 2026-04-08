# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument_events_data import InstrumentEventsData
from ....shared.base_response import BaseResponse

__all__ = ["EventGetInstrumentEventsResponse"]


class EventGetInstrumentEventsResponse(BaseResponse):
    data: InstrumentEventsData
    """Grouped instrument events by type"""
