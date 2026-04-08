# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..security_id_source import SecurityIDSource

__all__ = ["NewsInstrument"]


class NewsInstrument(BaseModel):
    """Instrument associated with a news item."""

    security_id: str
    """Security identifier value."""

    security_id_source: SecurityIDSource
    """Security identifier source."""

    instrument_id: Optional[str] = None
    """OEMS instrument UUID, if available from instrument cache enrichment."""

    name: Optional[str] = None
    """Instrument name/description, if available from instrument cache enrichment."""

    symbol: Optional[str] = None
    """Trading symbol, if available from instrument cache enrichment."""
