# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .revocation_list import RevocationList
from ...shared.base_response import BaseResponse

__all__ = ["APIKeyRevokeAllResponse"]


class APIKeyRevokeAllResponse(BaseResponse):
    data: RevocationList
