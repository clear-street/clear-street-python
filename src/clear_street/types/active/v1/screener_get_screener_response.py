# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .screener_item_list import ScreenerItemList
from ...shared.base_response import BaseResponse

__all__ = ["ScreenerGetScreenerResponse"]


class ScreenerGetScreenerResponse(BaseResponse):
    data: ScreenerItemList
