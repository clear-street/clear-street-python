# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..sort_direction import SortDirection
from .field_ref_param import FieldRefParam

__all__ = ["SortSpecParam"]


class SortSpecParam(TypedDict, total=False):
    """A sort specification pairing a field with a direction."""

    field: Required[FieldRefParam]
    """The field to sort by."""

    direction: SortDirection
    """Sort direction (defaults to DESC)."""
