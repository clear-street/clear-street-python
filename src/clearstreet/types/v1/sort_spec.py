# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .field_ref import FieldRef
from ..sort_direction import SortDirection

__all__ = ["SortSpec"]


class SortSpec(BaseModel):
    """A sort specification pairing a field with a direction."""

    field: FieldRef
    """The field to sort by."""

    direction: Optional[SortDirection] = None
    """Sort direction (defaults to DESC)."""
