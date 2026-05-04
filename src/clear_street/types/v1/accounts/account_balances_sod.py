# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["AccountBalancesSod"]


class AccountBalancesSod(BaseModel):
    buying_power: str
    """Start-of-day buying power."""

    equity: str
    """Start-of-day equity."""

    long_market_value: str
    """Start-of-day long market value."""

    short_market_value: str
    """Start-of-day short market value."""

    asof: Optional[date] = None
    """Timestamp for the start-of-day values."""

    day_trade_buying_power: Optional[str] = None
    """Start-of-day day-trade buying power."""

    maintenance_margin_excess: Optional[str] = None
    """Start-of-day maintenance margin excess."""

    maintenance_margin_requirement: Optional[str] = None
    """Start-of-day maintenance margin requirement."""

    trade_cash: Optional[str] = None
    """Start-of-day trade cash."""
