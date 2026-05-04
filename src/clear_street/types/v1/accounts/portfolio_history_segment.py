# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ...._models import BaseModel

__all__ = ["PortfolioHistorySegment"]


class PortfolioHistorySegment(BaseModel):
    date: datetime.date
    """The date for this segment"""

    eod_equity: str
    """The equity at the end of the trading day."""

    realized_pnl: str
    """Sum of the profit and loss realized from position closing trading activity."""

    sod_equity: str
    """The equity at the start of the trading day."""

    unrealized_pnl: str
    """Sum of the profit and loss from market changes."""

    bought_notional: Optional[str] = None
    """Amount bought MTM"""

    day_pnl: Optional[str] = None
    """
    Sum of the profit and loss from intraday trading activities for the trading day.
    """

    net_pnl: Optional[str] = None
    """
    P&L after netting all realized and unrealized P&L, adjustments, dividends,
    change in accruals, income and expenses
    """

    position_pnl: Optional[str] = None
    """
    P&L attributable to start-of-day (carried) positions from market movement during
    this trading day.
    """

    sold_notional: Optional[str] = None
    """Amount sold MTM"""
