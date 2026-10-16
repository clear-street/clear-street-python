# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ..._models import BaseModel
from .fiscal_quarter import FiscalQuarter
from .fiscal_period_type import FiscalPeriodType

__all__ = ["InstrumentEarningsTranscript"]


class InstrumentEarningsTranscript(BaseModel):
    """An earnings call transcript for one fiscal quarter."""

    content: str
    """The full text of the transcript"""

    date: datetime.date
    """The date of the earnings call"""

    period: FiscalQuarter
    """The fiscal quarter of the call"""

    period_type: FiscalPeriodType
    """The type of fiscal period. Always `QUARTERLY`."""

    year: int
    """The fiscal year of the call"""
