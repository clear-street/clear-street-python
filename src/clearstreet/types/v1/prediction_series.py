# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PredictionSeries"]


class PredictionSeries(BaseModel):
    """A prediction market series: a family of related markets that share a code."""

    code: str
    """Series code, shared by the markets in the family."""
