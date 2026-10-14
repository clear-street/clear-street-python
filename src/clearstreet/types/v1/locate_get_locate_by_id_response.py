# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locate import Locate
from ..shared.base_response import BaseResponse

__all__ = ["LocateGetLocateByIDResponse"]


class LocateGetLocateByIDResponse(BaseResponse):
    data: Locate
    """A locate request joined with the locate granted for it, if any."""
