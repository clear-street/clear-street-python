# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .market_hours import (
    MarketHoursResource,
    AsyncMarketHoursResource,
    MarketHoursResourceWithRawResponse,
    AsyncMarketHoursResourceWithRawResponse,
    MarketHoursResourceWithStreamingResponse,
    AsyncMarketHoursResourceWithStreamingResponse,
)

__all__ = ["CalendarsResource", "AsyncCalendarsResource"]


class CalendarsResource(SyncAPIResource):
    @cached_property
    def market_hours(self) -> MarketHoursResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return CalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return CalendarsResourceWithStreamingResponse(self)


class AsyncCalendarsResource(AsyncAPIResource):
    @cached_property
    def market_hours(self) -> AsyncMarketHoursResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncCalendarsResourceWithStreamingResponse(self)


class CalendarsResourceWithRawResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResourceWithRawResponse(self._calendars.market_hours)


class AsyncCalendarsResourceWithRawResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResourceWithRawResponse(self._calendars.market_hours)


class CalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResourceWithStreamingResponse(self._calendars.market_hours)


class AsyncCalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResourceWithStreamingResponse(self._calendars.market_hours)
