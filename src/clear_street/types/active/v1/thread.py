# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Thread"]


class Thread(BaseModel):
    """Thread metadata returned by list/get thread endpoints."""

    id: str

    created_at: str

    description: str

    title: str

    updated_at: str
