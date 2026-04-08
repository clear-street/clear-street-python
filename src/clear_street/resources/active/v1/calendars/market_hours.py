# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.active.v1.calendars import MarketType, market_hour_get_market_hours_calendar_params
from .....types.active.v1.calendars.market_type import MarketType
from .....types.active.v1.calendars.market_hour_get_market_hours_calendar_response import (
    MarketHourGetMarketHoursCalendarResponse,
)

__all__ = ["MarketHoursResource", "AsyncMarketHoursResource"]


class MarketHoursResource(SyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> MarketHoursResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return MarketHoursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketHoursResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return MarketHoursResourceWithStreamingResponse(self)

    def get_market_hours_calendar(
        self,
        *,
        date: str,
        market: MarketType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketHourGetMarketHoursCalendarResponse:
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
            "/active/v1/calendars/market-hours",
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
                    market_hour_get_market_hours_calendar_params.MarketHourGetMarketHoursCalendarParams,
                ),
            ),
            cast_to=MarketHourGetMarketHoursCalendarResponse,
        )


class AsyncMarketHoursResource(AsyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> AsyncMarketHoursResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketHoursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketHoursResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncMarketHoursResourceWithStreamingResponse(self)

    async def get_market_hours_calendar(
        self,
        *,
        date: str,
        market: MarketType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketHourGetMarketHoursCalendarResponse:
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
            "/active/v1/calendars/market-hours",
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
                    market_hour_get_market_hours_calendar_params.MarketHourGetMarketHoursCalendarParams,
                ),
            ),
            cast_to=MarketHourGetMarketHoursCalendarResponse,
        )


class MarketHoursResourceWithRawResponse:
    def __init__(self, market_hours: MarketHoursResource) -> None:
        self._market_hours = market_hours

        self.get_market_hours_calendar = to_raw_response_wrapper(
            market_hours.get_market_hours_calendar,
        )


class AsyncMarketHoursResourceWithRawResponse:
    def __init__(self, market_hours: AsyncMarketHoursResource) -> None:
        self._market_hours = market_hours

        self.get_market_hours_calendar = async_to_raw_response_wrapper(
            market_hours.get_market_hours_calendar,
        )


class MarketHoursResourceWithStreamingResponse:
    def __init__(self, market_hours: MarketHoursResource) -> None:
        self._market_hours = market_hours

        self.get_market_hours_calendar = to_streamed_response_wrapper(
            market_hours.get_market_hours_calendar,
        )


class AsyncMarketHoursResourceWithStreamingResponse:
    def __init__(self, market_hours: AsyncMarketHoursResource) -> None:
        self._market_hours = market_hours

        self.get_market_hours_calendar = async_to_streamed_response_wrapper(
            market_hours.get_market_hours_calendar,
        )
