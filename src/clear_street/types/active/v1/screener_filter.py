# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ScreenerFilter"]


class ScreenerFilter(BaseModel):
    """A single filter criterion for the screener."""

    field: str
    """Field to filter on (e.g., "market_cap", "sector", "price")"""

    operator: str
    """Comparison operator (e.g., "eq", "gte", "lte", "in")"""

    value: object
    """Filter value"""
