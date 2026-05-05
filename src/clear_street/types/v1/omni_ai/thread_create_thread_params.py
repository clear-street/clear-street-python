# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThreadCreateThreadParams", "Target"]


class ThreadCreateThreadParams(TypedDict, total=False):
    account_id: Required[int]

    type: Required[Literal["instant", "deep_insights"]]
    """Thread creation mode."""

    capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]

    target: Optional[Target]
    """Deep-insights target payload."""

    text: Optional[str]

    thesis: Optional[str]


class Target(TypedDict, total=False):
    """Deep-insights target payload."""

    ticker: Required[str]

    type: Required[Literal["ticker"]]
    """Deep-insights target type. Launch supports ticker-only."""
