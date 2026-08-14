# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .offerings import (
    OfferingsResource,
    AsyncOfferingsResource,
    OfferingsResourceWithRawResponse,
    AsyncOfferingsResourceWithRawResponse,
    OfferingsResourceWithStreamingResponse,
    AsyncOfferingsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PrivateMarketsResource", "AsyncPrivateMarketsResource"]


class PrivateMarketsResource(SyncAPIResource):
    @cached_property
    def offerings(self) -> OfferingsResource:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrivateMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PrivateMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return PrivateMarketsResourceWithStreamingResponse(self)


class AsyncPrivateMarketsResource(AsyncAPIResource):
    @cached_property
    def offerings(self) -> AsyncOfferingsResource:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrivateMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncPrivateMarketsResourceWithStreamingResponse(self)


class PrivateMarketsResourceWithRawResponse:
    def __init__(self, private_markets: PrivateMarketsResource) -> None:
        self._private_markets = private_markets

    @cached_property
    def offerings(self) -> OfferingsResourceWithRawResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResourceWithRawResponse(self._private_markets.offerings)


class AsyncPrivateMarketsResourceWithRawResponse:
    def __init__(self, private_markets: AsyncPrivateMarketsResource) -> None:
        self._private_markets = private_markets

    @cached_property
    def offerings(self) -> AsyncOfferingsResourceWithRawResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResourceWithRawResponse(self._private_markets.offerings)


class PrivateMarketsResourceWithStreamingResponse:
    def __init__(self, private_markets: PrivateMarketsResource) -> None:
        self._private_markets = private_markets

    @cached_property
    def offerings(self) -> OfferingsResourceWithStreamingResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResourceWithStreamingResponse(self._private_markets.offerings)


class AsyncPrivateMarketsResourceWithStreamingResponse:
    def __init__(self, private_markets: AsyncPrivateMarketsResource) -> None:
        self._private_markets = private_markets

    @cached_property
    def offerings(self) -> AsyncOfferingsResourceWithStreamingResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResourceWithStreamingResponse(self._private_markets.offerings)
