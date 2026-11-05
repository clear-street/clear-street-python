# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .prediction_market_summary import PredictionMarketSummary

__all__ = ["PredictionEvent"]


class PredictionEvent(BaseModel):
    """A prediction market event: a set of related markets that resolve together."""

    categories: List[str]
    """Distinct categories of the event's listable markets, sorted alphabetically."""

    code: str
    """Event code."""

    markets: Optional[List[PredictionMarketSummary]] = None
    """Every market of the event in any status, ordered by symbol.

    Present only when `include_markets` is `true`.
    """

    title: Optional[str] = None
    """The question of the event's first listable market, by symbol."""
