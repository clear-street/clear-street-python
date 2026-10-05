# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Thread"]


class Thread(BaseModel):
    """Thread metadata."""

    id: str

    created_at: datetime

    title: str

    updated_at: datetime
    """
    Time of the last activity: a new message in the thread or a change to the
    thread.
    """
