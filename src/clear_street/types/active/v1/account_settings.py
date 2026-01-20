# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .risk_settings import RiskSettings

__all__ = ["AccountSettings"]


class AccountSettings(BaseModel):
    risk: Optional[RiskSettings] = None
    """Risk settings for the account"""
