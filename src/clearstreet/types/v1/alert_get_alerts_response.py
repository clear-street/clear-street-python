# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .alert_list import AlertList
from ..shared.base_response import BaseResponse

__all__ = ["AlertGetAlertsResponse"]


class AlertGetAlertsResponse(BaseResponse):
    data: AlertList
