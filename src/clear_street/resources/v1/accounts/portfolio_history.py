# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.v1.accounts import portfolio_history_get_portfolio_history_params
from ....types.v1.accounts.portfolio_history_get_portfolio_history_response import (
    PortfolioHistoryGetPortfolioHistoryResponse,
)

__all__ = ["PortfolioHistoryResource", "AsyncPortfolioHistoryResource"]


class PortfolioHistoryResource(SyncAPIResource):
    """Manage trading accounts, balances, and portfolio history."""

    @cached_property
    def with_raw_response(self) -> PortfolioHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PortfolioHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfolioHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return PortfolioHistoryResourceWithStreamingResponse(self)

    def get_portfolio_history(
        self,
        account_id: int,
        *,
        start_date: Union[str, date],
        end_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioHistoryGetPortfolioHistoryResponse:
        """
        Retrieves daily portfolio history for the specified account.

        Args:
          end_date: Defaults to today in America/New_York when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/portfolio-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                    },
                    portfolio_history_get_portfolio_history_params.PortfolioHistoryGetPortfolioHistoryParams,
                ),
            ),
            cast_to=PortfolioHistoryGetPortfolioHistoryResponse,
        )


class AsyncPortfolioHistoryResource(AsyncAPIResource):
    """Manage trading accounts, balances, and portfolio history."""

    @cached_property
    def with_raw_response(self) -> AsyncPortfolioHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortfolioHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfolioHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncPortfolioHistoryResourceWithStreamingResponse(self)

    async def get_portfolio_history(
        self,
        account_id: int,
        *,
        start_date: Union[str, date],
        end_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioHistoryGetPortfolioHistoryResponse:
        """
        Retrieves daily portfolio history for the specified account.

        Args:
          end_date: Defaults to today in America/New_York when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/portfolio-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                    },
                    portfolio_history_get_portfolio_history_params.PortfolioHistoryGetPortfolioHistoryParams,
                ),
            ),
            cast_to=PortfolioHistoryGetPortfolioHistoryResponse,
        )


class PortfolioHistoryResourceWithRawResponse:
    def __init__(self, portfolio_history: PortfolioHistoryResource) -> None:
        self._portfolio_history = portfolio_history

        self.get_portfolio_history = to_raw_response_wrapper(
            portfolio_history.get_portfolio_history,
        )


class AsyncPortfolioHistoryResourceWithRawResponse:
    def __init__(self, portfolio_history: AsyncPortfolioHistoryResource) -> None:
        self._portfolio_history = portfolio_history

        self.get_portfolio_history = async_to_raw_response_wrapper(
            portfolio_history.get_portfolio_history,
        )


class PortfolioHistoryResourceWithStreamingResponse:
    def __init__(self, portfolio_history: PortfolioHistoryResource) -> None:
        self._portfolio_history = portfolio_history

        self.get_portfolio_history = to_streamed_response_wrapper(
            portfolio_history.get_portfolio_history,
        )


class AsyncPortfolioHistoryResourceWithStreamingResponse:
    def __init__(self, portfolio_history: AsyncPortfolioHistoryResource) -> None:
        self._portfolio_history = portfolio_history

        self.get_portfolio_history = async_to_streamed_response_wrapper(
            portfolio_history.get_portfolio_history,
        )
