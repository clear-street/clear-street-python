# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RiskSettings"]


class RiskSettings(BaseModel):
    """Risk settings for an account"""

    max_notional: Optional[str] = None
    """The maximum notional value available to the account"""
