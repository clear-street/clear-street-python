# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .screener_row_list import ScreenerRowList
from ...shared.base_response import BaseResponse

__all__ = ["ScreenerSearchScreenerResponse"]


class ScreenerSearchScreenerResponse(BaseResponse):
    data: ScreenerRowList
