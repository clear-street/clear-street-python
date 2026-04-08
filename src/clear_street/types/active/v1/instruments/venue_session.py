# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["VenueSession"]


class VenueSession(BaseModel):
    """A trading session within a venue's trading day"""

    end_local: str
    """Session end time in venue's local timezone (HH:MM format, 24-hour)"""

    name: str
    """The name of the trading session"""

    start_local: str
    """Session start time in venue's local timezone (HH:MM format, 24-hour)"""
