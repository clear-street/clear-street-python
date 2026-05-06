# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from ...active.v1.accounts.exercise_instruction import ExerciseInstruction

__all__ = ["ExerciseCancelExerciseResponse"]


class ExerciseCancelExerciseResponse(BaseResponse):
    data: ExerciseInstruction
    """
    The API representation of a single CSC instruction, combining the caller's
    request with the `oems-csc` lifecycle state.
    """
