# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .create_alert_response import CreateAlertResponse

__all__ = ["AlertCreateAlertResponse"]


class AlertCreateAlertResponse(BaseResponse):
    data: CreateAlertResponse
    """Response payload for alert creation."""
