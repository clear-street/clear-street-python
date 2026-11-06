# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .non_trade_activity_list import NonTradeActivityList

__all__ = ["AccountGetNonTradeActivitiesResponse"]


class AccountGetNonTradeActivitiesResponse(BaseResponse):
    data: NonTradeActivityList
