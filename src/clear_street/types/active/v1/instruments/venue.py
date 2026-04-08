# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gtd_accepts import GtdAccepts
from .display_type import DisplayType
from .venue_session import VenueSession

__all__ = ["Venue"]


class Venue(BaseModel):
    """A trading venue with its characteristics and capabilities"""

    country: str
    """The ISO country code where the venue operates"""

    display_type: DisplayType
    """The display characteristics of the venue"""

    gtd_accepts: GtdAccepts
    """
    Indicates whether GOOD_TILL_DATE orders accept date-only or timestamp
    specifications
    """

    lot_size: int
    """The minimum quantity increment for orders at this venue"""

    mic: str
    """The Market Identifier Code (MIC) for the venue"""

    name: str
    """The display name of the venue"""

    sessions: List[VenueSession]
    """Trading sessions available at this venue"""

    supported_order_types: List[str]
    """Order types supported by this venue"""

    supported_tifs: List[str]
    """Time-in-force options supported by this venue"""

    tick_size: str
    """The minimum price increment for orders at this venue"""

    timezone: str
    """IANA timezone identifier for the venue's local time"""
