# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .margin_type import MarginType
from .margin_details import MarginDetails
from .margin_session import MarginSession
from .account_balances_sma import AccountBalancesSma
from .account_balances_sod import AccountBalancesSod
from .prediction_market_balances import PredictionMarketBalances

__all__ = ["AccountBalances"]


class AccountBalances(BaseModel):
    """Represents the balance details for a trading account"""

    account_id: int
    """The unique identifier for the account"""

    buying_power: str
    """
    The total buying power available in the account: base buying power plus the open
    order adjustment, where base buying power is maintenance margin excess times the
    multiplier for intraday and overnight margin excess times the multiplier for
    overnight.
    """

    currency: str
    """Currency identifier for all monetary values."""

    current_session: MarginSession
    """
    The session whose values the engine is applying to these balances.
    `buying_power`, `multiplier`, and `margin_details.usage` reflect this session. A
    closed market reports `overnight`.
    """

    daily_change: str
    """Difference between current equity and start-of-day equity."""

    daily_pnl: str
    """Total profit or loss since start of day."""

    daily_realized_pnl: str
    """Realized profit or loss since start of day."""

    daily_unrealized_pnl: str
    """Total unrealized profit or loss across all positions relative to prior close."""

    equity: str
    """
    The total equity in the account: cash plus long market value plus short market
    value, where short market value is negative.
    """

    long_market_value: str
    """The total market value of all long positions."""

    margin_type: MarginType
    """The applicable margin model for the account"""

    open_order_adjustment: str
    """
    Buying power correction from open orders, computed as projected buying power
    minus actual buying power. A negative value means open orders are consuming
    buying power.
    """

    settled_cash: str
    """The amount of cash that is settled and available for withdrawal or trading."""

    sod: AccountBalancesSod
    """Start-of-day snapshot balances."""

    trade_cash: str
    """Trade-date effective cash."""

    unrealized_pnl: str
    """Total unrealized profit or loss across all open positions."""

    unsettled_credits: str
    """Trade-date unsettled cash credits."""

    unsettled_debits: str
    """Trade-date unsettled cash debits."""

    withdrawable_cash: str
    """The amount of cash currently available to withdraw."""

    margin_details: Optional[MarginDetails] = None
    """
    Margin-account-only details. When a null/undefined value is observed, it
    indicates it does not apply.
    """

    multiplier: Optional[str] = None
    """
    Margin multiplier: 4 during intraday sessions (pre-market, regular, and
    after-hours) and 2 during the overnight session. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    prediction_market: Optional[PredictionMarketBalances] = None
    """Prediction-market buying power in the same currency as the account balances."""

    short_market_value: Optional[str] = None
    """
    The total market value of all short positions. When null/undefined, the value
    should be assumed to be zero. The field is omitted to simplify the response.
    """

    sma: Optional[AccountBalancesSma] = None
    """
    The intraday special memorandum account (SMA) of the account holder. Omitted
    when no SMA is available for the current trade date, or when the account holder
    has more than one open account. When a null/undefined value is observed, it
    indicates that there is no available data.
    """
