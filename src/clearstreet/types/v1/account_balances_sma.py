# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["AccountBalancesSma"]


class AccountBalancesSma(BaseModel):
    """The intraday special memorandum account (SMA) of an account holder.

    The SMA belongs to the account holder, not to one account. The API returns it
    only when the account holder has a single open account.
    """

    asof: datetime
    """The time the SMA was calculated as of (UTC).

    During a trade date the API returns the last published value, so use this time
    to judge how current the value is.
    """

    value: str
    """The SMA amount in the account currency. The value can be negative."""
