# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ModifierArg"]


class ModifierArg(BaseModel):
    """One positional `modifier.args` slot."""

    kind: str
    """`"NUMBER"` or `"ENUM"`."""

    note: str
    """The arg's meaning and constraints."""

    position: int
    """Zero-based position in the `args` array."""

    required: bool
    """Whether the arg must be present in every modifier use."""

    default: Optional[str] = None
    """For optional args: the value used when the arg is omitted."""

    ref: Optional[str] = None
    """For `"ENUM"` args: the `enums` list the value must be a member of."""
