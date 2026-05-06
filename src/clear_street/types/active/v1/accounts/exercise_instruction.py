# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel
from .exercise_action import ExerciseAction
from .exercise_status import ExerciseStatus
from ....security_id_source import SecurityIDSource

__all__ = ["ExerciseInstruction"]


class ExerciseInstruction(BaseModel):
    """
    The API representation of a single CSC instruction, combining the caller's
    request with the `oems-csc` lifecycle state.
    """

    id: str
    """Stable server-assigned id for the instruction (the engine instruction UUID).

    Used as the `{exercise_id}` path parameter on DELETE.
    """

    account_id: int
    """Account the instruction belongs to."""

    action: ExerciseAction
    """The instruction type as understood by this API."""

    client_exercise_id: str
    """
    Caller-supplied correlation id (echoed from the submit request, or the
    server-generated fallback when the caller omitted one).
    """

    instrument_id: str
    """OEMS instrument identifier the instruction is for."""

    quantity: str
    """Quantity of contracts."""

    security_id: str
    """Security identifier (display-only; resolved from the instrument cache)."""

    security_id_source: SecurityIDSource
    """Security identifier source (display-only)."""

    status: ExerciseStatus
    """Current lifecycle status."""

    symbol: str
    """Trading symbol resolved from the instrument cache.

    Empty if the instrument cannot be resolved (e.g. expired option).
    """

    accepted_quantity: Optional[str] = None
    """Quantity accepted by OCC. Populated after `ACCEPTED`."""

    created_at: Optional[datetime] = None
    """Row creation timestamp surfaced from `oems-csc`."""

    error: Optional[str] = None
    """Inline error detail when a batch entry was rejected (omitted on success)."""

    rejection_reason: Optional[str] = None
    """Reason text populated on terminal reject / cancel-failed statuses."""

    updated_at: Optional[datetime] = None
    """Last update timestamp surfaced from `oems-csc`."""
