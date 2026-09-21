# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContextItemParam"]


class ContextItemParam(TypedDict, total=False):
    """A snapshot of the widget the user asks about."""

    data: Required[Dict[str, object]]
    """Relevant widget data, selections, and units.

    Use strings for exact decimals and large IDs.
    """

    kind: Required[str]
    """Nonblank descriptive kind. New kinds do not require a backend release."""

    label: Required[str]
    """Nonblank attachment label for conversation rendering."""

    captured_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Client-reported snapshot time. Omit when unknown."""
