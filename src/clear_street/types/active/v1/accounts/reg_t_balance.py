# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["RegTBalance"]


class RegTBalance(BaseModel):
    """The Reg T balance for the account"""

    buying_power: str
    """The total buying power available in the account"""

    currency: str
    """Currency identifier for all monetary values"""

    daytrading_buying_power: str
    """Day-trading buying power."""

    equity: str
    """The total equity in the account (market value of all assets minus liabilities)"""

    long_market_value: str
    """The total market value of all long positions"""

    maintenance_margin: str
    """Margin requirement for trade-date balances."""

    margin_excess: str
    """Margin excess for trade-date balances."""

    multiplier: str
    """Applied multiplier for margin calculations."""

    regt_buying_power: str
    """Regulation T buying power."""

    settled_cash: str
    """The amount of cash that is settled and available for withdrawal or trading"""

    short_market_value: str
    """The total market value of all short positions (represented as a positive value)"""

    sod_cash: str
    """Start-of-day cash balance."""

    sod_daytrading_buying_power: str
    """Start-of-day day-trading buying power."""

    sod_equity: str
    """Start-of-day equity based on cash and positions."""

    sod_long_market_value: str
    """Start-of-day long position market value (ex-cash)."""

    sod_margin_excess: str
    """Start-of-day margin excess."""

    sod_margin_requirement: str
    """Start-of-day margin requirement."""

    sod_reg_t_buying_power: str
    """Start-of-day Regulation T buying power."""

    sod_short_market_value: str
    """Start-of-day short position market value (ex-cash)."""

    trade_cash: str
    """Aggregated cash value."""

    unsettled_cash_credits: str
    """Trade-date unsettled cash credits."""

    unsettled_cash_debits: str
    """Trade-date unsettled cash debits."""
