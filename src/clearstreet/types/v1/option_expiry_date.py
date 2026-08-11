# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ..._models import BaseModel

__all__ = ["OptionExpiryDate"]


class OptionExpiryDate(BaseModel):
    """
    An options expiry date, annotated with which settlement cycles have
    listed contracts on it.
    """

    date: datetime.date
    """The expiration date."""

    has_settles_on_close: bool
    """
    Whether this date has at least one listed contract that settles at the close (PM
    settlement) -- the standard cycle.
    """

    has_settles_on_open: bool
    """
    Whether this date has at least one listed contract that settles on the opening
    print (AM settlement).
    """
