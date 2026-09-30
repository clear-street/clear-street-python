# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import calendar_get_market_hours_calendar_params, calendar_get_economic_events_calendar_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.calendar_get_clock_response import CalendarGetClockResponse
from ...types.v1.calendar_get_market_hours_calendar_response import CalendarGetMarketHoursCalendarResponse
from ...types.v1.calendar_get_economic_events_calendar_response import CalendarGetEconomicEventsCalendarResponse

__all__ = ["CalendarResource", "AsyncCalendarResource"]


class CalendarResource(SyncAPIResource):
    """Access clocks and financial calendars for market sessions and events."""

    @cached_property
    def with_raw_response(self) -> CalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return CalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return CalendarResourceWithStreamingResponse(self)

    def get_clock(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetClockResponse:
        """Returns the current server time in UTC."""
        return self._get(
            "/v1/clock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarGetClockResponse,
        )

    def get_economic_events_calendar(
        self,
        *,
        country: str | Omit = omit,
        impact: List[Literal["NONE", "LOW", "MEDIUM", "HIGH"]] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        timestamp: calendar_get_economic_events_calendar_params.Timestamp | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetEconomicEventsCalendarResponse:
        """Retrieves macroeconomic calendar events (e.g.

        CPI, jobs reports, central bank
        rate decisions), optionally filtered by country, impact, and event time range.

        Absent a `timestamp` lower bound, results default to events from the start of
        the previous trading day (America/New_York); absent an upper bound, results
        default through 7 days from today (America/New_York).

        Args:
          country: Comma-separated ISO 3166-1 alpha-2 country codes (or `EU`) to filter by.
              Defaults to `US` when omitted.

          impact: Comma-separated impact levels to filter by.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/calendars/economic-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "impact": impact,
                        "page_size": page_size,
                        "page_token": page_token,
                        "timestamp": timestamp,
                    },
                    calendar_get_economic_events_calendar_params.CalendarGetEconomicEventsCalendarParams,
                ),
            ),
            cast_to=CalendarGetEconomicEventsCalendarResponse,
        )

    def get_market_hours_calendar(
        self,
        *,
        date: str | Omit = omit,
        market: Literal["us_equities", "us_options"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetMarketHoursCalendarResponse:
        """
        Retrieves comprehensive trading hours including pre-market, regular, and
        after-hours sessions. Returns market status, session times, and next session
        schedules.

        Args:
          date: The date to query market hours for (YYYY-MM-DD). Defaults to today.

          market: Market type to query (us_equities, us_options). If omitted, returns all markets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/calendars/market-hours",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "market": market,
                    },
                    calendar_get_market_hours_calendar_params.CalendarGetMarketHoursCalendarParams,
                ),
            ),
            cast_to=CalendarGetMarketHoursCalendarResponse,
        )


class AsyncCalendarResource(AsyncAPIResource):
    """Access clocks and financial calendars for market sessions and events."""

    @cached_property
    def with_raw_response(self) -> AsyncCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncCalendarResourceWithStreamingResponse(self)

    async def get_clock(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetClockResponse:
        """Returns the current server time in UTC."""
        return await self._get(
            "/v1/clock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarGetClockResponse,
        )

    async def get_economic_events_calendar(
        self,
        *,
        country: str | Omit = omit,
        impact: List[Literal["NONE", "LOW", "MEDIUM", "HIGH"]] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        timestamp: calendar_get_economic_events_calendar_params.Timestamp | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetEconomicEventsCalendarResponse:
        """Retrieves macroeconomic calendar events (e.g.

        CPI, jobs reports, central bank
        rate decisions), optionally filtered by country, impact, and event time range.

        Absent a `timestamp` lower bound, results default to events from the start of
        the previous trading day (America/New_York); absent an upper bound, results
        default through 7 days from today (America/New_York).

        Args:
          country: Comma-separated ISO 3166-1 alpha-2 country codes (or `EU`) to filter by.
              Defaults to `US` when omitted.

          impact: Comma-separated impact levels to filter by.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/calendars/economic-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "impact": impact,
                        "page_size": page_size,
                        "page_token": page_token,
                        "timestamp": timestamp,
                    },
                    calendar_get_economic_events_calendar_params.CalendarGetEconomicEventsCalendarParams,
                ),
            ),
            cast_to=CalendarGetEconomicEventsCalendarResponse,
        )

    async def get_market_hours_calendar(
        self,
        *,
        date: str | Omit = omit,
        market: Literal["us_equities", "us_options"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarGetMarketHoursCalendarResponse:
        """
        Retrieves comprehensive trading hours including pre-market, regular, and
        after-hours sessions. Returns market status, session times, and next session
        schedules.

        Args:
          date: The date to query market hours for (YYYY-MM-DD). Defaults to today.

          market: Market type to query (us_equities, us_options). If omitted, returns all markets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/calendars/market-hours",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "market": market,
                    },
                    calendar_get_market_hours_calendar_params.CalendarGetMarketHoursCalendarParams,
                ),
            ),
            cast_to=CalendarGetMarketHoursCalendarResponse,
        )


class CalendarResourceWithRawResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.get_clock = to_raw_response_wrapper(
            calendar.get_clock,
        )
        self.get_economic_events_calendar = to_raw_response_wrapper(
            calendar.get_economic_events_calendar,
        )
        self.get_market_hours_calendar = to_raw_response_wrapper(
            calendar.get_market_hours_calendar,
        )


class AsyncCalendarResourceWithRawResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.get_clock = async_to_raw_response_wrapper(
            calendar.get_clock,
        )
        self.get_economic_events_calendar = async_to_raw_response_wrapper(
            calendar.get_economic_events_calendar,
        )
        self.get_market_hours_calendar = async_to_raw_response_wrapper(
            calendar.get_market_hours_calendar,
        )


class CalendarResourceWithStreamingResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.get_clock = to_streamed_response_wrapper(
            calendar.get_clock,
        )
        self.get_economic_events_calendar = to_streamed_response_wrapper(
            calendar.get_economic_events_calendar,
        )
        self.get_market_hours_calendar = to_streamed_response_wrapper(
            calendar.get_market_hours_calendar,
        )


class AsyncCalendarResourceWithStreamingResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.get_clock = async_to_streamed_response_wrapper(
            calendar.get_clock,
        )
        self.get_economic_events_calendar = async_to_streamed_response_wrapper(
            calendar.get_economic_events_calendar,
        )
        self.get_market_hours_calendar = async_to_streamed_response_wrapper(
            calendar.get_market_hours_calendar,
        )
