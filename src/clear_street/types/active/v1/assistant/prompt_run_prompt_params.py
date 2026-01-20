# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PromptRunPromptParams"]


class PromptRunPromptParams(TypedDict, total=False):
    body: Required[object]
    """JSON payload forwarded to the prompt workflow."""

    slug: Required[str]
    """Unique slug identifying the prompt workflow to execute."""

    metadata: Dict[str, str]
