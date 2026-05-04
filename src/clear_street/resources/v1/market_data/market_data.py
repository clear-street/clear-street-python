# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .snapshot import (
    SnapshotResource,
    AsyncSnapshotResource,
    SnapshotResourceWithRawResponse,
    AsyncSnapshotResourceWithRawResponse,
    SnapshotResourceWithStreamingResponse,
    AsyncSnapshotResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .daily_summary import (
    DailySummaryResource,
    AsyncDailySummaryResource,
    DailySummaryResourceWithRawResponse,
    AsyncDailySummaryResourceWithRawResponse,
    DailySummaryResourceWithStreamingResponse,
    AsyncDailySummaryResourceWithStreamingResponse,
)

__all__ = ["MarketDataResource", "AsyncMarketDataResource"]


class MarketDataResource(SyncAPIResource):
    @cached_property
    def daily_summary(self) -> DailySummaryResource:
        """Real-time market data snapshots."""
        return DailySummaryResource(self._client)

    @cached_property
    def snapshot(self) -> SnapshotResource:
        """Real-time market data snapshots."""
        return SnapshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return MarketDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return MarketDataResourceWithStreamingResponse(self)


class AsyncMarketDataResource(AsyncAPIResource):
    @cached_property
    def daily_summary(self) -> AsyncDailySummaryResource:
        """Real-time market data snapshots."""
        return AsyncDailySummaryResource(self._client)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResource:
        """Real-time market data snapshots."""
        return AsyncSnapshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncMarketDataResourceWithStreamingResponse(self)


class MarketDataResourceWithRawResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def daily_summary(self) -> DailySummaryResourceWithRawResponse:
        """Real-time market data snapshots."""
        return DailySummaryResourceWithRawResponse(self._market_data.daily_summary)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithRawResponse:
        """Real-time market data snapshots."""
        return SnapshotResourceWithRawResponse(self._market_data.snapshot)


class AsyncMarketDataResourceWithRawResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def daily_summary(self) -> AsyncDailySummaryResourceWithRawResponse:
        """Real-time market data snapshots."""
        return AsyncDailySummaryResourceWithRawResponse(self._market_data.daily_summary)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithRawResponse:
        """Real-time market data snapshots."""
        return AsyncSnapshotResourceWithRawResponse(self._market_data.snapshot)


class MarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def daily_summary(self) -> DailySummaryResourceWithStreamingResponse:
        """Real-time market data snapshots."""
        return DailySummaryResourceWithStreamingResponse(self._market_data.daily_summary)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithStreamingResponse:
        """Real-time market data snapshots."""
        return SnapshotResourceWithStreamingResponse(self._market_data.snapshot)


class AsyncMarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def daily_summary(self) -> AsyncDailySummaryResourceWithStreamingResponse:
        """Real-time market data snapshots."""
        return AsyncDailySummaryResourceWithStreamingResponse(self._market_data.daily_summary)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithStreamingResponse:
        """Real-time market data snapshots."""
        return AsyncSnapshotResourceWithStreamingResponse(self._market_data.snapshot)
