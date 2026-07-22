# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.instrument_data import market_data_get_snapshots_params, market_data_get_daily_summaries_params
from ....types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ....types.v1.instrument_data.market_data_get_snapshots_response import MarketDataGetSnapshotsResponse
from ....types.v1.instrument_data.market_data_get_daily_summaries_response import MarketDataGetDailySummariesResponse

__all__ = ["MarketDataResource", "AsyncMarketDataResource"]


class MarketDataResource(SyncAPIResource):
    """Retrieve instrument analytics, market data, news, and related reference data."""

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

    def get_daily_summaries(
        self,
        *,
        instrument_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDataGetDailySummariesResponse:
        """
        Returns the most recent open, high, low, volume (OHLV) and current price for the
        requested instruments.

        Response contract: every request returns one row per **unique** `instrument_id`,
        in first-seen request order. Unresolvable IDs come back with `symbol = null` and
        every market-data field `null`; resolvable IDs with no available data come back
        with `symbol` populated but market-data fields `null`.

        Args:
          instrument_ids: Comma-separated instrument identifiers (required, 1..=100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/market-data/daily-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_ids": instrument_ids},
                    market_data_get_daily_summaries_params.MarketDataGetDailySummariesParams,
                ),
            ),
            cast_to=MarketDataGetDailySummariesResponse,
        )

    def get_snapshots(
        self,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDataGetSnapshotsResponse:
        """
        Get market data snapshots for one or more securities.

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/market-data/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_ids": instrument_ids}, market_data_get_snapshots_params.MarketDataGetSnapshotsParams
                ),
            ),
            cast_to=MarketDataGetSnapshotsResponse,
        )


class AsyncMarketDataResource(AsyncAPIResource):
    """Retrieve instrument analytics, market data, news, and related reference data."""

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

    async def get_daily_summaries(
        self,
        *,
        instrument_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDataGetDailySummariesResponse:
        """
        Returns the most recent open, high, low, volume (OHLV) and current price for the
        requested instruments.

        Response contract: every request returns one row per **unique** `instrument_id`,
        in first-seen request order. Unresolvable IDs come back with `symbol = null` and
        every market-data field `null`; resolvable IDs with no available data come back
        with `symbol` populated but market-data fields `null`.

        Args:
          instrument_ids: Comma-separated instrument identifiers (required, 1..=100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/market-data/daily-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_ids": instrument_ids},
                    market_data_get_daily_summaries_params.MarketDataGetDailySummariesParams,
                ),
            ),
            cast_to=MarketDataGetDailySummariesResponse,
        )

    async def get_snapshots(
        self,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDataGetSnapshotsResponse:
        """
        Get market data snapshots for one or more securities.

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/market-data/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_ids": instrument_ids}, market_data_get_snapshots_params.MarketDataGetSnapshotsParams
                ),
            ),
            cast_to=MarketDataGetSnapshotsResponse,
        )


class MarketDataResourceWithRawResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

        self.get_daily_summaries = to_raw_response_wrapper(
            market_data.get_daily_summaries,
        )
        self.get_snapshots = to_raw_response_wrapper(
            market_data.get_snapshots,
        )


class AsyncMarketDataResourceWithRawResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

        self.get_daily_summaries = async_to_raw_response_wrapper(
            market_data.get_daily_summaries,
        )
        self.get_snapshots = async_to_raw_response_wrapper(
            market_data.get_snapshots,
        )


class MarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

        self.get_daily_summaries = to_streamed_response_wrapper(
            market_data.get_daily_summaries,
        )
        self.get_snapshots = to_streamed_response_wrapper(
            market_data.get_snapshots,
        )


class AsyncMarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

        self.get_daily_summaries = async_to_streamed_response_wrapper(
            market_data.get_daily_summaries,
        )
        self.get_snapshots = async_to_streamed_response_wrapper(
            market_data.get_snapshots,
        )
