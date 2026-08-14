# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .margin_details_usage import MarginDetailsUsage
from .margin_session_details import MarginSessionDetails
from .margin_top_contributor import MarginTopContributor

__all__ = ["MarginDetails"]


class MarginDetails(BaseModel):
    initial_margin_excess: str
    """The difference between equity and the initial margin requirement."""

    initial_margin_requirement: str
    """The amount of equity required to open new positions."""

    intraday_details: MarginSessionDetails
    """Intraday session margin calculation details."""

    maintenance_margin_excess: str
    """The difference between equity and the maintenance margin requirement."""

    maintenance_margin_requirement: str
    """The amount of equity required to maintain current positions."""

    overnight_details: MarginSessionDetails
    """Overnight session margin calculation details."""

    top_contributors: Optional[List[MarginTopContributor]] = None
    """Optional top margin contributors, returned only when explicitly requested."""

    usage: Optional[MarginDetailsUsage] = None
    """
    Current usage totals. When a null/undefined value is observed, it indicates that
    there is no available data.
    """
