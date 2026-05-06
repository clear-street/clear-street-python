# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.accounts import InstrumentIDOrSymbol
from ....types.v1.instruments import balance_sheet_get_instrument_balance_sheet_statements_params
from ....types.v1.accounts.instrument_id_or_symbol import InstrumentIDOrSymbol
from ....types.v1.instruments.balance_sheet_get_instrument_balance_sheet_statements_response import (
    BalanceSheetGetInstrumentBalanceSheetStatementsResponse,
)

__all__ = ["BalanceSheetsResource", "AsyncBalanceSheetsResource"]


class BalanceSheetsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> BalanceSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return BalanceSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return BalanceSheetsResourceWithStreamingResponse(self)

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
    ) -> BalanceSheetGetInstrumentBalanceSheetStatementsResponse:
        """
        Get balance sheet statements for an instrument.

        Retrieves quarterly balance sheet statements for a specific instrument, sorted
        by fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: OEMS instrument UUID

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

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
                    balance_sheet_get_instrument_balance_sheet_statements_params.BalanceSheetGetInstrumentBalanceSheetStatementsParams,
                ),
            ),
            cast_to=BalanceSheetGetInstrumentBalanceSheetStatementsResponse,
        )


class AsyncBalanceSheetsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncBalanceSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncBalanceSheetsResourceWithStreamingResponse(self)

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
    ) -> BalanceSheetGetInstrumentBalanceSheetStatementsResponse:
        """
        Get balance sheet statements for an instrument.

        Retrieves quarterly balance sheet statements for a specific instrument, sorted
        by fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          instrument_id: OEMS instrument UUID

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

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
                    balance_sheet_get_instrument_balance_sheet_statements_params.BalanceSheetGetInstrumentBalanceSheetStatementsParams,
                ),
            ),
            cast_to=BalanceSheetGetInstrumentBalanceSheetStatementsResponse,
        )


class BalanceSheetsResourceWithRawResponse:
    def __init__(self, balance_sheets: BalanceSheetsResource) -> None:
        self._balance_sheets = balance_sheets

        self.get_instrument_balance_sheet_statements = to_raw_response_wrapper(
            balance_sheets.get_instrument_balance_sheet_statements,
        )


class AsyncBalanceSheetsResourceWithRawResponse:
    def __init__(self, balance_sheets: AsyncBalanceSheetsResource) -> None:
        self._balance_sheets = balance_sheets

        self.get_instrument_balance_sheet_statements = async_to_raw_response_wrapper(
            balance_sheets.get_instrument_balance_sheet_statements,
        )


class BalanceSheetsResourceWithStreamingResponse:
    def __init__(self, balance_sheets: BalanceSheetsResource) -> None:
        self._balance_sheets = balance_sheets

        self.get_instrument_balance_sheet_statements = to_streamed_response_wrapper(
            balance_sheets.get_instrument_balance_sheet_statements,
        )


class AsyncBalanceSheetsResourceWithStreamingResponse:
    def __init__(self, balance_sheets: AsyncBalanceSheetsResource) -> None:
        self._balance_sheets = balance_sheets

        self.get_instrument_balance_sheet_statements = async_to_streamed_response_wrapper(
            balance_sheets.get_instrument_balance_sheet_statements,
        )
