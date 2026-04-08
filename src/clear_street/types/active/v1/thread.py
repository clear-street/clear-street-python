# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Thread"]


class Thread(BaseModel):
    account_id: str

    created_at: str

    description: str

    owner_user_id: str

    title: str

    updated_at: str

    id: Optional[str] = None

    metadata: Optional[object] = None
