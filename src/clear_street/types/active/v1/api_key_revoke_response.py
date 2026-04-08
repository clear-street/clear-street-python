# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .revocation import Revocation
from ...shared.base_response import BaseResponse

__all__ = ["APIKeyRevokeResponse"]


class APIKeyRevokeResponse(BaseResponse):
    data: Revocation
