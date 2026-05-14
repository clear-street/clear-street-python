# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .position_instruction_type import PositionInstructionType
from .position_instruction_status import PositionInstructionStatus

__all__ = ["PositionInstruction"]


class PositionInstruction(BaseModel):
    """A position instruction and its current lifecycle state."""

    id: str
    """Server-assigned id. Used as the path parameter on cancel."""

    account_id: int
    """Account the instruction belongs to."""

    instruction_id: str
    """
    Caller-supplied idempotency key echoed from the submit request; the
    server-assigned fallback when none was supplied.
    """

    instruction_type: PositionInstructionType
    """The action this instruction requests."""

    instrument_id: str
    """Identifier of the options contract this instruction acts on."""

    quantity: str
    """Number of contracts included in the instruction."""

    status: PositionInstructionStatus
    """Current lifecycle status."""

    symbol: str
    """Options symbol (OSI) for display."""

    accepted_quantity: Optional[str] = None
    """Number of contracts accepted by the clearing venue.

    Populated once the instruction reaches `ACCEPTED`.
    """

    created_at: Optional[datetime] = None
    """When the instruction was first accepted by the service."""

    error: Optional[str] = None
    """Per-row error on a batch submission (omitted on success)."""

    rejection_reason: Optional[str] = None
    """Explanation populated on terminal reject or cancel-failed statuses."""

    updated_at: Optional[datetime] = None
    """When the instruction's lifecycle state last changed."""
