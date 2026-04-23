# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .economic_calendar_event_list import EconomicCalendarEventList

__all__ = ["EconomicGetEconomicCalendarResponse"]


class EconomicGetEconomicCalendarResponse(BaseResponse):
    data: EconomicCalendarEventList
