# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from .modifier_op import ModifierOp

__all__ = ["ModifierParam"]


class ModifierParam(TypedDict, total=False):
    """Arithmetic modifier applied to a variable value."""

    args: Required[SequenceNotStr[Union[float, str]]]

    name: Required[ModifierOp]
    """The modifier operation."""
