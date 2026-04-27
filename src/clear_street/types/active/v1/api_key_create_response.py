# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .api_key import APIKey
from ...shared.base_response import BaseResponse

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseResponse):
    data: APIKey
