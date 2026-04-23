# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .earnings_calendar_event_list import EarningsCalendarEventList

__all__ = ["EarningGetEarningsCalendarResponse"]


class EarningGetEarningsCalendarResponse(BaseResponse):
    data: EarningsCalendarEventList
