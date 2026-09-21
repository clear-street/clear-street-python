# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .context_item_param import ContextItemParam

__all__ = ["TurnContextParam"]


class TurnContextParam(TypedDict, total=False):
    """Client snapshots attached to one instant-chat user message.

    Context is separate from visible message text and does not grant account access.
    The compact JSON representation must not exceed 64 KiB.
    """

    items: Required[Iterable[ContextItemParam]]
    """One to four snapshots.

    Each snapshot's data may contain at most 32 levels of nesting.
    """
