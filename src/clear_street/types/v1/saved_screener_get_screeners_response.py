# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .screener_entry_list import ScreenerEntryList
from ..shared.base_response import BaseResponse

__all__ = ["SavedScreenerGetScreenersResponse"]


class SavedScreenerGetScreenersResponse(BaseResponse):
    data: ScreenerEntryList
