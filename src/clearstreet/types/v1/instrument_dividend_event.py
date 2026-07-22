# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["InstrumentDividendEvent"]


class InstrumentDividendEvent(BaseModel):
    """Represents a dividend event for an instrument"""

    adjusted_dividend_amount: str
    """The adjusted dividend amount accounting for any splits."""

    ex_date: date
    """The day the stock starts trading without the right to receive that dividend."""

    declaration_date: Optional[date] = None
    """
    The declaration date of the dividend When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    dividend_amount: Optional[str] = None
    """
    The dividend amount per share. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    dividend_yield: Optional[str] = None
    """
    The dividend yield as a percentage of the stock price. When a null/undefined
    value is observed, it indicates that there is no available data.
    """

    frequency: Optional[str] = None
    """
    The frequency of the dividend payments (e.g., "Quarterly", "Annual"). When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    payment_date: Optional[date] = None
    """
    The payment date is the date on which a declared stock dividend is scheduled to
    be paid. When a null/undefined value is observed, it indicates that there is no
    available data.
    """

    record_date: Optional[date] = None
    """
    The record date, set by a company's board of directors, is when a company
    compiles a list of shareholders of the stock for which it has declared a
    dividend. When a null/undefined value is observed, it indicates that there is no
    available data.
    """
