# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .prediction_market_status import PredictionMarketStatus
from .prediction_market_outcome import PredictionMarketOutcome

__all__ = ["PredictionMarketSummary"]


class PredictionMarketSummary(BaseModel):
    """Summary of a prediction market inside an event listing.

    Request the market
    by `id` or `symbol` for its full detail.
    """

    id: str
    """Instrument id of the market."""

    is_liquidation_only: bool
    """Whether only orders that reduce a position are accepted."""

    is_tradable: bool
    """Whether the market accepts orders now."""

    status: PredictionMarketStatus
    """Current status of the market."""

    symbol: str
    """Market ticker."""

    close_at: Optional[datetime] = None
    """When trading is scheduled to close."""

    open_at: Optional[datetime] = None
    """When trading opens."""

    outcome: Optional[PredictionMarketOutcome] = None
    """Winning side.

    Set only when `status` is `SETTLED` and the market resolved `YES` or `NO`.
    Absent otherwise, including for voided and scalar markets.
    """

    settlement_price: Optional[str] = None
    """Settlement value of the YES side, in dollars per contract.

    Set only when `status` is `SETTLED`, and absent otherwise.
    """

    title: Optional[str] = None
    """Short title of the market, for example the name of the candidate."""
