# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .market_hours_list import MarketHoursList
from ....shared.base_response import BaseResponse

__all__ = ["MarketHourGetMarketHoursCalendarResponse"]


class MarketHourGetMarketHoursCalendarResponse(BaseResponse):
    data: MarketHoursList
