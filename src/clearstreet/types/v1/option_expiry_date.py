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
    Whether this date has at least one contract that settles on the opening print
    (AM settlement) and can still be traded. AM-settled contracts stop trading at
    the close of the business day before settlement, so this turns false before the
    expiration date arrives. A date leaves the list once no contract on it can be
    traded in either settlement cycle.
    """
