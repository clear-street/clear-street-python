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
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
]


class UnionMember0(ContentPartTextPayload):
    """Text content part."""

    type: Literal["text"]


class UnionMember1(ContentPartThinkingPayload):
    """Thinking content part shown on dynamic response polling."""

    type: Literal["thinking"]


class UnionMember2(ContentPartStructuredActionPayload):
    """Structured action content part."""

    type: Literal["structured_action"]


class UnionMember3(ContentPartChartPayload):
    """Chart payload content part."""

    type: Literal["chart"]


class UnionMember4(ContentPartSuggestedActionsPayload):
    """Suggested actions payload content part."""

    type: Literal["suggested_actions"]


class UnionMember5(ContentPartCustomPayload):
    """Escape-hatch custom payload content part."""

    type: Literal["custom"]


ResponseContentPart: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5
]
