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
from .....types.active.v1.market_data import daily_summary_get_daily_summaries_params
from .....types.active.v1.market_data.daily_summary_get_daily_summaries_response import (
    DailySummaryGetDailySummariesResponse,
)

__all__ = ["DailySummaryResource", "AsyncDailySummaryResource"]


class DailySummaryResource(SyncAPIResource):
    """Real-time market data snapshots."""

    @cached_property
    def with_raw_response(self) -> DailySummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return DailySummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DailySummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return DailySummaryResourceWithStreamingResponse(self)

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
    ) -> DailySummaryGetDailySummariesResponse:
        """
        Returns the most recent OHLV and current price for the requested OEMS
        instruments. Backed by the in-memory Polygon snapshot cache.

        Response contract: every request returns one row per **unique** `instrument_id`,
        in first-seen request order. Unresolvable IDs come back with `symbol = null` and
        every market-data field `null`; resolvable IDs with no cache entry come back
        with `symbol` populated but market-data fields `null`.

        **Note (temporary):** ID resolution currently goes through the supplemental
        screener (OEMS instrument_id → FMP fmp_symbol → metadata_id → realtime cache).
        Removed when the market-data service serves daily aggregates directly, or when
        Polygon symbology is loaded into the instrument cache.

        Args:
          instrument_ids: Comma-separated OEMS instrument UUIDs (required, 1..=100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/market-data/daily-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_ids": instrument_ids},
                    daily_summary_get_daily_summaries_params.DailySummaryGetDailySummariesParams,
                ),
            ),
            cast_to=DailySummaryGetDailySummariesResponse,
        )


class AsyncDailySummaryResource(AsyncAPIResource):
    """Real-time market data snapshots."""

    @cached_property
    def with_raw_response(self) -> AsyncDailySummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDailySummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDailySummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncDailySummaryResourceWithStreamingResponse(self)

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
    ) -> DailySummaryGetDailySummariesResponse:
        """
        Returns the most recent OHLV and current price for the requested OEMS
        instruments. Backed by the in-memory Polygon snapshot cache.

        Response contract: every request returns one row per **unique** `instrument_id`,
        in first-seen request order. Unresolvable IDs come back with `symbol = null` and
        every market-data field `null`; resolvable IDs with no cache entry come back
        with `symbol` populated but market-data fields `null`.

        **Note (temporary):** ID resolution currently goes through the supplemental
        screener (OEMS instrument_id → FMP fmp_symbol → metadata_id → realtime cache).
        Removed when the market-data service serves daily aggregates directly, or when
        Polygon symbology is loaded into the instrument cache.

        Args:
          instrument_ids: Comma-separated OEMS instrument UUIDs (required, 1..=100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/market-data/daily-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_ids": instrument_ids},
                    daily_summary_get_daily_summaries_params.DailySummaryGetDailySummariesParams,
                ),
            ),
            cast_to=DailySummaryGetDailySummariesResponse,
        )


class DailySummaryResourceWithRawResponse:
    def __init__(self, daily_summary: DailySummaryResource) -> None:
        self._daily_summary = daily_summary

        self.get_daily_summaries = to_raw_response_wrapper(
            daily_summary.get_daily_summaries,
        )


class AsyncDailySummaryResourceWithRawResponse:
    def __init__(self, daily_summary: AsyncDailySummaryResource) -> None:
        self._daily_summary = daily_summary

        self.get_daily_summaries = async_to_raw_response_wrapper(
            daily_summary.get_daily_summaries,
        )


class DailySummaryResourceWithStreamingResponse:
    def __init__(self, daily_summary: DailySummaryResource) -> None:
        self._daily_summary = daily_summary

        self.get_daily_summaries = to_streamed_response_wrapper(
            daily_summary.get_daily_summaries,
        )


class AsyncDailySummaryResourceWithStreamingResponse:
    def __init__(self, daily_summary: AsyncDailySummaryResource) -> None:
        self._daily_summary = daily_summary

        self.get_daily_summaries = async_to_streamed_response_wrapper(
            daily_summary.get_daily_summaries,
        )
