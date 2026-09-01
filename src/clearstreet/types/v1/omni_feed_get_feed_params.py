# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OmniFeedGetFeedParams"]


class OmniFeedGetFeedParams(TypedDict, total=False):
    account_id: int
    """Trading account to serve as context. Optional — the feed works without one."""

    cursor: str
    """
    Id of the last item already received; the response continues from the item after
    it. Omit to resume from the oldest unseen item.
    """

    limit: int
    """Maximum number of items to return (1–100, default 20)."""
