# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContentPartCustomPayload"]


class ContentPartCustomPayload(BaseModel):
    """Escape-hatch custom payload content part."""

    payload: object
