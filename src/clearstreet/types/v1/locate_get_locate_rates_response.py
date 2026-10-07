# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .locate_rate_result_list import LocateRateResultList

__all__ = ["LocateGetLocateRatesResponse"]


class LocateGetLocateRatesResponse(BaseResponse):
    data: LocateRateResultList
