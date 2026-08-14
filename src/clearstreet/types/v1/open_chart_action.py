# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OpenChartAction"]


class OpenChartAction(BaseModel):
    """Action to open a chart for a symbol."""

    symbol: str
    """Trading symbol to chart"""

    extras: Optional[object] = None
    """
    Additional chart configuration (indicators, overlays, etc.) When a
    null/undefined value is observed, it indicates it does not apply.
    """

    item_id: Optional[str] = None
    """Interaction-tracking identity.

    Absent on messages created before tracking. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    timeframe: Optional[str] = None
    """
    Chart timeframe (e.g., "1D", "1W", "1M", "3M", "1Y", "5Y") When a null/undefined
    value is observed, it indicates it does not apply.
    """
