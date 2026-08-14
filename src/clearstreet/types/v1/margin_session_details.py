# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MarginSessionDetails"]


class MarginSessionDetails(BaseModel):
    buying_power: str
    """
    Maximum buying power available in the account during the session: base buying
    power plus the open order adjustment, where base buying power is maintenance
    margin excess times the multiplier for intraday and initial margin excess times
    the multiplier for overnight.
    """

    multiplier: Optional[str] = None
    """
    Margin multiplier for the session: 4 during intraday sessions (pre-market,
    regular, and after-hours) and 2 during the overnight session.
    """
