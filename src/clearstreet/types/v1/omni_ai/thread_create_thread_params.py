# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .turn_context_param import TurnContextParam

__all__ = ["ThreadCreateThreadParams", "Target"]


class ThreadCreateThreadParams(TypedDict, total=False):
    type: Required[Literal["instant", "deep_insights"]]
    """Thread creation mode."""

    account_id: Optional[int]
    """Selected account for creation or the first account-linked turn.

    Omit for an unlinked conversation. An existing account link remains
    authoritative even when another account is selected.
    """

    capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]

    context: Optional[TurnContextParam]
    """Snapshots for the first instant-chat message. Omit to attach no new context."""

    target: Optional[Target]
    """Deep-insights target payload."""

    text: Optional[str]

    thesis: Optional[str]


class Target(TypedDict, total=False):
    """Deep-insights target payload."""

    ticker: Required[str]

    type: Required[Literal["ticker"]]
    """Deep-insights target type. Launch supports ticker-only."""
