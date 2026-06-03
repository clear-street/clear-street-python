# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .version import Version
from ..shared.base_response import BaseResponse

__all__ = ["APIVersionGetVersionResponse"]


class APIVersionGetVersionResponse(BaseResponse):
    data: Version
    """API version information"""
