# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.private_markets import offering_get_offerings_params, offering_get_offering_by_id_params
from ....types.v1.private_markets.offering_get_offerings_response import OfferingGetOfferingsResponse
from ....types.v1.private_markets.offering_get_offering_by_id_response import OfferingGetOfferingByIDResponse

__all__ = ["OfferingsResource", "AsyncOfferingsResource"]


class OfferingsResource(SyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def with_raw_response(self) -> OfferingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OfferingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OfferingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return OfferingsResourceWithStreamingResponse(self)

    def get_offering_by_id(
        self,
        offering_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferingGetOfferingByIDResponse:
        """
        Fetch one visible private-market offering with its documents, participants, and
        any attached SPV. Requires the account holder to have attested. Returns `404`
        when the offering does not exist or is not currently visible.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offering_id:
            raise ValueError(f"Expected a non-empty value for `offering_id` but received {offering_id!r}")
        return self._get(
            path_template("/v1/private-markets/offerings/{offering_id}", offering_id=offering_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, offering_get_offering_by_id_params.OfferingGetOfferingByIDParams
                ),
            ),
            cast_to=OfferingGetOfferingByIDResponse,
        )

    def get_offerings(
        self,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferingGetOfferingsResponse:
        """
        List every visible private-market offering as a card, with its derived class,
        company and SPV identity, and indicative terms. Requires the account holder to
        have attested.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/private-markets/offerings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, offering_get_offerings_params.OfferingGetOfferingsParams
                ),
            ),
            cast_to=OfferingGetOfferingsResponse,
        )


class AsyncOfferingsResource(AsyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOfferingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOfferingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOfferingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncOfferingsResourceWithStreamingResponse(self)

    async def get_offering_by_id(
        self,
        offering_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferingGetOfferingByIDResponse:
        """
        Fetch one visible private-market offering with its documents, participants, and
        any attached SPV. Requires the account holder to have attested. Returns `404`
        when the offering does not exist or is not currently visible.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offering_id:
            raise ValueError(f"Expected a non-empty value for `offering_id` but received {offering_id!r}")
        return await self._get(
            path_template("/v1/private-markets/offerings/{offering_id}", offering_id=offering_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, offering_get_offering_by_id_params.OfferingGetOfferingByIDParams
                ),
            ),
            cast_to=OfferingGetOfferingByIDResponse,
        )

    async def get_offerings(
        self,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferingGetOfferingsResponse:
        """
        List every visible private-market offering as a card, with its derived class,
        company and SPV identity, and indicative terms. Requires the account holder to
        have attested.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/private-markets/offerings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, offering_get_offerings_params.OfferingGetOfferingsParams
                ),
            ),
            cast_to=OfferingGetOfferingsResponse,
        )


class OfferingsResourceWithRawResponse:
    def __init__(self, offerings: OfferingsResource) -> None:
        self._offerings = offerings

        self.get_offering_by_id = to_raw_response_wrapper(
            offerings.get_offering_by_id,
        )
        self.get_offerings = to_raw_response_wrapper(
            offerings.get_offerings,
        )


class AsyncOfferingsResourceWithRawResponse:
    def __init__(self, offerings: AsyncOfferingsResource) -> None:
        self._offerings = offerings

        self.get_offering_by_id = async_to_raw_response_wrapper(
            offerings.get_offering_by_id,
        )
        self.get_offerings = async_to_raw_response_wrapper(
            offerings.get_offerings,
        )


class OfferingsResourceWithStreamingResponse:
    def __init__(self, offerings: OfferingsResource) -> None:
        self._offerings = offerings

        self.get_offering_by_id = to_streamed_response_wrapper(
            offerings.get_offering_by_id,
        )
        self.get_offerings = to_streamed_response_wrapper(
            offerings.get_offerings,
        )


class AsyncOfferingsResourceWithStreamingResponse:
    def __init__(self, offerings: AsyncOfferingsResource) -> None:
        self._offerings = offerings

        self.get_offering_by_id = async_to_streamed_response_wrapper(
            offerings.get_offering_by_id,
        )
        self.get_offerings = async_to_streamed_response_wrapper(
            offerings.get_offerings,
        )
