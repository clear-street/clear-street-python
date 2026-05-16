# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SessionSchedule"]


class SessionSchedule(BaseModel):
    """Session schedule with open and close timestamps"""

    close: datetime
    """Session close timestamp with timezone offset"""

    open: datetime
    """Session open timestamp with timezone offset"""

    time_until_close: Optional[str] = None
    """ISO 8601 duration until session closes. Null if session is not currently open."""

    time_until_open: Optional[str] = None
    """ISO 8601 duration until session opens.

    Null if session has already started or closed.
    """
