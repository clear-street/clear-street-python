# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageSubmitFeedbackParams"]


class MessageSubmitFeedbackParams(TypedDict, total=False):
    score: Required[int]
    """Feedback score (-1, 0, +1 or 1-5)."""

    account_id: Optional[int]
    """Optional selection. Feedback always uses the thread's linked account."""

    comment: str
    """Optional feedback comment"""

    metadata: Optional[object]
    """Optional metadata"""
