# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locate_list import LocateList
from ..shared.base_response import BaseResponse

__all__ = ["LocateGetLocatesResponse"]


class LocateGetLocatesResponse(BaseResponse):
    data: LocateList
