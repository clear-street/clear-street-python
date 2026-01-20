# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Version"]


class Version(BaseModel):
    """API version information"""

    version: str
    """API version string"""
