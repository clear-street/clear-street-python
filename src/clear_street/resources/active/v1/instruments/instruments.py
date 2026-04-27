# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from ....._types import (
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
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .fundamentals import (
    FundamentalsResource,
    AsyncFundamentalsResource,
    FundamentalsResourceWithRawResponse,
    AsyncFundamentalsResourceWithRawResponse,
    FundamentalsResourceWithStreamingResponse,
    AsyncFundamentalsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active import SecurityIDSource
from .analyst_reporting import (
    AnalystReportingResource,
    AsyncAnalystReportingResource,
    AnalystReportingResourceWithRawResponse,
    AsyncAnalystReportingResourceWithRawResponse,
    AnalystReportingResourceWithStreamingResponse,
    AsyncAnalystReportingResourceWithStreamingResponse,
)
from .....types.active.v1 import (
    instrument_search_params,
    instrument_get_instruments_params,
    instrument_get_instrument_by_id_params,
)
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instrument_search_response import InstrumentSearchResponse
from .....types.active.v1.instrument_get_instruments_response import InstrumentGetInstrumentsResponse
from .....types.active.v1.instrument_get_instrument_by_id_response import InstrumentGetInstrumentByIDResponse

__all__ = ["InstrumentsResource", "AsyncInstrumentsResource"]


class InstrumentsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        """Retrieve details and lists of tradable instruments."""
        return EventsResource(self._client)

    @cached_property
    def fundamentals(self) -> FundamentalsResource:
        """Retrieve details and lists of tradable instruments."""
        return FundamentalsResource(self._client)

    @cached_property
    def options(self) -> OptionsResource:
        """Retrieve details and lists of tradable instruments."""
        return OptionsResource(self._client)

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
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
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
          security_id_source: Security identifier source

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return self._get(
            path_template(
                "/active/v1/instruments/{security_id_source}/{security_id}",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
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
        id_filter: str | Omit = omit,
        instrument_type: Literal[
            "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
        ]
        | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_restricted: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
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

          id_filter: Filter IDs to those containing this substring. For options, and when
              instrument_type is omitted and no security_id/security_id_source filters are
              provided, this is required.

          instrument_type: Filter by instrument type. If omitted, returns all types.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "id_filter": id_filter,
                        "instrument_type": instrument_type,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_restricted": is_restricted,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )

    def search(
        self,
        *,
        q: str,
        asset_class: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_inactive: bool | Omit = omit,
        include_restricted: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentSearchResponse:
        """
        Fast in-memory typeahead search over the loaded instrument universe.

        Supports three independent match dimensions in a single `q` parameter: ticker
        symbol (exact > prefix > substring), alt-id exact (CUSIP / ISIN / OPRA root /
        CMS), and company name (token + character-trigram). Results are ranked by a
        composite score that includes ADV (log-scaled), listing status, marginable / ETB
        flags, and OTC / restricted / liquidation-only penalties. Defaults to the
        `EQUITY` asset class (common stock + ETFs + exchange-traded mutual funds); pass
        `asset_class=OPTION` for option chains.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alt-IDs
              (CUSIP/ISIN/OPRA-root/CMS), and company names.

          asset_class: Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER). Defaults to
              EQUITY.

          country: Optional listing-country filter (e.g., US).

          currency: Optional ISO currency filter (e.g., USD).

          cursor: Opaque continuation cursor for show-more paging — pass the `next_page_token`
              from a prior response. Same wire format as `page_token` on other paginated
              endpoints.

          include_inactive: Include inactive instruments. Default false.

          include_restricted: Include restricted instruments. Default true (penalized in ranking).

          limit: Maximum hits to return. Bounded [1, 100]. Default 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/instruments/search",
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
                        "cursor": cursor,
                        "include_inactive": include_inactive,
                        "include_restricted": include_restricted,
                        "limit": limit,
                    },
                    instrument_search_params.InstrumentSearchParams,
                ),
            ),
            cast_to=InstrumentSearchResponse,
        )


class AsyncInstrumentsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResource(self._client)

    @cached_property
    def fundamentals(self) -> AsyncFundamentalsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncFundamentalsResource(self._client)

    @cached_property
    def options(self) -> AsyncOptionsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncOptionsResource(self._client)

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
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
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
          security_id_source: Security identifier source

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return await self._get(
            path_template(
                "/active/v1/instruments/{security_id_source}/{security_id}",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
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
        id_filter: str | Omit = omit,
        instrument_type: Literal[
            "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
        ]
        | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_restricted: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
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

          id_filter: Filter IDs to those containing this substring. For options, and when
              instrument_type is omitted and no security_id/security_id_source filters are
              provided, this is required.

          instrument_type: Filter by instrument type. If omitted, returns all types.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "id_filter": id_filter,
                        "instrument_type": instrument_type,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_restricted": is_restricted,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )

    async def search(
        self,
        *,
        q: str,
        asset_class: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_inactive: bool | Omit = omit,
        include_restricted: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentSearchResponse:
        """
        Fast in-memory typeahead search over the loaded instrument universe.

        Supports three independent match dimensions in a single `q` parameter: ticker
        symbol (exact > prefix > substring), alt-id exact (CUSIP / ISIN / OPRA root /
        CMS), and company name (token + character-trigram). Results are ranked by a
        composite score that includes ADV (log-scaled), listing status, marginable / ETB
        flags, and OTC / restricted / liquidation-only penalties. Defaults to the
        `EQUITY` asset class (common stock + ETFs + exchange-traded mutual funds); pass
        `asset_class=OPTION` for option chains.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alt-IDs
              (CUSIP/ISIN/OPRA-root/CMS), and company names.

          asset_class: Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER). Defaults to
              EQUITY.

          country: Optional listing-country filter (e.g., US).

          currency: Optional ISO currency filter (e.g., USD).

          cursor: Opaque continuation cursor for show-more paging — pass the `next_page_token`
              from a prior response. Same wire format as `page_token` on other paginated
              endpoints.

          include_inactive: Include inactive instruments. Default false.

          include_restricted: Include restricted instruments. Default true (penalized in ranking).

          limit: Maximum hits to return. Bounded [1, 100]. Default 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/instruments/search",
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
                        "cursor": cursor,
                        "include_inactive": include_inactive,
                        "include_restricted": include_restricted,
                        "limit": limit,
                    },
                    instrument_search_params.InstrumentSearchParams,
                ),
            ),
            cast_to=InstrumentSearchResponse,
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
        self.search = to_raw_response_wrapper(
            instruments.search,
        )

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return EventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def fundamentals(self) -> FundamentalsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return FundamentalsResourceWithRawResponse(self._instruments.fundamentals)

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return OptionsResourceWithRawResponse(self._instruments.options)


class AsyncInstrumentsResourceWithRawResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_raw_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_raw_response_wrapper(
            instruments.get_instruments,
        )
        self.search = async_to_raw_response_wrapper(
            instruments.search,
        )

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def fundamentals(self) -> AsyncFundamentalsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncFundamentalsResourceWithRawResponse(self._instruments.fundamentals)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncOptionsResourceWithRawResponse(self._instruments.options)


class InstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = to_streamed_response_wrapper(
            instruments.get_instruments,
        )
        self.search = to_streamed_response_wrapper(
            instruments.search,
        )

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return EventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def fundamentals(self) -> FundamentalsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return FundamentalsResourceWithStreamingResponse(self._instruments.fundamentals)

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return OptionsResourceWithStreamingResponse(self._instruments.options)


class AsyncInstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_streamed_response_wrapper(
            instruments.get_instruments,
        )
        self.search = async_to_streamed_response_wrapper(
            instruments.search,
        )

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def fundamentals(self) -> AsyncFundamentalsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncFundamentalsResourceWithStreamingResponse(self._instruments.fundamentals)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncOptionsResourceWithStreamingResponse(self._instruments.options)
