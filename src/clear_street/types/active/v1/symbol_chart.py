# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SymbolChart"]


class SymbolChart(BaseModel):
    """Chart for a single symbol and timeframe."""

    symbol: str

    timeframe: Optional[str] = None
