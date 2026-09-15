# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .position_instruction_type import PositionInstructionType
from .position_instruction_status import PositionInstructionStatus
from .position_instruction_rejection import PositionInstructionRejection

__all__ = ["PositionInstruction"]


class PositionInstruction(BaseModel):
    """A position instruction and its current lifecycle state."""

    id: str
    """Server-assigned id. Used as the path parameter on cancel."""

    account_id: int
    """Account the instruction belongs to."""

    client_instruction_id: str
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

    Populated once the instruction reaches `ACCEPTED`. When a null/undefined value
    is observed, it indicates that there is no available data.
    """

    created_at: Optional[datetime] = None
    """
    When the instruction was first accepted by the service. When a null/undefined
    value is observed, it indicates that there is no available data.
    """

    rejection: Optional[PositionInstructionRejection] = None
    """
    Machine-readable counterpart to `rejection_reason`: a stable reason code plus
    params, present on every rejected row that has a `rejection_reason` — on submit,
    cancel, get, and list alike. Branch on `rejection.reason` instead of parsing
    `rejection_reason`. Forward-only: instructions rejected before this field
    shipped may carry only `rejection_reason`. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    rejection_reason: Optional[str] = None
    """
    Human-readable explanation populated on any non-success terminal status —
    `REJECTED` or `CANCEL_FAILED`. On a `207 Multi-Status` batch submit the
    top-level `error` field summarizes the batch; per-row detail continues to live
    here. When a null/undefined value is observed, it indicates it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """
    Identifier of the underlying instrument, when available. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    updated_at: Optional[datetime] = None
    """
    When the instruction's lifecycle state last changed. When a null/undefined value
    is observed, it indicates that there is no available data.
    """
