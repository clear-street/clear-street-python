# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["FieldColumns"]


class FieldColumns(BaseModel):
    """
    Struct-of-arrays: all four fields are the same length, index `i` is one
    field.
    """

    description: List[str]
    """A human-readable description of the field."""

    display_name: List[str]
    """The display name of the column when no `period` / `lookback` is set."""

    kind: List[int]
    """Index into `Catalog::kinds`."""

    name: List[str]
    """
    The base field name, as accepted in a request's `left.name` / `right[].variable`
    field reference.
    """
