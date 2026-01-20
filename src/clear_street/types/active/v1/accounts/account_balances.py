# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .margin_type import MarginType
from .api_timestamp import APITimestamp
from .reg_t_balance import RegTBalance

__all__ = ["AccountBalances"]


class AccountBalances(BaseModel):
    """Represents the balance details for a trading account"""

    account_id: int
    """The unique identifier for the account"""

    balance: RegTBalance
    """The Reg T balance for the account"""

    daily_realized_pnl: str
    """Realized profit or loss since start of day."""

    daily_total_pnl: str
    """Total profit or loss since start of day."""

    daily_unrealized_pnl: str
    """Total unrealized profit or loss across all positions relative to prior close."""

    margin_type: MarginType
    """The applicable margin model for the account"""

    sod_asof: Optional[APITimestamp] = None
    """Timestamp for the start-of-day values"""
