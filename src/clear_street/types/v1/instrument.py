# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .instrument_core import InstrumentCore

__all__ = ["Instrument"]


class Instrument(InstrumentCore):
    """Represents a tradable financial instrument."""

    options_expiry_dates: Optional[List[date]] = None
    """
    Available options expiration dates for this instrument. Present only when
    `include_options_expiry_dates=true` in the request.
    """
