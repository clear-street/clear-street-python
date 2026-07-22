# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["SnapshotSession"]


class SnapshotSession(BaseModel):
    """Session-level pricing metrics for a market data snapshot."""

    change: str
    """Absolute change from previous close to last trade."""

    change_percent: str
    """Percent change from previous close to last trade."""

    previous_close: str
    """Previous session close price."""
