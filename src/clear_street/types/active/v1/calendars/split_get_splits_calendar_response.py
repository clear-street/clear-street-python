# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .stock_split_event_list import StockSplitEventList
from ....shared.base_response import BaseResponse

__all__ = ["SplitGetSplitsCalendarResponse"]


class SplitGetSplitsCalendarResponse(BaseResponse):
    data: StockSplitEventList
