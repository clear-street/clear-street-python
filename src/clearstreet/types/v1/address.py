# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    """A postal address."""

    city: str
    """City"""

    country: str
    """Country"""

    line1: str
    """First street address line"""

    postal_code: str
    """Postal code"""

    line2: Optional[str] = None
    """
    Second street address line When a null/undefined value is observed, it indicates
    it does not apply.
    """

    state: Optional[str] = None
    """
    State or province When a null/undefined value is observed, it indicates it does
    not apply.
    """
