# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import (
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
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    instrument_get_instruments_params,
    instrument_search_instruments_params,
    instrument_get_instrument_by_id_params,
    instrument_get_option_contracts_params,
    instrument_get_prediction_events_params,
    instrument_get_prediction_series_params,
    instrument_get_prediction_markets_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.instrument_get_instruments_response import InstrumentGetInstrumentsResponse
from ...types.v1.instrument_search_instruments_response import InstrumentSearchInstrumentsResponse
from ...types.v1.instrument_get_instrument_by_id_response import InstrumentGetInstrumentByIDResponse
from ...types.v1.instrument_get_option_contracts_response import InstrumentGetOptionContractsResponse
from ...types.v1.instrument_get_prediction_events_response import InstrumentGetPredictionEventsResponse
from ...types.v1.instrument_get_prediction_series_response import InstrumentGetPredictionSeriesResponse
from ...types.v1.instrument_get_prediction_markets_response import InstrumentGetPredictionMarketsResponse
from ...types.v1.instrument_get_prediction_categories_response import InstrumentGetPredictionCategoriesResponse

__all__ = ["InstrumentsResource", "AsyncInstrumentsResource"]


class InstrumentsResource(SyncAPIResource):
    """Retrieve core details and discovery endpoints for tradable instruments."""

    @cached_property
    def with_raw_response(self) -> InstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return InstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return InstrumentsResourceWithStreamingResponse(self)

    def get_instrument_by_id(
        self,
        instrument_id: str,
        *,
        include_options_expiry_dates: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentByIDResponse:
        """
        Retrieves detailed information for a specific instrument.

        Args:
          instrument_id: Instrument identifier: either an instrument UUID or a symbol (symbol for
              equities, OSI for options). Non-UUID inputs are resolved server-side.

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_options_expiry_dates": include_options_expiry_dates},
                    instrument_get_instrument_by_id_params.InstrumentGetInstrumentByIDParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentByIDResponse,
        )

    def get_instruments(
        self,
        *,
        easy_to_borrow: bool | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "INDEX", "OPTION", "CASH", "EVENT_CONTRACT"] | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_ptp: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentsResponse:
        """
        Retrieves a list of tradeable instruments.

        Args:
          easy_to_borrow: Filter by easy to borrow status

          instrument_ids: Comma-separated instrument identifiers: unique identifiers or symbols (symbol
              for equities, OSI for options)

          instrument_type: Filter by instrument type (e.g. COMMON_STOCK, OPTION)

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_ptp: Filter by publicly traded partnership (PTP) status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

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
            "/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_ptp": is_ptp,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )

    def get_option_contracts(
        self,
        *,
        contract_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        contract_type: Literal["CALL", "PUT"] | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        is_settle_on_open: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        root: str | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts with options-specific metadata. Exactly one identifier
        must be provided: `root`/`underlying_instrument_id` (list all contracts for that
        underlier) or `contract_ids` (look up specific contracts directly).
        `expiry`/`contract_type` apply as filters in either case.

        Args:
          contract_ids: Comma-separated contract instrument IDs (UUID) or OSI option symbols to look up
              directly, bypassing underlier expansion. Mutually exclusive with
              root/underlying_instrument_id; up to 100 values.

          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          is_settle_on_open: Filter by settlement cycle: true for early-settling (AM, settle-on-open)
              contracts, false for normal (PM) contracts. Omit to return both.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          root: OSI option root symbol (e.g., AAPL, SPXW). Index roots also include their weekly
              series (e.g., SPX includes SPXW).

          underlier: Deprecated: use `root`. If both are sent, the values must match.

          underlying_instrument_id: Instrument identifier or symbol of the underlying equity/index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instruments/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contract_ids": contract_ids,
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "is_settle_on_open": is_settle_on_open,
                        "page_size": page_size,
                        "page_token": page_token,
                        "root": root,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    instrument_get_option_contracts_params.InstrumentGetOptionContractsParams,
                ),
            ),
            cast_to=InstrumentGetOptionContractsResponse,
        )

    def get_prediction_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionCategoriesResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the distinct categories, sorted alphabetically, of every prediction market
        contract that can currently be listed: contracts that are initialized or active
        and have not yet closed.

        The list refreshes every 15 minutes. Returns `503` until the categories first
        load after a restart.
        """
        return self._get(
            "/v1/instruments/predictions/categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentGetPredictionCategoriesResponse,
        )

    def get_prediction_events(
        self,
        *,
        categories: str | Omit = omit,
        close_at: instrument_get_prediction_events_params.CloseAt | Omit = omit,
        include_markets: bool | Omit = omit,
        include_settled: bool | Omit = omit,
        market_ids: str | Omit = omit,
        open_at: instrument_get_prediction_events_params.OpenAt | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        search: str | Omit = omit,
        series_codes: str | Omit = omit,
        sort_by: Literal["OPEN_AT", "CLOSE_AT"] | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionEventsResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the prediction market events that have at least one market that can
        currently be listed: initialized or active and not yet closed. A market that is
        paused does not count, so an event whose markets are all paused is not listed.

        Events are ordered by code unless `sort_by` names another key or `search` is
        set; ties break on code ascending. `series_codes` and `categories` keep events
        of those series or with a listable market in those categories, ignoring case.

        `search` keeps events whose code, series code, or a market's question or title
        contains every word of the text. Words match by prefix and English stem,
        ignoring case and punctuation; text with no searchable word, such as `the`,
        matches nothing. A word of four or more letters that matches nothing is replaced
        by up to three close spellings. Without `sort_by`, the best match comes first,
        closest spellings first. Search covers listable events unless
        `include_settled=true`.

        With `include_settled=true`, settled and expired events are listed too: every
        market counts as listable for `categories`, `title`, `open_at.*`, `close_at.*`,
        `search`, and `sort_by`. Such a request that takes longer than 30 seconds fails
        with `504`; narrow `search` or the filters and try again.

        `open_at.*` and `close_at.*` bound an event's open and close time, which are the
        earliest across its listable markets, and `sort_by` uses the same times.

        An event's `title` is the question of its first listable market by symbol, and
        its `categories` are those of its listable markets.

        With `include_markets=true`, each event carries `markets`: a summary of every
        market of the event, ordered by symbol, in any status. This includes paused
        markets of a listed event and settled markets. Pages carry no totals: follow
        `next_page_token` until it is absent.

        `market_ids` (1-100 market ids or tickers, in any status) keeps the events those
        markets belong to, each once, and the other filters still apply. Ids that match
        no market are reported: `207` with the events found and the missing ids in
        `error.details`, or `404` when none matched.

        Args:
          categories: Comma-separated categories. Keeps events with a listable market in any of them,
              ignoring case.

          include_markets: Embed a summary of every market of each event, in any status. Default false.

          include_settled: Also list settled and expired events, not only events with a listable market.
              Every market then counts as listable for the other filters, `title`,
              `categories`, and the open and close times. Default false. A request that takes
              longer than 30 seconds fails with `504`; narrow `search` or the filters and try
              again.

          market_ids: Comma-separated market ids (UUID) or tickers, 1-100. Keeps events of those
              markets, in any status; the other filters still apply. Ids that match no market
              are reported: `207`, or `404` when none match.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          search: Keeps events whose code, series code, or a market's question or title contains
              every word, matched by prefix and English stem, ignoring case. Searches listable
              events, or every event with `include_settled`. A word of four or more letters
              that matches nothing is replaced by up to three close spellings. Without
              `sort_by`, orders by relevance, closest spellings first.

          series_codes: Comma-separated series codes. Keeps events of those series, ignoring case.

          sort_by: Sort key. Defaults to relevance when `search` is set, else the event code. Ties
              break on event code ascending.

          sort_direction: Sort direction. Defaults to ascending. Ignored when sorting by relevance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instruments/predictions/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "categories": categories,
                        "close_at": close_at,
                        "include_markets": include_markets,
                        "include_settled": include_settled,
                        "market_ids": market_ids,
                        "open_at": open_at,
                        "page_size": page_size,
                        "page_token": page_token,
                        "search": search,
                        "series_codes": series_codes,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    instrument_get_prediction_events_params.InstrumentGetPredictionEventsParams,
                ),
            ),
            cast_to=InstrumentGetPredictionEventsResponse,
        )

    def get_prediction_markets(
        self,
        *,
        event_code: str | Omit = omit,
        market_ids: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        statuses: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionMarketsResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Looks up prediction markets in any status, by `market_ids` (1-100 market ids or
        tickers) or by `event_code`. Exactly one of the two is required. Markets are
        ordered by symbol.

        `statuses` keeps markets in any listed status. It defaults to `OPEN` with
        `event_code` and to every status with `market_ids`.

        With `event_code`, pages carry no totals: follow `next_page_token` until it is
        absent. `market_ids` lookups are not paginated and ignore page parameters.

        With `market_ids`, ids that match no market are reported: `207` with the markets
        found and the missing ids in `error.details`, or `404` when none matched. A
        market removed only by `statuses` is not reported as missing.

        Each market trades one YES-denominated instrument; there is no NO instrument.
        Prices, including those from `/market-data/snapshot`, are YES prices in dollars,
        and `no_price = 1 - yes_price`. A negative position quantity is NO exposure.

        Args:
          event_code: Event code; returns the markets of the event. Mutually exclusive with
              `market_ids`.

          market_ids: Comma-separated market ids (UUID) or tickers, 1-100, in any status. Mutually
              exclusive with `event_code`.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          statuses: Comma-separated statuses to keep: `OPEN`, `UNOPENED`, `PAUSED`, `CLOSED`,
              `SETTLED`. Defaults to `OPEN` with `event_code` and to every status with
              `market_ids`. Unrecognized values are ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instruments/predictions/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_code": event_code,
                        "market_ids": market_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "statuses": statuses,
                    },
                    instrument_get_prediction_markets_params.InstrumentGetPredictionMarketsParams,
                ),
            ),
            cast_to=InstrumentGetPredictionMarketsResponse,
        )

    def get_prediction_series(
        self,
        *,
        categories: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionSeriesResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the distinct series codes of prediction markets that can currently be
        listed: markets that are initialized or active and have not yet closed. Series
        are ordered by code.

        `categories` keeps series with a market in any listed category, ignoring case.
        Pages carry no totals: follow `next_page_token` until it is absent.

        Args:
          categories: Comma-separated categories. Keeps series with a market in any of them, ignoring
              case.

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
            "/v1/instruments/predictions/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "categories": categories,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_get_prediction_series_params.InstrumentGetPredictionSeriesParams,
                ),
            ),
            cast_to=InstrumentGetPredictionSeriesResponse,
        )

    def search_instruments(
        self,
        *,
        q: str,
        asset_class: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        include_inactive: bool | Omit = omit,
        include_ptp: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentSearchInstrumentsResponse:
        """
        Search instruments by symbol, alternate identifier, or company name.

        The `q` parameter is case-insensitive and supports ticker symbols, alternate
        identifiers such as CUSIP, ISIN, and OPRA root, and company names for non-option
        instruments. Results are ranked by match quality plus instrument quality signals
        and relevance. Defaults to the `EQUITY` asset class (common stocks, preferred
        shares, ADRs, ETFs, and exchange-traded mutual funds). Pass `asset_class=OPTION`
        to search option contracts: by full OSI symbol, by an OSI prefix (root +
        `YYMMDD` expiry, e.g. `AAPL 261217`), or by a root-scoped phrase such as
        `AAPL Dec 250 call`.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alternate identifiers
              (CUSIP, ISIN, OPRA root), and company names for non-option instruments. Option
              searches match symbols and alternate identifiers.

          asset_class: Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER). Defaults to
              EQUITY.

          country: Optional listing-country filter (e.g., US).

          currency: Optional ISO currency filter (e.g., USD).

          include_inactive: Include inactive instruments. Default false.

          include_ptp: Include publicly traded partnership (PTP) instruments. Default true (penalized
              in ranking).

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
            "/v1/instruments/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "asset_class": asset_class,
                        "country": country,
                        "currency": currency,
                        "include_inactive": include_inactive,
                        "include_ptp": include_ptp,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_search_instruments_params.InstrumentSearchInstrumentsParams,
                ),
            ),
            cast_to=InstrumentSearchInstrumentsResponse,
        )


