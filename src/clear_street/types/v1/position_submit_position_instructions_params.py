# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .position_instruction_type import PositionInstructionType

__all__ = ["PositionSubmitPositionInstructionsParams", "Instruction"]


class PositionSubmitPositionInstructionsParams(TypedDict, total=False):
    instructions: Required[Iterable[Instruction]]


class Instruction(TypedDict, total=False):
    """A position instruction to submit.

    Use `DELETE /accounts/{account_id}/positions/instructions/{instruction_id}`
    to cancel an outstanding instruction.
    """

    instruction_type: Required[PositionInstructionType]
    """The action to take."""

    instrument_id: Required[str]
    """Identifier of the options contract to act on. Unknown ids return 404."""

    quantity: Required[str]
    """Number of contracts to include in the instruction."""

    instruction_id: Optional[str]
    """Caller-supplied idempotency key.

    Echoed on the response. The server generates a unique id when omitted.
    """
