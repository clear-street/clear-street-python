# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from .variable import Variable
from ..._models import BaseModel

__all__ = ["FilterValue"]


class FilterValue(BaseModel):
    """A filter value: either a literal or a variable reference."""

    value: Union[float, str, None] = None

    variable: Optional[Variable] = None
    """A variable reference."""
