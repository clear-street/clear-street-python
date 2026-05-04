# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstrumentSearchParams"]


class InstrumentSearchParams(TypedDict, total=False):
    q: Required[str]
    """
    Search term applied case-insensitively to ticker symbols, alt-IDs
    (CUSIP/ISIN/OPRA-root/CMS), and company names.
    """

    asset_class: str
    """Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER).

    Defaults to EQUITY.
    """

    country: str
    """Optional listing-country filter (e.g., US)."""

    currency: str
    """Optional ISO currency filter (e.g., USD)."""

    cursor: str
    """
    Opaque continuation cursor for show-more paging — pass the `next_page_token`
    from a prior response. Same wire format as `page_token` on other paginated
    endpoints.
    """

    include_inactive: bool
    """Include inactive instruments. Default false."""

    include_restricted: bool
    """Include restricted instruments. Default true (penalized in ranking)."""

    limit: int
    """Maximum hits to return. Bounded [1, 100]. Default 20."""
