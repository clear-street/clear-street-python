# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ThreadGetThreadResponseParams"]


class ThreadGetThreadResponseParams(TypedDict, total=False):
    account_id: int
    """
    Lists only conversations for this account, or unlinked conversations when
    omitted. Other reads authorize the resource's linked account. Omit when no
    account is selected; empty values and the string null are invalid.
    """
