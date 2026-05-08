# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .entitlement_code import EntitlementCode

__all__ = ["EntitlementCreateEntitlementsParams"]


class EntitlementCreateEntitlementsParams(TypedDict, total=False):
    agreement_id: Required[str]

    requested_entitlement_codes: Required[List[EntitlementCode]]

    trading_account_ids: Required[Iterable[int]]
