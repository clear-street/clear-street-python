# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .schedule import Schedule
from ..._models import BaseModel
from .alert_source import AlertSource
from .alert_status import AlertStatus
from .trigger_mode import TriggerMode

__all__ = ["Alert"]


class Alert(BaseModel):
    """A stored alert: the spec it was created with plus its lifecycle facts."""

    id: str

    condition: object
    """
    The boolean condition tree, with instrument references resolved to OEMS
    instrument ids.
    """

    created_at: str

    schedule: Schedule
    """How often an alert's condition is evaluated."""

    source: AlertSource
    """Where an alert came from."""

    status: AlertStatus
    """Lifecycle status of an alert.

    Soft-deleted alerts are invisible on this API, so there is no `deleted` value.
    """

    trigger: TriggerMode
    """How an alert triggers. `once` alerts complete after their first trigger."""

    account_id: Optional[int] = None

    expires_at: Optional[str] = None

    omni_text: Optional[str] = None
    """The originating natural-language text, for alerts compiled from one."""

    triggered_at: Optional[str] = None
    """When the alert last triggered; absent if it never has."""
