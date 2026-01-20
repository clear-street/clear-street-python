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
from .....types.active.v1.calendars import earning_get_earnings_calendar_params
from .....types.active.v1.calendars.earning_get_earnings_calendar_response import EarningGetEarningsCalendarResponse

__all__ = ["EarningsResource", "AsyncEarningsResource"]


class EarningsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return EarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return EarningsResourceWithStreamingResponse(self)

    def get_earnings_calendar(
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
    ) -> EarningGetEarningsCalendarResponse:
        """
        Retrieves upcoming earnings announcements.

        Args:
          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/calendars/earnings",
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
                    earning_get_earnings_calendar_params.EarningGetEarningsCalendarParams,
                ),
            ),
            cast_to=EarningGetEarningsCalendarResponse,
        )


class AsyncEarningsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncEarningsResourceWithStreamingResponse(self)

    async def get_earnings_calendar(
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
    ) -> EarningGetEarningsCalendarResponse:
        """
        Retrieves upcoming earnings announcements.

        Args:
          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/calendars/earnings",
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
                    earning_get_earnings_calendar_params.EarningGetEarningsCalendarParams,
                ),
            ),
            cast_to=EarningGetEarningsCalendarResponse,
        )


class EarningsResourceWithRawResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings_calendar = to_raw_response_wrapper(
            earnings.get_earnings_calendar,
        )


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings_calendar = async_to_raw_response_wrapper(
            earnings.get_earnings_calendar,
        )


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings_calendar = to_streamed_response_wrapper(
            earnings.get_earnings_calendar,
        )


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.get_earnings_calendar = async_to_streamed_response_wrapper(
            earnings.get_earnings_calendar,
        )
