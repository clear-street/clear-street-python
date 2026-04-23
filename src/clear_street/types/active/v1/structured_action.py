# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .open_chart_action import OpenChartAction
from .open_screener_action import OpenScreenerAction
from .prefill_order_action import PrefillOrderAction
from .open_entitlement_consent_action import OpenEntitlementConsentAction

__all__ = ["StructuredAction", "PrefillOrder", "OpenChart", "OpenScreener", "OpenEntitlementConsent"]


class PrefillOrder(PrefillOrderAction):
    """Prefill an order ticket for user confirmation"""

    action_type: Literal["prefill_order"]


class OpenChart(OpenChartAction):
    """Open a chart for a symbol"""

    action_type: Literal["open_chart"]


class OpenScreener(OpenScreenerAction):
    """Open a stock screener with filters"""

    action_type: Literal["open_screener"]


class OpenEntitlementConsent(OpenEntitlementConsentAction):
    """Open entitlement consent flow"""

    action_type: Literal["open_entitlement_consent"]


StructuredAction: TypeAlias = Union[PrefillOrder, OpenChart, OpenScreener, OpenEntitlementConsent]
