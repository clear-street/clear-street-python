# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .position_instruction_type import PositionInstructionType

__all__ = ["InstructionSubmitPositionInstructionsParams", "Instruction"]


class InstructionSubmitPositionInstructionsParams(TypedDict, total=False):
    instructions: Required[Iterable[Instruction]]


class Instruction(TypedDict, total=False):
    """One exercise / DNE / CEA instruction requested by a client.

    Cancel is not an instruction type — use `DELETE /accounts/{account_id}/positions/instructions/{instruction_id}`.
    """

    instruction_type: Required[PositionInstructionType]
    """Instruction type."""

    instrument_id: Required[str]
    """OEMS instrument identifier.

    api-gw resolves this to `security_id` + `security_id_source` via the instrument
    cache before dispatching to `oems-csc`. Unknown ids return 404.
    """

    quantity: Required[str]
    """Quantity of contracts to exercise / DNE / CEA."""

    instruction_id: Optional[str]
    """Caller-supplied instruction id.

    Echoed back on the response and used as the FIX `pos_req_id` (tag 710) for
    idempotency. If omitted the server generates a UUID.
    """
