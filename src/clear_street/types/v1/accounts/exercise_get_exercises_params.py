# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExerciseGetExercisesParams"]


class ExerciseGetExercisesParams(TypedDict, total=False):
    instrument_id: str
    """Filter by OEMS instrument id."""
