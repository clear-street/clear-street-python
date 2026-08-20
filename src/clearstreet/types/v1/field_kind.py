# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .combination import Combination

__all__ = ["FieldKind"]


class FieldKind(BaseModel):
    """
    One deduplicated `(category, format, value_type, combinations, default
    combination)` tuple; `fields.kind[i]` indexes into `Catalog::kinds`.
    """

    category: str
    """The field's category, a member of `enums.category`."""

    combinations: List[Combination]
    """Ordered, in declaration order.

    The empty combination is the current or most recent value.
    """

    default_combination: Combination
    """
    The combination a bare field reference resolves to: the field's current or most
    recent value when the kind offers it, otherwise the kind's default `period` /
    `lookback`.
    """

    format: str
    """The field's format, a member of `enums.format`."""

    value_type: str
    """The field's value type, a member of `enums.value_type`."""
