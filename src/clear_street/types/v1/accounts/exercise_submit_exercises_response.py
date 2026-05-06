# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from ...active.v1.accounts.exercise_instruction_list import ExerciseInstructionList

__all__ = ["ExerciseSubmitExercisesResponse"]


class ExerciseSubmitExercisesResponse(BaseResponse):
    data: ExerciseInstructionList
