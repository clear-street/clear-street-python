# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date

import httpx

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    InstrumentIDOrSymbol,
    instrument_data_get_instrument_events_params,
    instrument_data_get_all_instrument_events_params,
    instrument_data_get_instrument_analyst_consensus_params,
    instrument_data_get_instrument_income_statements_params,
    instrument_data_get_instrument_cash_flow_statements_params,
    instrument_data_get_instrument_balance_sheet_statements_params,
)
from .market_data import (
    MarketDataResource,
    AsyncMarketDataResource,
    MarketDataResourceWithRawResponse,
    AsyncMarketDataResourceWithRawResponse,
    MarketDataResourceWithStreamingResponse,
    AsyncMarketDataResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.all_events_event_type import AllEventsEventType
from ....types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ....types.v1.instrument_data_get_instrument_events_response import InstrumentDataGetInstrumentEventsResponse
from ....types.v1.instrument_data_get_all_instrument_events_response import InstrumentDataGetAllInstrumentEventsResponse
from ....types.v1.instrument_data_get_instrument_fundamentals_response import (
    InstrumentDataGetInstrumentFundamentalsResponse,
)
from ....types.v1.instrument_data_get_instrument_analyst_consensus_response import (
    InstrumentDataGetInstrumentAnalystConsensusResponse,
)
from ....types.v1.instrument_data_get_instrument_income_statements_response import (
    InstrumentDataGetInstrumentIncomeStatementsResponse,
)
from ....types.v1.instrument_data_get_instrument_cash_flow_statements_response import (
    InstrumentDataGetInstrumentCashFlowStatementsResponse,
)
from ....types.v1.instrument_data_get_instrument_balance_sheet_statements_response import (
    InstrumentDataGetInstrumentBalanceSheetStatementsResponse,
)

__all__ = ["InstrumentDataResource", "AsyncInstrumentDataResource"]


class InstrumentDataResource(SyncAPIResource):
    """Retrieve instrument analytics, market data, news, and related reference data."""

    @cached_property
    def market_data(self) -> MarketDataResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return MarketDataResource(self._client)

    @cached_property
    def news(self) -> NewsResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return NewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstrumentDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return InstrumentDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstrumentDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return InstrumentDataResourceWithStreamingResponse(self)

    def get_all_instrument_events(
        self,
        *,
        event_types: List[AllEventsEventType] | Omit = omit,
        from_date: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetAllInstrumentEventsResponse:
        """
        List instrument events across all securities.

        Retrieves all instrument events grouped by date.

        Args:
          event_types:
              Filter by event type(s). Comma-delimited list. Example:
              `event_types=EARNINGS,IPO`.

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          instrument_ids:
              Filter by instrument ID(s). Comma-delimited list of UUIDs. Example:
              `instrument_ids=550e8400-e29b-41d4-a716-446655440000`.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instruments/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_types": event_types,
                        "from_date": from_date,
                        "instrument_ids": instrument_ids,
                        "to_date": to_date,
                    },
                    instrument_data_get_all_instrument_events_params.InstrumentDataGetAllInstrumentEventsParams,
                ),
            ),
            cast_to=InstrumentDataGetAllInstrumentEventsResponse,
        )

    def get_instrument_analyst_consensus(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentAnalystConsensusResponse:
        """
        Retrieves analyst ratings and price targets for an instrument.

        Args:
          instrument_id: Instrument identifier

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/analyst-reporting", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    instrument_data_get_instrument_analyst_consensus_params.InstrumentDataGetInstrumentAnalystConsensusParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentAnalystConsensusResponse,
        )

    def get_instrument_balance_sheet_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentBalanceSheetStatementsResponse:
        """
        Get balance sheet statements for an instrument.

        Retrieves quarterly balance sheet statements for a specific instrument, sorted
        by fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/balance-sheets", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_balance_sheet_statements_params.InstrumentDataGetInstrumentBalanceSheetStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentBalanceSheetStatementsResponse,
        )

    def get_instrument_cash_flow_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentCashFlowStatementsResponse:
        """
        Get cash flow statements for an instrument.

        Retrieves historical cash flow statements for the specified instrument. Cash
        flow statements show cash inflows and outflows from operating, investing, and
        financing activities.

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/cash-flow-statements", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_cash_flow_statements_params.InstrumentDataGetInstrumentCashFlowStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentCashFlowStatementsResponse,
        )

    def get_instrument_events(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument, grouped
        by event type.

        Date range defaults:

        - `from_date`: today - 365 days
        - `to_date`: today + 60 days

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/events", instrument_id=instrument_id),
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
                    instrument_data_get_instrument_events_params.InstrumentDataGetInstrumentEventsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentEventsResponse,
        )

    def get_instrument_fundamentals(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentFundamentalsResponse:
        """
        Retrieves supplemental fundamentals and company profile data for an instrument.

        Args:
          instrument_id: Instrument identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/fundamentals", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentDataGetInstrumentFundamentalsResponse,
        )

    def get_instrument_income_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentIncomeStatementsResponse:
        """
        Retrieves quarterly income statements for a specific instrument, sorted by
        fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/income-statements", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_income_statements_params.InstrumentDataGetInstrumentIncomeStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentIncomeStatementsResponse,
        )


