# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .position_instruction import PositionInstruction
from ..shared.base_response import BaseResponse

__all__ = ["PositionCancelPositionInstructionResponse"]


class PositionCancelPositionInstructionResponse(BaseResponse):
    data: PositionInstruction
    """
    The API representation of a single CSC instruction, combining the caller's
    request with the `oems-csc` lifecycle state.
    """
