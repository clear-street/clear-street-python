# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Thread"]


class Thread(BaseModel):
    """Thread metadata returned by list/get thread endpoints."""

    id: str

    created_at: datetime

    title: str

    updated_at: datetime
