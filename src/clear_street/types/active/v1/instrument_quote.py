# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InstrumentQuote"]


class InstrumentQuote(BaseModel):
    """Real-time market quote data for a specific instrument"""

    high: str
    """The highest trade price during the current trading day"""

    last_price: str
    """The most recent trade price"""

    low: str
    """The lowest trade price during the current trading day"""

    open: str
    """The opening price for the current trading day"""

    volume: int
    """The total number of shares traded during the current trading day"""
