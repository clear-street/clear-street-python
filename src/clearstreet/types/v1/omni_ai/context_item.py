# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ContextItem"]


class ContextItem(BaseModel):
    """A snapshot of the widget the user asks about."""

    data: Dict[str, object]
    """Relevant widget data, selections, and units.

    Use strings for exact decimals and large IDs.
    """

    kind: str
    """Nonblank descriptive kind. New kinds do not require a backend release."""

    label: str
    """Nonblank attachment label for conversation rendering."""

    captured_at: Optional[datetime] = None
    """Client-reported snapshot time. Omit when unknown."""
