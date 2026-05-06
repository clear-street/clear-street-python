# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...active.v1.accounts.exercise_action import ExerciseAction

__all__ = ["ExerciseSubmitExercisesParams", "Exercise"]


class ExerciseSubmitExercisesParams(TypedDict, total=False):
    exercises: Required[Iterable[Exercise]]


class Exercise(TypedDict, total=False):
    """One exercise / DNE / CEA instruction requested by a client.

    Cancel is not an action — use `DELETE /accounts/{account_id}/exercises/{exercise_id}`.
    """

    action: Required[ExerciseAction]
    """Instruction type."""

    instrument_id: Required[str]
    """OEMS instrument identifier.

    api-gw resolves this to `security_id` + `security_id_source` via the instrument
    cache before dispatching to `oems-csc`. Unknown ids return 404.
    """

    quantity: Required[str]
    """Quantity of contracts to exercise / DNE / CEA."""

    client_exercise_id: Optional[str]
    """Caller-supplied correlation id.

    Echoed back on the response and used as the FIX `pos_req_id` (tag 710) for
    idempotency. If omitted the server generates a UUID.
    """
