# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContentPartTextPayload"]


class ContentPartTextPayload(BaseModel):
    """Text content part."""

    text: str
