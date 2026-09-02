# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .currency import Currency
from ...._models import BaseModel
from .offering_spv import OfferingSpv
from .offering_class import OfferingClass
from .valuation_basis import ValuationBasis
from .offering_company import OfferingCompany

__all__ = ["OfferingCard"]


class OfferingCard(BaseModel):
    """
    One offering as it appears in a list: its derived class, indicative terms,
    a company identity summary, and any attached SPV.
    """

    id: str
    """Stable public identifier; IOIs and history hang off it."""

    class_: OfferingClass = FieldInfo(alias="class")
    """Derived classification."""

    company: OfferingCompany
    """Owning company identity."""

    currency: Currency
    """Terms currency."""

    headline: str
    """Card/detail headline."""

    summary: str
    """Top opportunity paragraph."""

    indicative_price_high: Optional[str] = None
    """Indicative price-per-share range, high endpoint."""

    indicative_price_low: Optional[str] = None
    """Indicative price-per-share range, low endpoint."""

    indicative_valuation_basis: Optional[ValuationBasis] = None
    """Meaning of the indicative valuation range."""

    indicative_valuation_high: Optional[str] = None
    """Indicative valuation range, high endpoint."""

    indicative_valuation_low: Optional[str] = None
    """Indicative valuation range, low endpoint."""

    ioi_deadline: Optional[datetime] = None
    """Deadline for indications of interest."""

    minimum_ioi_amount: Optional[str] = None
    """Minimum indication-of-interest amount."""

    spv: Optional[OfferingSpv] = None
    """Attached SPV identity and lifecycle, once one exists."""
