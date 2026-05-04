# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from ..cancel_response_payload import CancelResponsePayload

__all__ = ["ResponseCancelResponseResponse"]


class ResponseCancelResponseResponse(BaseResponse):
    data: CancelResponsePayload
