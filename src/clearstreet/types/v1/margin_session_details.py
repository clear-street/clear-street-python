# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MarginSessionDetails"]


class MarginSessionDetails(BaseModel):
    buying_power: str
    """Maximum buying power available in the account during the session."""

    multiplier: Optional[str] = None
    """Effective multiplier for margin calculations during the session."""
