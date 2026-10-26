# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["OrderPreviewError"]


class OrderPreviewError(BaseModel):
    """
    One pre-trade risk-check error the order would trigger, shaped like
    the violation entries in `ApiError.details[]` on rejected submissions.
    """

    description: str
    """Human-readable description of the error."""

    metadata: Dict[str, str]
    """
    Structured details for the error (stringified values), e.g. required and
    available amounts, and `leg_index`/`leg_symbol` for multileg leg errors.
    """

    type: str
    """Stable error code."""
