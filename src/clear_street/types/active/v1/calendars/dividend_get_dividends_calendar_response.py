# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .dividend_calendar_event_list import DividendCalendarEventList

__all__ = ["DividendGetDividendsCalendarResponse"]


class DividendGetDividendsCalendarResponse(BaseResponse):
    data: DividendCalendarEventList
