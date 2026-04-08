# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["SnapshotLastTrade"]


class SnapshotLastTrade(BaseModel):
    """Last-trade fields for a market data snapshot."""

    price: str
    """Most recent last-sale eligible trade price."""
