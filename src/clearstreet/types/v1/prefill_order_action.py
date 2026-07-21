# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from . import prefill_new_order_action, prefill_cancel_order_action, prefill_modify_order_action

__all__ = ["PrefillOrderAction", "PrefillNewOrderAction", "PrefillCancelOrderAction", "PrefillModifyOrderAction"]


class PrefillNewOrderAction(prefill_new_order_action.PrefillNewOrderAction):
    """Create one or more new orders."""

    action_type: Literal["NEW"]


class PrefillCancelOrderAction(prefill_cancel_order_action.PrefillCancelOrderAction):
    """Cancel one or more existing orders."""

    action_type: Literal["CANCEL"]


class PrefillModifyOrderAction(prefill_modify_order_action.PrefillModifyOrderAction):
    """Modify one or more existing orders."""

    action_type: Literal["MODIFY"]


PrefillOrderAction: TypeAlias = Union[PrefillNewOrderAction, PrefillCancelOrderAction, PrefillModifyOrderAction]
