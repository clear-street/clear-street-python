# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreateAlertResponse"]


class CreateAlertResponse(BaseModel):
    """Response payload for alert creation."""

    alert_id: str
