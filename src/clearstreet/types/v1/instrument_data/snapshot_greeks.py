# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["SnapshotGreeks"]


class SnapshotGreeks(BaseModel):
    """Theoretical price and Greeks for an options snapshot.

    All values are
    **per share**; no contract multiplier is applied.
    """

    delta: str
    """Delta: ∂V/∂S, range \\[[-1, 1\\]]."""

    gamma: str
    """Gamma: ∂²V/∂S²."""

    iv: str
    """Implied volatility.

    Temporarily withheld: always `0`. Do not use this value; it is not a market
    implied volatility.
    """

    rho: str
    """Rho per 1.0 rate point."""

    theo_price: str
    """Theoretical option price in USD per share."""

    theta: str
    """Theta per trading day."""

    timestamp: datetime
    """Timestamp when the Greeks were calculated."""

    vega: str
    """Vega per 1.0 vol point."""
