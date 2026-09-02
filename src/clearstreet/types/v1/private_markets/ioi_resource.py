# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .currency import Currency
from ...._models import BaseModel
from .nda_acceptance_resource import NdaAcceptanceResource

__all__ = ["IoiResource"]


class IoiResource(BaseModel):
    """One live indication of interest."""

    id: str

    account_id: int

    created_at: datetime

    currency: Currency
    """Terms currency."""

    notional_amount: str

    offering_id: str

    updated_at: datetime

    nda_acceptance: Optional[NdaAcceptanceResource] = None
    """Most recent NDA acceptance linked to this IOI, if any."""
