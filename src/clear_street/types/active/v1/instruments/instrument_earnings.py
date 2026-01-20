# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ....._models import BaseModel
from .fiscal_period_type import FiscalPeriodType

__all__ = ["InstrumentEarnings"]


class InstrumentEarnings(BaseModel):
    """Represents instrument earnings data"""

    date: datetime.date
    """The date when the earnings report was published"""

    period: int
    """The fiscal period (e.g., quarter) within the year"""

    period_type: FiscalPeriodType
    """The type of fiscal period"""

    year: int
    """The fiscal year of the earnings period"""

    eps_actual: Optional[str] = None
    """The actual earnings per share (EPS) for the period"""

    eps_estimate: Optional[str] = None
    """The estimated earnings per share (EPS) for the period"""

    eps_surprise_percent: Optional[str] = None
    """The percentage difference between actual and estimated EPS"""

    revenue_actual: Optional[int] = None
    """The actual total revenue for the period"""

    revenue_estimate: Optional[int] = None
    """The estimated total revenue for the period"""

    revenue_surprise_percent: Optional[str] = None
    """The percentage difference between actual and estimated revenue"""
