# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ....._models import BaseModel

__all__ = ["StockSplitEvent"]


class StockSplitEvent(BaseModel):
    """Represents a stock split event"""

    date: datetime.date
    """The date the split will occur"""

    denominator: int
    """The pre-split number of shares"""

    numerator: int
    """The post-split number of shares for every 'denominator' pre-split shares"""

    symbol: str
    """The symbol for the instrument"""
