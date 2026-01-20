# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.calendars import dividend_get_dividends_calendar_params
from .....types.active.v1.calendars.dividend_get_dividends_calendar_response import DividendGetDividendsCalendarResponse

__all__ = ["DividendsResource", "AsyncDividendsResource"]


class DividendsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DividendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return DividendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DividendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return DividendsResourceWithStreamingResponse(self)

    def get_dividends_calendar(
        self,
        *,
        from_date: str,
        to_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DividendGetDividendsCalendarResponse:
        """
        Retrieves upcoming dividend payments.

        Args:
          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/calendars/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    dividend_get_dividends_calendar_params.DividendGetDividendsCalendarParams,
                ),
            ),
            cast_to=DividendGetDividendsCalendarResponse,
        )


class AsyncDividendsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDividendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDividendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDividendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncDividendsResourceWithStreamingResponse(self)

    async def get_dividends_calendar(
        self,
        *,
        from_date: str,
        to_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DividendGetDividendsCalendarResponse:
        """
        Retrieves upcoming dividend payments.

        Args:
          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/calendars/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    dividend_get_dividends_calendar_params.DividendGetDividendsCalendarParams,
                ),
            ),
            cast_to=DividendGetDividendsCalendarResponse,
        )


class DividendsResourceWithRawResponse:
    def __init__(self, dividends: DividendsResource) -> None:
        self._dividends = dividends

        self.get_dividends_calendar = to_raw_response_wrapper(
            dividends.get_dividends_calendar,
        )


class AsyncDividendsResourceWithRawResponse:
    def __init__(self, dividends: AsyncDividendsResource) -> None:
        self._dividends = dividends

        self.get_dividends_calendar = async_to_raw_response_wrapper(
            dividends.get_dividends_calendar,
        )


class DividendsResourceWithStreamingResponse:
    def __init__(self, dividends: DividendsResource) -> None:
        self._dividends = dividends

        self.get_dividends_calendar = to_streamed_response_wrapper(
            dividends.get_dividends_calendar,
        )


class AsyncDividendsResourceWithStreamingResponse:
    def __init__(self, dividends: AsyncDividendsResource) -> None:
        self._dividends = dividends

        self.get_dividends_calendar = async_to_streamed_response_wrapper(
            dividends.get_dividends_calendar,
        )
