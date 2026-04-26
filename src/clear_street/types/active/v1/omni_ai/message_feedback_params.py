# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageFeedbackParams"]


class MessageFeedbackParams(TypedDict, total=False):
    account_id: Required[int]
    """Account ID for the request"""

    score: Required[int]
    """Feedback score (-1, 0, +1 or 1-5)"""

    comment: str
    """Optional feedback comment"""

    metadata: Optional[object]
    """Optional metadata"""
