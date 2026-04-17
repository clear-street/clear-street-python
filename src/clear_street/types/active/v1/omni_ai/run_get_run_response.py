# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..get_run_response import GetRunResponse
from ....shared.base_response import BaseResponse

__all__ = ["RunGetRunResponse"]


class RunGetRunResponse(BaseResponse):
    data: GetRunResponse
