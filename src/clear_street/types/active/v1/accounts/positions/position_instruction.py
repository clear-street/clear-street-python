# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ......_models import BaseModel
from .position_instruction_type import PositionInstructionType
from .position_instruction_status import PositionInstructionStatus

__all__ = ["PositionInstruction"]


class PositionInstruction(BaseModel):
    """
    The API representation of a single CSC instruction, combining the caller's
    request with the `oems-csc` lifecycle state.
    """

    id: str
    """Stable server-assigned id for the instruction (the engine instruction UUID).

    Used as the `{instruction_id}` path parameter on DELETE.
    """

    account_id: int
    """Account the instruction belongs to."""

    instruction_id: str
    """
    Caller-supplied instruction id (echoed from the submit request, or the
    server-generated fallback when the caller omitted one).
    """

    instruction_type: PositionInstructionType
    """The instruction type as understood by this API."""

    instrument_id: str
    """OEMS instrument identifier the instruction is for."""

    osi: str
    """OSI option symbol (e.g.

    `AAPL 280121C00195000`). Display-only; resolved from the instrument cache.
    """

    quantity: str
    """Quantity of contracts."""

    status: PositionInstructionStatus
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
