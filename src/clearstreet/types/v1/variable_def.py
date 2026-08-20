# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["VariableDef"]


class VariableDef(BaseModel):
    """A built-in variable, as accepted in `filters[].right[].variable`."""

    description: str
    """A human-readable description of what the variable resolves to."""

    name: str
    """The variable name as accepted in `filters[].right[].variable`."""

    resolves_to: str
    """What the variable resolves to at call time (`DATE` for all built-ins)."""
