# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active import SecurityIDSource
from .....types.active.v1.instruments import income_statement_get_instrument_income_statements_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instruments.income_statement_get_instrument_income_statements_response import (
    IncomeStatementGetInstrumentIncomeStatementsResponse,
)

__all__ = ["IncomeStatementsResource", "AsyncIncomeStatementsResource"]


class IncomeStatementsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> IncomeStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return IncomeStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomeStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return IncomeStatementsResourceWithStreamingResponse(self)

    def get_instrument_income_statements(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
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
    ) -> IncomeStatementGetInstrumentIncomeStatementsResponse:
        """
        Retrieves quarterly income statements for a specific instrument, sorted by
        fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

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
                "/active/v1/instruments/{security_id_source}/{security_id}/income-statements",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
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
                    income_statement_get_instrument_income_statements_params.IncomeStatementGetInstrumentIncomeStatementsParams,
                ),
            ),
            cast_to=IncomeStatementGetInstrumentIncomeStatementsResponse,
        )


class AsyncIncomeStatementsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncIncomeStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncomeStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomeStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncIncomeStatementsResourceWithStreamingResponse(self)

    async def get_instrument_income_statements(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
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
    ) -> IncomeStatementGetInstrumentIncomeStatementsResponse:
        """
        Retrieves quarterly income statements for a specific instrument, sorted by
        fiscal period (most recent first).

        Date range defaults:

        - `from_date`: None (no lower bound)
        - `to_date`: None (no upper bound)

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

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
                "/active/v1/instruments/{security_id_source}/{security_id}/income-statements",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
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
                    income_statement_get_instrument_income_statements_params.IncomeStatementGetInstrumentIncomeStatementsParams,
                ),
            ),
            cast_to=IncomeStatementGetInstrumentIncomeStatementsResponse,
        )


class IncomeStatementsResourceWithRawResponse:
    def __init__(self, income_statements: IncomeStatementsResource) -> None:
        self._income_statements = income_statements

        self.get_instrument_income_statements = to_raw_response_wrapper(
            income_statements.get_instrument_income_statements,
        )


class AsyncIncomeStatementsResourceWithRawResponse:
    def __init__(self, income_statements: AsyncIncomeStatementsResource) -> None:
        self._income_statements = income_statements

        self.get_instrument_income_statements = async_to_raw_response_wrapper(
            income_statements.get_instrument_income_statements,
        )


class IncomeStatementsResourceWithStreamingResponse:
    def __init__(self, income_statements: IncomeStatementsResource) -> None:
        self._income_statements = income_statements

        self.get_instrument_income_statements = to_streamed_response_wrapper(
            income_statements.get_instrument_income_statements,
        )


class AsyncIncomeStatementsResourceWithStreamingResponse:
    def __init__(self, income_statements: AsyncIncomeStatementsResource) -> None:
        self._income_statements = income_statements

        self.get_instrument_income_statements = async_to_streamed_response_wrapper(
            income_statements.get_instrument_income_statements,
        )
