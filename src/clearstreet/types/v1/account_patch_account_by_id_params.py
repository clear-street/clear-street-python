# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .risk_settings_param import RiskSettingsParam

__all__ = ["AccountPatchAccountByIDParams"]


class AccountPatchAccountByIDParams(TypedDict, total=False):
    risk: Optional[RiskSettingsParam]
    """Risk settings for the account"""
