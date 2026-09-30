# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .economic_event_list import EconomicEventList
from ..shared.base_response import BaseResponse

__all__ = ["CalendarGetEconomicEventsCalendarResponse"]


class CalendarGetEconomicEventsCalendarResponse(BaseResponse):
    data: EconomicEventList
