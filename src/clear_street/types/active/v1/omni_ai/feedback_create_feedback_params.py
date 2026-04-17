# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FeedbackCreateFeedbackParams"]


class FeedbackCreateFeedbackParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID for the request"""

    message_id: Required[str]
    """Message to provide feedback on"""

    score: Required[int]
    """Feedback score (-1, 0, +1 or 1-5)"""

    thread_id: Required[str]
    """Thread containing the message"""

    comment: str
    """Optional feedback comment"""

    metadata: Optional[object]
    """Optional metadata"""
