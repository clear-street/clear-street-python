# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .instrument_events_data import InstrumentEventsData

__all__ = ["InstrumentDataGetInstrumentEventsResponse"]


class InstrumentDataGetInstrumentEventsResponse(BaseResponse):
    data: InstrumentEventsData
    """Grouped instrument events by type"""
