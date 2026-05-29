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
    ContractType,
    InstrumentIDOrSymbol,
    instrument_get_instruments_params,
    instrument_search_instruments_params,
    instrument_get_instrument_by_id_params,
    instrument_get_option_contracts_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.contract_type import ContractType
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.instrument_get_instruments_response import InstrumentGetInstrumentsResponse
from ...types.v1.instrument_search_instruments_response import InstrumentSearchInstrumentsResponse
from ...types.v1.instrument_get_instrument_by_id_response import InstrumentGetInstrumentByIDResponse
from ...types.v1.instrument_get_option_contracts_response import InstrumentGetOptionContractsResponse

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
        instrument_id: InstrumentIDOrSymbol,
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
          instrument_id: OEMS instrument UUID

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
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
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

          instrument_ids: Comma-separated OEMS instrument UUIDs

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
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: InstrumentIDOrSymbol | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlying_instrument_id: OEMS instrument UUID or symbol of the underlying equity/index

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
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "page_size": page_size,
                        "page_token": page_token,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    instrument_get_option_contracts_params.InstrumentGetOptionContractsParams,
                ),
            ),
            cast_to=InstrumentGetOptionContractsResponse,
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
        identifiers such as CUSIP, ISIN, OPRA root, and CMS identifiers, and company
        names for non-option instruments. Results are ranked by match quality plus
        instrument quality signals including log-scaled ADV, listing status,
        marginability, easy-to-borrow status, and OTC, restricted, and liquidation-only
        penalties. Defaults to the `EQUITY` asset class (common stocks, preferred
        shares, ADRs, ETFs, and exchange-traded mutual funds). Pass `asset_class=OPTION`
        to search option contracts by symbol or alternate identifier.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alternate identifiers
              (CUSIP, ISIN, OPRA root, CMS), and company names for non-option instruments.
              Option searches match symbols and alternate identifiers.

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
        instrument_id: InstrumentIDOrSymbol,
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
          instrument_id: OEMS instrument UUID

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
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
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

          instrument_ids: Comma-separated OEMS instrument UUIDs

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
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: InstrumentIDOrSymbol | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlying_instrument_id: OEMS instrument UUID or symbol of the underlying equity/index

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
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "page_size": page_size,
                        "page_token": page_token,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    instrument_get_option_contracts_params.InstrumentGetOptionContractsParams,
                ),
            ),
            cast_to=InstrumentGetOptionContractsResponse,
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
        identifiers such as CUSIP, ISIN, OPRA root, and CMS identifiers, and company
        names for non-option instruments. Results are ranked by match quality plus
        instrument quality signals including log-scaled ADV, listing status,
        marginability, easy-to-borrow status, and OTC, restricted, and liquidation-only
        penalties. Defaults to the `EQUITY` asset class (common stocks, preferred
        shares, ADRs, ETFs, and exchange-traded mutual funds). Pass `asset_class=OPTION`
        to search option contracts by symbol or alternate identifier.

        Args:
          q: Search term applied case-insensitively to ticker symbols, alternate identifiers
              (CUSIP, ISIN, OPRA root, CMS), and company names for non-option instruments.
              Option searches match symbols and alternate identifiers.

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
        self.search_instruments = async_to_streamed_response_wrapper(
            instruments.search_instruments,
        )
