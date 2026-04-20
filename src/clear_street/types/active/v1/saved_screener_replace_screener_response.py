# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .screener_entry import ScreenerEntry
from ...shared.base_response import BaseResponse

__all__ = ["SavedScreenerReplaceScreenerResponse"]


class SavedScreenerReplaceScreenerResponse(BaseResponse):
    data: ScreenerEntry
    """A saved screener configuration entry"""
