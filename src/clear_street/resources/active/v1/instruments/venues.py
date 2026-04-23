# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.instruments.venue_get_venues_response import VenueGetVenuesResponse

__all__ = ["VenuesResource", "AsyncVenuesResource"]


class VenuesResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> VenuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return VenuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VenuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return VenuesResourceWithStreamingResponse(self)

    def get_venues(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VenueGetVenuesResponse:
        """Retrieves a list of available trading venues and exchanges."""
        return self._get(
            "/active/v1/instruments/venues",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VenueGetVenuesResponse,
        )


class AsyncVenuesResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncVenuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVenuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVenuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncVenuesResourceWithStreamingResponse(self)

    async def get_venues(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VenueGetVenuesResponse:
        """Retrieves a list of available trading venues and exchanges."""
        return await self._get(
            "/active/v1/instruments/venues",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VenueGetVenuesResponse,
        )


class VenuesResourceWithRawResponse:
    def __init__(self, venues: VenuesResource) -> None:
        self._venues = venues

        self.get_venues = to_raw_response_wrapper(
            venues.get_venues,
        )


class AsyncVenuesResourceWithRawResponse:
    def __init__(self, venues: AsyncVenuesResource) -> None:
        self._venues = venues

        self.get_venues = async_to_raw_response_wrapper(
            venues.get_venues,
        )


class VenuesResourceWithStreamingResponse:
    def __init__(self, venues: VenuesResource) -> None:
        self._venues = venues

        self.get_venues = to_streamed_response_wrapper(
            venues.get_venues,
        )


class AsyncVenuesResourceWithStreamingResponse:
    def __init__(self, venues: AsyncVenuesResource) -> None:
        self._venues = venues

        self.get_venues = async_to_streamed_response_wrapper(
            venues.get_venues,
        )
