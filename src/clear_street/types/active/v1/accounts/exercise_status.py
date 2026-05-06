# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ExerciseStatus"]

ExerciseStatus: TypeAlias = Literal[
    "SENT", "ACCEPTED", "REJECTED", "ENGINE_REJECTED", "CANCEL_REQUESTED", "CANCELLED", "CANCEL_FAILED", "UNKNOWN"
]
