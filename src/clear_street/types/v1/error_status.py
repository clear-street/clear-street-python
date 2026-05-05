# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ErrorStatus"]


class ErrorStatus(BaseModel):
    """Shared sanitized error payload."""

    code: str

    message: str

    details: Optional[object] = None
