# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["GtdAccepts"]


class GtdAccepts(BaseModel):
    """Good-till-date order acceptance capabilities"""

    date: bool
    """Whether the venue accepts date-only expiration (YYYY-MM-DD)"""

    timestamp: bool
    """Whether the venue accepts precise timestamp expiration"""
