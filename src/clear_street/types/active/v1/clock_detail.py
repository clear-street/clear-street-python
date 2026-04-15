# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ClockDetail"]


class ClockDetail(BaseModel):
    """Current server time and market clock information"""

    clock: datetime
    """Current server time in UTC"""
