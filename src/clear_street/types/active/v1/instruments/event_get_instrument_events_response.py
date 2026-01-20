# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument_event_list import InstrumentEventList
from ....shared.base_response import BaseResponse

__all__ = ["EventGetInstrumentEventsResponse"]


class EventGetInstrumentEventsResponse(BaseResponse):
    data: InstrumentEventList
