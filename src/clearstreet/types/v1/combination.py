# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Combination"]


class Combination(BaseModel):
    """A single combination, expressed with the API's own parameter names.

    At most one of `period` / `lookback` is set; a combination with neither
    selects the field's current or most recent value.
    """

    lookback: Optional[str] = None
    """The lookback, a member of `enums.lookback`."""

    period: Optional[str] = None
    """The period, a member of `enums.period`."""
