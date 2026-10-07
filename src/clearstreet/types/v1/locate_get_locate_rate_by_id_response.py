# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locate_rate import LocateRate
from ..shared.base_response import BaseResponse

__all__ = ["LocateGetLocateRateByIDResponse"]


class LocateGetLocateRateByIDResponse(BaseResponse):
    data: LocateRate
    """A locate borrow rate for an instrument."""
