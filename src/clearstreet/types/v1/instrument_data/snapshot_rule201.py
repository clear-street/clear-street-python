# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .rule201_state import Rule201State

__all__ = ["SnapshotRule201"]


class SnapshotRule201(BaseModel):
    """Live SEC Rule 201 short-sale price test state for a single security.

    Rule 201 triggers when a security falls 10% below the previous close, and
    then restricts non-exempt short sales at or below the national best bid for
    the rest of that day and all of the next trading day.
    """

    state: Rule201State
    """Current price test state for this security."""
