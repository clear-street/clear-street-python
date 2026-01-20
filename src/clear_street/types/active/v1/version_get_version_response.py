# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .version import Version
from ...shared.base_response import BaseResponse

__all__ = ["VersionGetVersionResponse"]


class VersionGetVersionResponse(BaseResponse):
    data: Version
    """API version information"""
