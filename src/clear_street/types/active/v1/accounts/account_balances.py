# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .margin_type import MarginType
from .margin_details import MarginDetails
from .account_balances_sod import AccountBalancesSod

__all__ = ["AccountBalances"]


class AccountBalances(BaseModel):
    """Represents the balance details for a trading account"""

    account_id: int
    """The unique identifier for the account"""

    buying_power: str
    """The total buying power available in the account."""

    currency: str
    """Currency identifier for all monetary values."""

    daily_realized_pnl: str
    """Realized profit or loss since start of day."""

    daily_total_pnl: str
    """Total profit or loss since start of day."""

    daily_unrealized_pnl: str
    """Total unrealized profit or loss across all positions relative to prior close."""

    equity: str
    """The total equity in the account."""

    long_market_value: str
    """The total market value of all long positions."""

    margin_type: MarginType
    """The applicable margin model for the account"""

    open_order_adjustment: str
    """Signed buying-power correction from open orders."""

    settled_cash: str
    """The amount of cash that is settled and available for withdrawal or trading."""

    sod: AccountBalancesSod
    """Start-of-day snapshot balances."""

    trade_cash: str
    """Trade-date effective cash."""

    unsettled_credits: str
    """Trade-date unsettled cash credits."""

    unsettled_debits: str
    """Trade-date unsettled cash debits."""

    margin_details: Optional[MarginDetails] = None
    """Margin-account-only details."""

    multiplier: Optional[str] = None
    """Applied multiplier for margin calculations."""

    short_market_value: Optional[str] = None
    """The total market value of all short positions."""
