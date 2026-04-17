# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..cancel_run_response import CancelRunResponse
from ....shared.base_response import BaseResponse

__all__ = ["RunCancelRunResponse"]


class RunCancelRunResponse(BaseResponse):
    data: CancelRunResponse
