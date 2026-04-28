# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .open_chart_action import OpenChartAction
from .open_screener_action import OpenScreenerAction
from .prefill_order_action import PrefillOrderAction
from .open_entitlement_consent_action import OpenEntitlementConsentAction

__all__ = ["StructuredAction", "PrefillOrder", "OpenChart", "OpenScreener", "OpenEntitlementConsent"]


class PrefillOrder(BaseModel):
    """Prefill an order ticket for user confirmation"""

    prefill_order: PrefillOrderAction
    """Prefill an order ticket for user confirmation"""


class OpenChart(BaseModel):
    """Open a chart for a symbol"""

    open_chart: OpenChartAction
    """Open a chart for a symbol"""


class OpenScreener(BaseModel):
    """Open a stock screener with filters"""

    open_screener: OpenScreenerAction
    """Open a stock screener with filters"""


class OpenEntitlementConsent(BaseModel):
    """Open entitlement consent flow"""

    open_entitlement_consent: OpenEntitlementConsentAction
    """Open entitlement consent flow"""


StructuredAction: TypeAlias = Union[PrefillOrder, OpenChart, OpenScreener, OpenEntitlementConsent]