class AsyncInstrumentsResource(AsyncAPIResource):
    """Retrieve core details and discovery endpoints for tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncInstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncInstrumentsResourceWithStreamingResponse(self)

    async def get_instrument_by_id(
        self,
        instrument_id: str,
        *,
        include_options_expiry_dates: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentByIDResponse:
        """
        Retrieves detailed information for a specific instrument.

        Args:
          instrument_id: Instrument identifier: either an instrument UUID or a symbol (symbol for
              equities, OSI for options). Non-UUID inputs are resolved server-side.

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_options_expiry_dates": include_options_expiry_dates},
                    instrument_get_instrument_by_id_params.InstrumentGetInstrumentByIDParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentByIDResponse,
        )

    async def get_instruments(
        self,
        *,
        easy_to_borrow: bool | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "INDEX", "OPTION", "CASH", "EVENT_CONTRACT"] | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_ptp: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentsResponse:
        """
        Retrieves a list of tradeable instruments.

        Args:
          easy_to_borrow: Filter by easy to borrow status

          instrument_ids: Comma-separated instrument identifiers: unique identifiers or symbols (symbol
              for equities, OSI for options)

          instrument_type: Filter by instrument type (e.g. COMMON_STOCK, OPTION)

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_ptp: Filter by publicly traded partnership (PTP) status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

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
            "/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_ptp": is_ptp,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )

    async def get_option_contracts(
        self,
        *,
        contract_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        contract_type: Literal["CALL", "PUT"] | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        is_settle_on_open: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        root: str | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts with options-specific metadata. Exactly one identifier
        must be provided: `root`/`underlying_instrument_id` (list all contracts for that
        underlier) or `contract_ids` (look up specific contracts directly).
        `expiry`/`contract_type` apply as filters in either case.

        Args:
          contract_ids: Comma-separated contract instrument IDs (UUID) or OSI option symbols to look up
              directly, bypassing underlier expansion. Mutually exclusive with
              root/underlying_instrument_id; up to 100 values.

          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          is_settle_on_open: Filter by settlement cycle: true for early-settling (AM, settle-on-open)
              contracts, false for normal (PM) contracts. Omit to return both.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          root: OSI option root symbol (e.g., AAPL, SPXW). Index roots also include their weekly
              series (e.g., SPX includes SPXW).

          underlier: Deprecated: use `root`. If both are sent, the values must match.

          underlying_instrument_id: Instrument identifier or symbol of the underlying equity/index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instruments/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contract_ids": contract_ids,
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "is_settle_on_open": is_settle_on_open,
                        "page_size": page_size,
                        "page_token": page_token,
                        "root": root,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    instrument_get_option_contracts_params.InstrumentGetOptionContractsParams,
                ),
            ),
            cast_to=InstrumentGetOptionContractsResponse,
        )

    async def get_prediction_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionCategoriesResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the distinct categories, sorted alphabetically, of every prediction market
        contract that can currently be listed: contracts that are initialized or active
        and have not yet closed.

        The list refreshes every 15 minutes. Returns `503` until the categories first
        load after a restart.
        """
        return await self._get(
            "/v1/instruments/predictions/categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentGetPredictionCategoriesResponse,
        )

    async def get_prediction_events(
        self,
        *,
        categories: str | Omit = omit,
        close_at: instrument_get_prediction_events_params.CloseAt | Omit = omit,
        include_markets: bool | Omit = omit,
        include_settled: bool | Omit = omit,
        market_ids: str | Omit = omit,
        open_at: instrument_get_prediction_events_params.OpenAt | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        search: str | Omit = omit,
        series_codes: str | Omit = omit,
        sort_by: Literal["OPEN_AT", "CLOSE_AT"] | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionEventsResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the prediction market events that have at least one market that can
        currently be listed: initialized or active and not yet closed. A market that is
        paused does not count, so an event whose markets are all paused is not listed.

        Events are ordered by code unless `sort_by` names another key or `search` is
        set; ties break on code ascending. `series_codes` and `categories` keep events
        of those series or with a listable market in those categories, ignoring case.

        `search` keeps events whose code, series code, or a market's question or title
        contains every word of the text. Words match by prefix and English stem,
        ignoring case and punctuation; text with no searchable word, such as `the`,
        matches nothing. A word of four or more letters that matches nothing is replaced
        by up to three close spellings. Without `sort_by`, the best match comes first,
        closest spellings first. Search covers listable events unless
        `include_settled=true`.

        With `include_settled=true`, settled and expired events are listed too: every
        market counts as listable for `categories`, `title`, `open_at.*`, `close_at.*`,
        `search`, and `sort_by`. Such a request that takes longer than 30 seconds fails
        with `504`; narrow `search` or the filters and try again.

        `open_at.*` and `close_at.*` bound an event's open and close time, which are the
        earliest across its listable markets, and `sort_by` uses the same times.

        An event's `title` is the question of its first listable market by symbol, and
        its `categories` are those of its listable markets.

        With `include_markets=true`, each event carries `markets`: a summary of every
        market of the event, ordered by symbol, in any status. This includes paused
        markets of a listed event and settled markets. Pages carry no totals: follow
        `next_page_token` until it is absent.

        `market_ids` (1-100 market ids or tickers, in any status) keeps the events those
        markets belong to, each once, and the other filters still apply. Ids that match
        no market are reported: `207` with the events found and the missing ids in
        `error.details`, or `404` when none matched.

        Args:
          categories: Comma-separated categories. Keeps events with a listable market in any of them,
              ignoring case.

          include_markets: Embed a summary of every market of each event, in any status. Default false.

          include_settled: Also list settled and expired events, not only events with a listable market.
              Every market then counts as listable for the other filters, `title`,
              `categories`, and the open and close times. Default false. A request that takes
              longer than 30 seconds fails with `504`; narrow `search` or the filters and try
              again.

          market_ids: Comma-separated market ids (UUID) or tickers, 1-100. Keeps events of those
              markets, in any status; the other filters still apply. Ids that match no market
              are reported: `207`, or `404` when none match.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          search: Keeps events whose code, series code, or a market's question or title contains
              every word, matched by prefix and English stem, ignoring case. Searches listable
              events, or every event with `include_settled`. A word of four or more letters
              that matches nothing is replaced by up to three close spellings. Without
              `sort_by`, orders by relevance, closest spellings first.

          series_codes: Comma-separated series codes. Keeps events of those series, ignoring case.

          sort_by: Sort key. Defaults to relevance when `search` is set, else the event code. Ties
              break on event code ascending.

          sort_direction: Sort direction. Defaults to ascending. Ignored when sorting by relevance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instruments/predictions/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "categories": categories,
                        "close_at": close_at,
                        "include_markets": include_markets,
                        "include_settled": include_settled,
                        "market_ids": market_ids,
                        "open_at": open_at,
                        "page_size": page_size,
                        "page_token": page_token,
                        "search": search,
                        "series_codes": series_codes,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    instrument_get_prediction_events_params.InstrumentGetPredictionEventsParams,
                ),
            ),
            cast_to=InstrumentGetPredictionEventsResponse,
        )

    async def get_prediction_markets(
        self,
        *,
        event_code: str | Omit = omit,
        market_ids: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        statuses: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionMarketsResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Looks up prediction markets in any status, by `market_ids` (1-100 market ids or
        tickers) or by `event_code`. Exactly one of the two is required. Markets are
        ordered by symbol.

        `statuses` keeps markets in any listed status. It defaults to `OPEN` with
        `event_code` and to every status with `market_ids`.

        With `event_code`, pages carry no totals: follow `next_page_token` until it is
        absent. `market_ids` lookups are not paginated and ignore page parameters.

        With `market_ids`, ids that match no market are reported: `207` with the markets
        found and the missing ids in `error.details`, or `404` when none matched. A
        market removed only by `statuses` is not reported as missing.

        Each market trades one YES-denominated instrument; there is no NO instrument.
        Prices, including those from `/market-data/snapshot`, are YES prices in dollars,
        and `no_price = 1 - yes_price`. A negative position quantity is NO exposure.

        Args:
          event_code: Event code; returns the markets of the event. Mutually exclusive with
              `market_ids`.

          market_ids: Comma-separated market ids (UUID) or tickers, 1-100, in any status. Mutually
              exclusive with `event_code`.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          statuses: Comma-separated statuses to keep: `OPEN`, `UNOPENED`, `PAUSED`, `CLOSED`,
              `SETTLED`. Defaults to `OPEN` with `event_code` and to every status with
              `market_ids`. Unrecognized values are ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instruments/predictions/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_code": event_code,
                        "market_ids": market_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "statuses": statuses,
                    },
                    instrument_get_prediction_markets_params.InstrumentGetPredictionMarketsParams,
                ),
            ),
            cast_to=InstrumentGetPredictionMarketsResponse,
        )

    async def get_prediction_series(
        self,
        *,
        categories: str | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetPredictionSeriesResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Lists the distinct series codes of prediction markets that can currently be
        listed: markets that are initialized or active and have not yet closed. Series
        are ordered by code.

        `categories` keeps series with a market in any listed category, ignoring case.
        Pages carry no totals: follow `next_page_token` until it is absent.

        Args:
          categories: Comma-separated categories. Keeps series with a market in any of them, ignoring
              case.

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
            "/v1/instruments/predictions/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "categories": categories,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_get_prediction_series_params.InstrumentGetPredictionSeriesParams,
                ),
            ),
            cast_to=InstrumentGetPredictionSeriesResponse,
        )

    async def search_instruments(
        self,
        *,
        q: str,
        asset_class: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        include_inactive: bool | Omit = omit,
        include_ptp: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentSearchInstrumentsResponse:
        """
        Search instruments by symbol, alternate identifier, or company name.

        The `q` parameter is case-insensitive and supports ticker symbols, alternate
        identifiers such as CUSIP, ISIN, and OPRA root, and company names for non-option
        instruments. Results are ranked by match quality plus instrument quality signals
        and relevance. Defaults to the `EQUITY` asset class (common stocks, preferred
        shares, ADRs, ETFs, and exchange-traded mutual funds). Pass `asset_class=OPTION`
        to search option contracts: by full OSI symbol, by an OSI prefix (root +
        `YYMMDD` expiry, e.g. `AAPL 261217`), or by a root-scoped phrase such as
        `AAPL Dec 250 call`.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alternate identifiers
              (CUSIP, ISIN, OPRA root), and company names for non-option instruments. Option
              searches match symbols and alternate identifiers.

          asset_class: Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER). Defaults to
              EQUITY.

          country: Optional listing-country filter (e.g., US).

          currency: Optional ISO currency filter (e.g., USD).

          include_inactive: Include inactive instruments. Default false.

          include_ptp: Include publicly traded partnership (PTP) instruments. Default true (penalized
              in ranking).

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
            "/v1/instruments/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "asset_class": asset_class,
                        "country": country,
                        "currency": currency,
                        "include_inactive": include_inactive,
                        "include_ptp": include_ptp,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    instrument_search_instruments_params.InstrumentSearchInstrumentsParams,
                ),
            ),
            cast_to=InstrumentSearchInstrumentsResponse,
        )


class InstrumentsResourceWithRawResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = to_raw_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = to_raw_response_wrapper(
            instruments.get_instruments,
        )
        self.get_option_contracts = to_raw_response_wrapper(
            instruments.get_option_contracts,
        )
        self.get_prediction_categories = to_raw_response_wrapper(
            instruments.get_prediction_categories,
        )
        self.get_prediction_events = to_raw_response_wrapper(
            instruments.get_prediction_events,
        )
        self.get_prediction_markets = to_raw_response_wrapper(
            instruments.get_prediction_markets,
        )
        self.get_prediction_series = to_raw_response_wrapper(
            instruments.get_prediction_series,
        )
        self.search_instruments = to_raw_response_wrapper(
            instruments.search_instruments,
        )


class AsyncInstrumentsResourceWithRawResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_raw_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_raw_response_wrapper(
            instruments.get_instruments,
        )
        self.get_option_contracts = async_to_raw_response_wrapper(
            instruments.get_option_contracts,
        )
        self.get_prediction_categories = async_to_raw_response_wrapper(
            instruments.get_prediction_categories,
        )
        self.get_prediction_events = async_to_raw_response_wrapper(
            instruments.get_prediction_events,
        )
        self.get_prediction_markets = async_to_raw_response_wrapper(
            instruments.get_prediction_markets,
        )
        self.get_prediction_series = async_to_raw_response_wrapper(
            instruments.get_prediction_series,
        )
        self.search_instruments = async_to_raw_response_wrapper(
            instruments.search_instruments,
        )


class InstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = to_streamed_response_wrapper(
            instruments.get_instruments,
        )
        self.get_option_contracts = to_streamed_response_wrapper(
            instruments.get_option_contracts,
        )
        self.get_prediction_categories = to_streamed_response_wrapper(
            instruments.get_prediction_categories,
        )
        self.get_prediction_events = to_streamed_response_wrapper(
            instruments.get_prediction_events,
        )
        self.get_prediction_markets = to_streamed_response_wrapper(
            instruments.get_prediction_markets,
        )
        self.get_prediction_series = to_streamed_response_wrapper(
            instruments.get_prediction_series,
        )
        self.search_instruments = to_streamed_response_wrapper(
            instruments.search_instruments,
        )


class AsyncInstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_streamed_response_wrapper(
            instruments.get_instruments,
        )
        self.get_option_contracts = async_to_streamed_response_wrapper(
            instruments.get_option_contracts,
        )
        self.get_prediction_categories = async_to_streamed_response_wrapper(
            instruments.get_prediction_categories,
        )
        self.get_prediction_events = async_to_streamed_response_wrapper(
            instruments.get_prediction_events,
        )
        self.get_prediction_markets = async_to_streamed_response_wrapper(
            instruments.get_prediction_markets,
        )
        self.get_prediction_series = async_to_streamed_response_wrapper(
            instruments.get_prediction_series,
        )
        self.search_instruments = async_to_streamed_response_wrapper(
            instruments.search_instruments,
        )
