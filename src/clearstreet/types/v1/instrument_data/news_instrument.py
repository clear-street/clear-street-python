# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["NewsInstrument"]


class NewsInstrument(BaseModel):
    """Instrument associated with a news item."""

    instrument_id: str
    """Instrument identifier."""

    name: Optional[str] = None
    """
    Instrument name/description, if available. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    symbol: Optional[str] = None
    """
    Trading symbol, if available. When a null/undefined value is observed, it
    indicates that there is no available data.
    """
