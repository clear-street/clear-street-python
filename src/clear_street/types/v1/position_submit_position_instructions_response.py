# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .position_instruction_list import PositionInstructionList

__all__ = ["PositionSubmitPositionInstructionsResponse"]


class PositionSubmitPositionInstructionsResponse(BaseResponse):
    data: PositionInstructionList
