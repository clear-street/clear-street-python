# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ..._models import BaseModel

__all__ = ["InstrumentSplitEvent"]


class InstrumentSplitEvent(BaseModel):
    """Represents a stock split event for an instrument"""

    date: datetime.date
    """The date of the stock split"""

    denominator: str
    """The denominator of the split ratio"""

    numerator: str
    """The numerator of the split ratio"""

    split_type: str
    """The type of stock split (e.g., "stock-split", "stock-dividend", "bonus-issue")"""
