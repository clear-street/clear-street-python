# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .alert import Alert
from ..shared.base_response import BaseResponse

__all__ = ["AlertGetAlertByIDResponse"]


class AlertGetAlertByIDResponse(BaseResponse):
    data: Alert
    """A stored alert: the spec it was created with plus its lifecycle facts."""
