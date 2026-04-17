# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from ..capability import Capability

__all__ = ["RunStartRunDeprecatedParams"]


class RunStartRunDeprecatedParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID for the request"""

    command_text: Required[str]
    """The user's natural language command"""

    capabilities: List[Capability]
    """Capabilities for structured actions"""

    thread_id: Optional[str]
    """Optional thread ID to continue an existing conversation"""

    thread_title: Optional[str]
    """Optional title for new threads"""
