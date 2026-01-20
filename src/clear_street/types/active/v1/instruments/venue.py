# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Venue", "GtdAccepts", "Session"]


class GtdAccepts(BaseModel):
    """
    Indicates whether GOOD_TILL_DATE orders accept date-only or timestamp specifications
    """

    date: bool
    """Whether the venue accepts date-only expiration (YYYY-MM-DD)"""

    timestamp: bool
    """Whether the venue accepts precise timestamp expiration"""


class Session(BaseModel):
    """A trading session within a venue's trading day"""

    end_local: str
    """Session end time in venue's local timezone (HH:MM format, 24-hour)"""

    name: str
    """The name of the trading session"""

    start_local: str
    """Session start time in venue's local timezone (HH:MM format, 24-hour)"""


class Venue(BaseModel):
    """A trading venue with its characteristics and capabilities"""

    country: str
    """The ISO country code where the venue operates"""

    display_type: Literal["LIT", "DARK", "PERIODIC_AUCTION", "RFQ"]
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

    sessions: List[Session]
    """Trading sessions available at this venue"""

    supported_order_types: List[str]
    """Order types supported by this venue"""

    supported_tifs: List[str]
    """Time-in-force options supported by this venue"""

    tick_size: str
    """The minimum price increment for orders at this venue"""

    timezone: str
    """IANA timezone identifier for the venue's local time"""
