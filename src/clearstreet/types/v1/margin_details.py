# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .margin_details_usage import MarginDetailsUsage
from .margin_session_details import MarginSessionDetails
from .margin_top_contributor import MarginTopContributor

__all__ = ["MarginDetails"]


class MarginDetails(BaseModel):
    day_trade_count: int
    """The number of day trades executed over the 5 most recent trading days."""

    initial_margin_excess: str
    """Initial margin excess for trade-date balances."""

    initial_margin_requirement: str
    """Initial margin requirement for trade-date balances."""

    intraday_details: MarginSessionDetails
    """Intraday session margin calculation details."""

    maintenance_margin_excess: str
    """Maintenance margin excess for trade-date balances."""

    maintenance_margin_requirement: str
    """Maintenance margin requirement for trade-date balances."""

    overnight_details: MarginSessionDetails
    """Overnight session margin calculation details."""

    pattern_day_trader: bool
    """`true` if the account is currently flagged as a PDT, otherwise `false`."""

    day_trade_buying_power_usage: Optional[str] = None
    """The amount of day-trade buying power used during the current trading day."""

    top_contributors: Optional[List[MarginTopContributor]] = None
    """Optional top margin contributors, returned only when explicitly requested."""

    usage: Optional[MarginDetailsUsage] = None
    """Current usage totals."""
