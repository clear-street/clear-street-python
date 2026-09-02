# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OfferingGetOfferingsParams"]


class OfferingGetOfferingsParams(TypedDict, total=False):
    account_id: Required[int]
    """
    Account whose account-holder entity must hold an accreditation attestation to
    browse private-market offerings.
    """
