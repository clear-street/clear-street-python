# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["InstrumentEventIpoItem"]


class InstrumentEventIpoItem(BaseModel):
    """IPO event in the all-events date grouping response."""

    actions: Optional[str] = None
    """IPO action."""

    announced_at: Optional[datetime] = None
    """IPO announced timestamp."""

    company: Optional[str] = None
    """IPO company name."""

    exchange: Optional[str] = None
    """IPO exchange."""

    market_cap: Optional[str] = None
    """IPO market cap."""

    price_range: Optional[str] = None
    """IPO price range."""

    shares: Optional[str] = None
    """IPO shares offered."""
