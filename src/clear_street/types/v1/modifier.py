# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel
from .modifier_op import ModifierOp

__all__ = ["Modifier"]


class Modifier(BaseModel):
    """Arithmetic modifier applied to a variable value."""

    args: List[Union[float, str]]

    name: ModifierOp
    """The modifier operation."""
