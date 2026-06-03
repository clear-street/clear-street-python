# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..content_part_text_payload import ContentPartTextPayload
from ..content_part_chart_payload import ContentPartChartPayload
from ..content_part_custom_payload import ContentPartCustomPayload
from ..content_part_thinking_payload import ContentPartThinkingPayload
from ..content_part_structured_action_payload import ContentPartStructuredActionPayload
from ..content_part_suggested_actions_payload import ContentPartSuggestedActionsPayload

__all__ = [
    "ResponseContentPart",
    "ContentPartText",
    "ContentPartThinking",
    "ContentPartStructuredAction",
    "ContentPartChart",
    "ContentPartSuggestedActions",
    "ContentPartCustom",
]


class ContentPartText(ContentPartTextPayload):
    """Text content part."""

    type: Literal["text"]


class ContentPartThinking(ContentPartThinkingPayload):
    """Thinking content part shown on dynamic response polling."""

    type: Literal["thinking"]


class ContentPartStructuredAction(ContentPartStructuredActionPayload):
    """Structured action content part."""

    type: Literal["structured_action"]


class ContentPartChart(ContentPartChartPayload):
    """Chart payload content part."""

    type: Literal["chart"]


class ContentPartSuggestedActions(ContentPartSuggestedActionsPayload):
    """Suggested actions payload content part."""

    type: Literal["suggested_actions"]


class ContentPartCustom(ContentPartCustomPayload):
    """Escape-hatch custom payload content part."""

    type: Literal["custom"]


ResponseContentPart: TypeAlias = Union[
    ContentPartText,
    ContentPartThinking,
    ContentPartStructuredAction,
    ContentPartChart,
    ContentPartSuggestedActions,
    ContentPartCustom,
]
