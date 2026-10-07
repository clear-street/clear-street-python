# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LocateRate"]


class LocateRate(BaseModel):
    """A locate borrow rate for an instrument."""

    instrument_id: str
    """Instrument id the rate applies to."""

    rate: str
    """Borrow rate, expressed as a decimal (e.g. 0.037012 for 3.7012%)."""

    as_of: Optional[datetime] = None
    """When the rate was requested from the locates venue."""
