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
from ....types.v1.instruments import cash_flow_statement_get_instrument_cash_flow_statements_params
from ....types.v1.instruments.cash_flow_statement_get_instrument_cash_flow_statements_response import (
    CashFlowStatementGetInstrumentCashFlowStatementsResponse,
)

__all__ = ["CashFlowStatementsResource", "AsyncCashFlowStatementsResource"]


class CashFlowStatementsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> CashFlowStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return CashFlowStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CashFlowStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return CashFlowStatementsResourceWithStreamingResponse(self)

    def get_instrument_cash_flow_statements(
        self,
        instrument_id: str,
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
    ) -> CashFlowStatementGetInstrumentCashFlowStatementsResponse:
        """
        Get cash flow statements for an instrument.

        Retrieves historical cash flow statements for the specified instrument. Cash
        flow statements show cash inflows and outflows from operating, investing, and
        financing activities.

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
                    cash_flow_statement_get_instrument_cash_flow_statements_params.CashFlowStatementGetInstrumentCashFlowStatementsParams,
                ),
            ),
            cast_to=CashFlowStatementGetInstrumentCashFlowStatementsResponse,
        )


class AsyncCashFlowStatementsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncCashFlowStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCashFlowStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCashFlowStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncCashFlowStatementsResourceWithStreamingResponse(self)

    async def get_instrument_cash_flow_statements(
        self,
        instrument_id: str,
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
    ) -> CashFlowStatementGetInstrumentCashFlowStatementsResponse:
        """
        Get cash flow statements for an instrument.

        Retrieves historical cash flow statements for the specified instrument. Cash
        flow statements show cash inflows and outflows from operating, investing, and
        financing activities.

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
                    cash_flow_statement_get_instrument_cash_flow_statements_params.CashFlowStatementGetInstrumentCashFlowStatementsParams,
                ),
            ),
            cast_to=CashFlowStatementGetInstrumentCashFlowStatementsResponse,
        )


class CashFlowStatementsResourceWithRawResponse:
    def __init__(self, cash_flow_statements: CashFlowStatementsResource) -> None:
        self._cash_flow_statements = cash_flow_statements

        self.get_instrument_cash_flow_statements = to_raw_response_wrapper(
            cash_flow_statements.get_instrument_cash_flow_statements,
        )


class AsyncCashFlowStatementsResourceWithRawResponse:
    def __init__(self, cash_flow_statements: AsyncCashFlowStatementsResource) -> None:
        self._cash_flow_statements = cash_flow_statements

        self.get_instrument_cash_flow_statements = async_to_raw_response_wrapper(
            cash_flow_statements.get_instrument_cash_flow_statements,
        )


class CashFlowStatementsResourceWithStreamingResponse:
    def __init__(self, cash_flow_statements: CashFlowStatementsResource) -> None:
        self._cash_flow_statements = cash_flow_statements

        self.get_instrument_cash_flow_statements = to_streamed_response_wrapper(
            cash_flow_statements.get_instrument_cash_flow_statements,
        )


class AsyncCashFlowStatementsResourceWithStreamingResponse:
    def __init__(self, cash_flow_statements: AsyncCashFlowStatementsResource) -> None:
        self._cash_flow_statements = cash_flow_statements

        self.get_instrument_cash_flow_statements = async_to_streamed_response_wrapper(
            cash_flow_statements.get_instrument_cash_flow_statements,
        )
