# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .modifier_arg import ModifierArg

__all__ = ["ModifierDef"]


class ModifierDef(BaseModel):
    """A modifier operation and the positional `args` each context accepts."""

    args: List[ModifierArg]
    """The positional `args` slots, in order."""

    name: str
    """The modifier operation name: one of `"ADD"` or `"SUBTRACT"`."""
