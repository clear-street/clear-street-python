# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .turn_context_param import TurnContextParam

__all__ = ["ThreadCreateMessageParams"]


class ThreadCreateMessageParams(TypedDict, total=False):
    text: Required[str]

    account_id: Optional[int]
    """Selected account for creation or the first account-linked turn.

    Omit for an unlinked conversation. An existing account link remains
    authoritative even when another account is selected.
    """

    capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]

    context: Optional[TurnContextParam]
    """Snapshots for this instant-chat message.

    Omission does not remove earlier attachments.
    """
