# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["InstrumentEvent"]


class InstrumentEvent(BaseModel):
    """Represents an instrument event (dividends, splits, etc.)"""

    date: datetime.date
    """The date of the event"""

    description: str
    """A brief description of the event"""

    event_type: Literal["EARNINGS", "DIVIDEND", "SPLIT", "MERGER_ACQUISITION"]
    """The type of event"""