class AsyncInstrumentDataResource(AsyncAPIResource):
    """Retrieve instrument analytics, market data, news, and related reference data."""

    @cached_property
    def market_data(self) -> AsyncMarketDataResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncMarketDataResource(self._client)

    @cached_property
    def news(self) -> AsyncNewsResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncNewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstrumentDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstrumentDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstrumentDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncInstrumentDataResourceWithStreamingResponse(self)

    async def get_all_instrument_events(
        self,
        *,
        event_types: List[AllEventsEventType] | Omit = omit,
        from_date: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetAllInstrumentEventsResponse:
        """
        List instrument events across all securities.

        Retrieves all instrument events grouped by date.

        Args:
          event_types:
              Filter by event type(s). Comma-delimited list. Example:
              `event_types=EARNINGS,IPO`.

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          instrument_ids:
              Filter by instrument ID(s). Comma-delimited list of UUIDs. Example:
              `instrument_ids=550e8400-e29b-41d4-a716-446655440000`.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instruments/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_types": event_types,
                        "from_date": from_date,
                        "instrument_ids": instrument_ids,
                        "to_date": to_date,
                    },
                    instrument_data_get_all_instrument_events_params.InstrumentDataGetAllInstrumentEventsParams,
                ),
            ),
            cast_to=InstrumentDataGetAllInstrumentEventsResponse,
        )

    async def get_instrument_analyst_consensus(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentAnalystConsensusResponse:
        """
        Retrieves analyst ratings and price targets for an instrument.

        Args:
          instrument_id: Instrument identifier

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/analyst-reporting", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    instrument_data_get_instrument_analyst_consensus_params.InstrumentDataGetInstrumentAnalystConsensusParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentAnalystConsensusResponse,
        )

    async def get_instrument_balance_sheet_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentBalanceSheetStatementsResponse:
        """
        Get balance sheet statements for an instrument.

        Retrieves quarterly balance sheet statements for a specific instrument, sorted
        by fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/balance-sheets", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_balance_sheet_statements_params.InstrumentDataGetInstrumentBalanceSheetStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentBalanceSheetStatementsResponse,
        )

    async def get_instrument_cash_flow_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentCashFlowStatementsResponse:
        """
        Get cash flow statements for an instrument.

        Retrieves historical cash flow statements for the specified instrument. Cash
        flow statements show cash inflows and outflows from operating, investing, and
        financing activities.

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/cash-flow-statements", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_cash_flow_statements_params.InstrumentDataGetInstrumentCashFlowStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentCashFlowStatementsResponse,
        )

    async def get_instrument_events(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument, grouped
        by event type.

        Date range defaults:

        - `from_date`: today - 365 days
        - `to_date`: today + 60 days

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/events", instrument_id=instrument_id),
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
                    instrument_data_get_instrument_events_params.InstrumentDataGetInstrumentEventsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentEventsResponse,
        )

    async def get_instrument_fundamentals(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentFundamentalsResponse:
        """
        Retrieves supplemental fundamentals and company profile data for an instrument.

        Args:
          instrument_id: Instrument identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/fundamentals", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentDataGetInstrumentFundamentalsResponse,
        )

    async def get_instrument_income_statements(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_date: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentDataGetInstrumentIncomeStatementsResponse:
        """
        Retrieves quarterly income statements for a specific instrument, sorted by
        fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: Instrument identifier

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/income-statements", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to_date": to_date,
                    },
                    instrument_data_get_instrument_income_statements_params.InstrumentDataGetInstrumentIncomeStatementsParams,
                ),
            ),
            cast_to=InstrumentDataGetInstrumentIncomeStatementsResponse,
        )


