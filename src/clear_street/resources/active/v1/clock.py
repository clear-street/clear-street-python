# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.active.v1.clock_get_clock_response import ClockGetClockResponse

__all__ = ["ClockResource", "AsyncClockResource"]


class ClockResource(SyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> ClockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ClockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ClockResourceWithStreamingResponse(self)

    def get_clock(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClockGetClockResponse:
        """Returns the current server time in UTC."""
        return self._get(
            "/active/v1/clock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClockGetClockResponse,
        )


class AsyncClockResource(AsyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> AsyncClockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncClockResourceWithStreamingResponse(self)

    async def get_clock(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClockGetClockResponse:
        """Returns the current server time in UTC."""
        return await self._get(
            "/active/v1/clock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClockGetClockResponse,
        )


class ClockResourceWithRawResponse:
    def __init__(self, clock: ClockResource) -> None:
        self._clock = clock

        self.get_clock = to_raw_response_wrapper(
            clock.get_clock,
        )


class AsyncClockResourceWithRawResponse:
    def __init__(self, clock: AsyncClockResource) -> None:
        self._clock = clock

        self.get_clock = async_to_raw_response_wrapper(
            clock.get_clock,
        )


class ClockResourceWithStreamingResponse:
    def __init__(self, clock: ClockResource) -> None:
        self._clock = clock

        self.get_clock = to_streamed_response_wrapper(
            clock.get_clock,
        )


class AsyncClockResourceWithStreamingResponse:
    def __init__(self, clock: AsyncClockResource) -> None:
        self._clock = clock

        self.get_clock = async_to_streamed_response_wrapper(
            clock.get_clock,
        )
