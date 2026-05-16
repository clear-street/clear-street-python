# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .position_instruction import PositionInstruction
from ..shared.base_response import BaseResponse

__all__ = ["PositionCancelPositionInstructionResponse"]


class PositionCancelPositionInstructionResponse(BaseResponse):
    data: PositionInstruction
    """A position instruction and its current lifecycle state."""
