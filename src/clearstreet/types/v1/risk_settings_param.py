# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RiskSettingsParam"]


class RiskSettingsParam(TypedDict, total=False):
    """Risk settings for an account"""

    max_notional: Optional[str]
    """The maximum notional value available to the account"""
