# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["APIKeyListEntry"]


class APIKeyListEntry(BaseModel):
    id: str

    created_at: datetime

    expires_at: datetime

    name: Optional[str] = None

    revoked_at: Optional[datetime] = None
