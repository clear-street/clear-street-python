# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .enums import Enums
from .rules import Rules
from ..._models import BaseModel
from .field_kind import FieldKind
from .modifier_def import ModifierDef
from .variable_def import VariableDef
from .field_columns import FieldColumns

__all__ = ["Catalog"]


class Catalog(BaseModel):
    """
    The complete screener field catalog, serialized as the `data` payload of
    `GET /screener/catalog`.
    """

    default_response_fields: List[str]
    """
    The `api_name`s that resolve to the POST default column set when `columns` is
    omitted.
    """

    enums: Enums
    """The enum universes every other section's values are drawn from."""

    fields: FieldColumns
    """Struct-of-arrays of the remaining per-field scalars."""

    kinds: List[FieldKind]
    """
    The deduplicated
    `(category, format, value_type, combinations, default combination)` tuples;
    `fields.kind[i]` indexes into this.
    """

    modifiers: List[ModifierDef]
    """The modifier operations and their legal `args` forms."""

    operators_by_value_type: Dict[str, List[str]]
    """`value_type` -> canonically-ordered valid operators."""

    rules: Rules
    """Request-side semantics for turning the data into a valid call."""

    suffixes: Dict[str, str]
    """Axis token -> abbreviation, for every token in use in `kinds`."""

    variables: List[VariableDef]
    """The built-in variables accepted in `filters[].right[].variable`."""
