# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["IoiOfferingResource"]


class IoiOfferingResource(BaseModel):
    """Offering identity embedded in an IOI list item."""

    id: str

    headline: str
