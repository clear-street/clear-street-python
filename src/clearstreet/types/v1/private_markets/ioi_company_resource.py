# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["IoiCompanyResource"]


class IoiCompanyResource(BaseModel):
    """Company identity embedded in an IOI list item."""

    id: str

    name: str
