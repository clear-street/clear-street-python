# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .schedule import Schedule
from .trigger_mode import TriggerMode

__all__ = ["AlertCreateAlertParams"]


class AlertCreateAlertParams(TypedDict, total=False):
    condition: Required[object]
    """
    The boolean condition tree, in the condition grammar. `"instrument_id"`
    references accept a ticker or an OEMS instrument id.
    """

    schedule: Required[Schedule]
    """How often an alert's condition is evaluated."""

    trigger: Required[TriggerMode]
    """How an alert triggers. `once` alerts complete after their first trigger."""

    account_id: Optional[int]
    """The account whose `account.*` signals and holdings scopes the condition reads.

    Optional: a market-only alert needs no account.
    """
