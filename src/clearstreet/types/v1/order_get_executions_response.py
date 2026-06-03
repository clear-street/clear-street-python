# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .execution_list import ExecutionList
from ..shared.base_response import BaseResponse

__all__ = ["OrderGetExecutionsResponse"]


class OrderGetExecutionsResponse(BaseResponse):
    data: ExecutionList