class InstrumentDataResourceWithRawResponse:
    def __init__(self, instrument_data: InstrumentDataResource) -> None:
        self._instrument_data = instrument_data

        self.get_all_instrument_events = to_raw_response_wrapper(
            instrument_data.get_all_instrument_events,
        )
        self.get_instrument_analyst_consensus = to_raw_response_wrapper(
            instrument_data.get_instrument_analyst_consensus,
        )
        self.get_instrument_balance_sheet_statements = to_raw_response_wrapper(
            instrument_data.get_instrument_balance_sheet_statements,
        )
        self.get_instrument_cash_flow_statements = to_raw_response_wrapper(
            instrument_data.get_instrument_cash_flow_statements,
        )
        self.get_instrument_events = to_raw_response_wrapper(
            instrument_data.get_instrument_events,
        )
        self.get_instrument_fundamentals = to_raw_response_wrapper(
            instrument_data.get_instrument_fundamentals,
        )
        self.get_instrument_income_statements = to_raw_response_wrapper(
            instrument_data.get_instrument_income_statements,
        )

    @cached_property
    def market_data(self) -> MarketDataResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return MarketDataResourceWithRawResponse(self._instrument_data.market_data)

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return NewsResourceWithRawResponse(self._instrument_data.news)


class AsyncInstrumentDataResourceWithRawResponse:
    def __init__(self, instrument_data: AsyncInstrumentDataResource) -> None:
        self._instrument_data = instrument_data

        self.get_all_instrument_events = async_to_raw_response_wrapper(
            instrument_data.get_all_instrument_events,
        )
        self.get_instrument_analyst_consensus = async_to_raw_response_wrapper(
            instrument_data.get_instrument_analyst_consensus,
        )
        self.get_instrument_balance_sheet_statements = async_to_raw_response_wrapper(
            instrument_data.get_instrument_balance_sheet_statements,
        )
        self.get_instrument_cash_flow_statements = async_to_raw_response_wrapper(
            instrument_data.get_instrument_cash_flow_statements,
        )
        self.get_instrument_events = async_to_raw_response_wrapper(
            instrument_data.get_instrument_events,
        )
        self.get_instrument_fundamentals = async_to_raw_response_wrapper(
            instrument_data.get_instrument_fundamentals,
        )
        self.get_instrument_income_statements = async_to_raw_response_wrapper(
            instrument_data.get_instrument_income_statements,
        )

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncMarketDataResourceWithRawResponse(self._instrument_data.market_data)

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncNewsResourceWithRawResponse(self._instrument_data.news)


class InstrumentDataResourceWithStreamingResponse:
    def __init__(self, instrument_data: InstrumentDataResource) -> None:
        self._instrument_data = instrument_data

        self.get_all_instrument_events = to_streamed_response_wrapper(
            instrument_data.get_all_instrument_events,
        )
        self.get_instrument_analyst_consensus = to_streamed_response_wrapper(
            instrument_data.get_instrument_analyst_consensus,
        )
        self.get_instrument_balance_sheet_statements = to_streamed_response_wrapper(
            instrument_data.get_instrument_balance_sheet_statements,
        )
        self.get_instrument_cash_flow_statements = to_streamed_response_wrapper(
            instrument_data.get_instrument_cash_flow_statements,
        )
        self.get_instrument_events = to_streamed_response_wrapper(
            instrument_data.get_instrument_events,
        )
        self.get_instrument_fundamentals = to_streamed_response_wrapper(
            instrument_data.get_instrument_fundamentals,
        )
        self.get_instrument_income_statements = to_streamed_response_wrapper(
            instrument_data.get_instrument_income_statements,
        )

    @cached_property
    def market_data(self) -> MarketDataResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return MarketDataResourceWithStreamingResponse(self._instrument_data.market_data)

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return NewsResourceWithStreamingResponse(self._instrument_data.news)


class AsyncInstrumentDataResourceWithStreamingResponse:
    def __init__(self, instrument_data: AsyncInstrumentDataResource) -> None:
        self._instrument_data = instrument_data

        self.get_all_instrument_events = async_to_streamed_response_wrapper(
            instrument_data.get_all_instrument_events,
        )
        self.get_instrument_analyst_consensus = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_analyst_consensus,
        )
        self.get_instrument_balance_sheet_statements = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_balance_sheet_statements,
        )
        self.get_instrument_cash_flow_statements = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_cash_flow_statements,
        )
        self.get_instrument_events = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_events,
        )
        self.get_instrument_fundamentals = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_fundamentals,
        )
        self.get_instrument_income_statements = async_to_streamed_response_wrapper(
            instrument_data.get_instrument_income_statements,
        )

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncMarketDataResourceWithStreamingResponse(self._instrument_data.market_data)

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncNewsResourceWithStreamingResponse(self._instrument_data.news)
