# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .calendar_date_summary_list import CalendarDateSummaryList

__all__ = ["SummaryGetCalendarSummaryResponse"]


class SummaryGetCalendarSummaryResponse(BaseResponse):
    data: CalendarDateSummaryList
