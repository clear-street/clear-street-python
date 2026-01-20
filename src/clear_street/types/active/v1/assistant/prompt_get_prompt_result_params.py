# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PromptGetPromptResultParams"]


class PromptGetPromptResultParams(TypedDict, total=False):
    return_all_outputs: bool
    """When true, return intermediate outputs for all nodes in the workflow."""
