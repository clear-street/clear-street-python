# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .prediction_market_status import PredictionMarketStatus
from .prediction_market_outcome import PredictionMarketOutcome

__all__ = ["PredictionMarket"]


class PredictionMarket(BaseModel):
    """A prediction market."""

    id: str
    """Instrument id of the market."""

    can_close_early: bool
    """Whether the market may close before `close_at`."""

    categories: List[str]
    """Categories of the market."""

    event_code: str
    """Code of the event the market belongs to."""

    is_liquidation_only: bool
    """Whether only orders that reduce a position are accepted."""

    is_tradable: bool
    """Whether the market accepts orders now."""

    restrictions: List[str]
    """Trading restrictions of the market."""

    series_code: str
    """Code of the series the market belongs to."""

    status: PredictionMarketStatus
    """Current status of the market."""

    symbol: str
    """Market ticker."""

    close_at: Optional[datetime] = None
    """When trading is scheduled to close."""

    contract_terms_url: Optional[str] = None
    """Link to the contract terms document."""

    early_close_condition: Optional[str] = None
    """Condition under which the market closes early."""

    expected_settlement_at: Optional[datetime] = None
    """When settlement is expected after the market closes."""

    full_title: Optional[str] = None
    """Full title of the market, event and market together."""

    open_at: Optional[datetime] = None
    """When trading opens."""

    outcome: Optional[PredictionMarketOutcome] = None
    """Winning side.

    Set only when `status` is `SETTLED` and the market resolved `YES` or `NO`.
    Absent otherwise, including for voided and scalar markets.
    """

    predicate: Optional[str] = None
    """The question the market resolves."""

    rules_primary: Optional[str] = None
    """Primary rules of the market."""

    rules_secondary: Optional[str] = None
    """Secondary rules of the market."""

    settlement_price: Optional[str] = None
    """Settlement value of the YES side, in dollars per contract.

    Set only when `status` is `SETTLED`, and absent otherwise.
    """

    title: Optional[str] = None
    """Short title of the market, for example the name of the candidate."""
