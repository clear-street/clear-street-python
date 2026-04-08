# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .market_hours_detail_list import MarketHoursDetailList

__all__ = ["MarketHourGetMarketHoursCalendarResponse"]


class MarketHourGetMarketHoursCalendarResponse(BaseResponse):
    data: MarketHoursDetailList
