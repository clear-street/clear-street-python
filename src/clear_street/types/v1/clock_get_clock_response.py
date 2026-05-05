# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .clock_detail import ClockDetail
from ..shared.base_response import BaseResponse

__all__ = ["ClockGetClockResponse"]


class ClockGetClockResponse(BaseResponse):
    data: ClockDetail
    """Current server time and market clock information"""
