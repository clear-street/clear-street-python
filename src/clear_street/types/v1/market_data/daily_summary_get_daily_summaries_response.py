# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .daily_summary_list import DailySummaryList
from ...shared.base_response import BaseResponse

__all__ = ["DailySummaryGetDailySummariesResponse"]


class DailySummaryGetDailySummariesResponse(BaseResponse):
    data: DailySummaryList
