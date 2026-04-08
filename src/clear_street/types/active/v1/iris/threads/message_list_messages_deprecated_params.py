# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageListMessagesDeprecatedParams"]


class MessageListMessagesDeprecatedParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID for the request"""

    after_seq: int
    """Return messages after this sequence number"""

    page_size: int
    """Maximum messages to return"""

    page_token: str
    """Page token for pagination"""
