# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .currency import Currency
from ...._models import BaseModel
from .spv_status import SpvStatus
from .valuation_basis import ValuationBasis
from .spv_fee_term_resource import SpvFeeTermResource

__all__ = ["SpvDetail"]


class SpvDetail(BaseModel):
    """An OPEN SPV's identity, exact economics, and typed fee schedule."""

    id: str
    """Stable SPV identifier."""

    company_id: str
    """Company whose shares the vehicle holds."""

    currency: Currency
    """Terms currency."""

    name: str
    """Legal/display name."""

    status: SpvStatus
    """Lifecycle state."""

    all_in_price_per_share: Optional[str] = None
    """Price per share including fees."""

    custodian_name: Optional[str] = None
    """Custodian."""

    fee_per_share: Optional[str] = None
    """Per-share fee."""

    fee_terms: Optional[List[SpvFeeTermResource]] = None
    """Typed fee schedule."""

    funded_percent: Optional[str] = None
    """Percentage of dollar allocation funded, derived from the allocation pair."""

    funding_deadline: Optional[datetime] = None
    """Funding deadline."""

    manager_name: Optional[str] = None
    """SPV manager."""

    minimum_investment_amount: Optional[str] = None
    """Minimum investment amount."""

    opened_at: Optional[datetime] = None
    """Time the vehicle opened."""

    price_per_share: Optional[str] = None
    """Price per share excluding fees."""

    remaining_allocation_amount: Optional[str] = None
    """Remaining dollar allocation."""

    remaining_share_allocation: Optional[str] = None
    """Remaining share allocation."""

    share_class: Optional[str] = None
    """Underlying share class, when specified."""

    structure_description: Optional[str] = None
    """Plain-text vehicle structure."""

    total_allocation_amount: Optional[str] = None
    """Total dollar allocation."""

    total_share_allocation: Optional[str] = None
    """Total share allocation."""

    valuation: Optional[str] = None
    """Exact company valuation."""

    valuation_basis: Optional[ValuationBasis] = None
    """Meaning of `valuation`."""
