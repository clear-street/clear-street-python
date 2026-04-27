# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Revocation"]


class Revocation(BaseModel):
    id: str

    revoked_at: datetime
