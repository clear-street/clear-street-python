# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .navigate_action import NavigateAction
from .content_part_text import ContentPartText
from .open_chart_action import OpenChartAction
from .content_part_chart import ContentPartChart
from .open_screener_action import OpenScreenerAction
from .prefill_order_action import PrefillOrderAction
from .content_part_thinking import ContentPartThinking
from .open_chat_window_action import OpenChatWindowAction
from .content_part_suggested_actions import ContentPartSuggestedActions

__all__ = [
    "ContentPart",
    "Text",
    "StructuredActionPrefillOrder",
    "StructuredActionOpenChart",
    "StructuredActionOpenScreener",
    "StructuredActionOpenChatWindow",
    "StructuredActionNavigate",
    "Thinking",
    "Chart",
    "SuggestedActions",
    "Type",
]


class Text(ContentPartText):
    """Plain text content"""

    type: Literal["text"]


class StructuredActionPrefillOrder(PrefillOrderAction):
    """Prefill an order ticket for user confirmation"""

    action_type: Literal["prefill_order"]

    type: Optional[Literal["structured_action"]] = None


class StructuredActionOpenChart(OpenChartAction):
    """Open a chart for a symbol"""

    action_type: Literal["open_chart"]

    type: Optional[Literal["structured_action"]] = None


class StructuredActionOpenScreener(OpenScreenerAction):
    """Open a stock screener with filters"""

    action_type: Literal["open_screener"]

    type: Optional[Literal["structured_action"]] = None


class StructuredActionOpenChatWindow(OpenChatWindowAction):
    """Open a chat window"""

    action_type: Literal["open_chat_window"]

    type: Optional[Literal["structured_action"]] = None


class StructuredActionNavigate(NavigateAction):
    """Navigate to a client route"""

    action_type: Literal["navigate"]

    type: Optional[Literal["structured_action"]] = None


class Thinking(ContentPartThinking):
    """Model reasoning/thinking content and tool call status indicators"""

    type: Literal["thinking"]


class Chart(ContentPartChart):
    """Typed inline chart (symbol or data-driven)"""

    type: Literal["chart"]


class SuggestedActions(ContentPartSuggestedActions):
    """Message-level follow-up action buttons"""

    type: Literal["suggested_actions"]


class Type(BaseModel):
    """Custom/extensible content"""

    type: Literal["custom"]


ContentPart: TypeAlias = Union[
    Text,
    Union[
        StructuredActionPrefillOrder,
        StructuredActionOpenChart,
        StructuredActionOpenScreener,
        StructuredActionOpenChatWindow,
        StructuredActionNavigate,
    ],
    Thinking,
    Chart,
    SuggestedActions,
    Type,
]
