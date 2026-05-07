# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from ....active.v1.accounts.positions.position_instruction_list import PositionInstructionList

__all__ = ["InstructionSubmitPositionInstructionsResponse"]


class InstructionSubmitPositionInstructionsResponse(BaseResponse):
    data: PositionInstructionList
