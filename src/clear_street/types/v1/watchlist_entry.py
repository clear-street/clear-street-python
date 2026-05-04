# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["WatchlistEntry"]


class WatchlistEntry(BaseModel):
    """Represents a user watchlist."""

    id: str
    """The unique identifier for the watchlist."""

    created_at: datetime
    """The timestamp when the watchlist was created."""

    name: str
    """The user-provided watchlist name."""
