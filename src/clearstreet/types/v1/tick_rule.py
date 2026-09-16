# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TickRule"]


class TickRule(BaseModel):
    """One band of an instrument's tick schedule.

    A price in the band is valid only
    if it is a whole multiple of `tick_size`. Bands describe the instrument
    itself: on an equity they say nothing about that equity's option chain.
    """

    start_price: str
    """Lowest price in the band, inclusive."""

    tick_size: str
    """Minimum price increment within the band."""

    end_price: Optional[str] = None
    """Upper bound of the band, exclusive.

    Absent on the last band, which runs to infinity. When a null/undefined value is
    observed, it indicates it does not apply.
    """
