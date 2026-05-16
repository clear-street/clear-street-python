# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThreadCreateMessageParams"]


class ThreadCreateMessageParams(TypedDict, total=False):
    account_id: Required[int]

    text: Required[str]

    capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
