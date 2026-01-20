# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.accounts.balance_get_account_balances_response import BalanceGetAccountBalancesResponse

__all__ = ["BalancesResource", "AsyncBalancesResource"]


class BalancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return BalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return BalancesResourceWithStreamingResponse(self)

    def get_account_balances(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetAccountBalancesResponse:
        """
        Fetch account balance information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/active/v1/accounts/{account_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceGetAccountBalancesResponse,
        )


class AsyncBalancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncBalancesResourceWithStreamingResponse(self)

    async def get_account_balances(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetAccountBalancesResponse:
        """
        Fetch account balance information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/active/v1/accounts/{account_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceGetAccountBalancesResponse,
        )


class BalancesResourceWithRawResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.get_account_balances = to_raw_response_wrapper(
            balances.get_account_balances,
        )


class AsyncBalancesResourceWithRawResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.get_account_balances = async_to_raw_response_wrapper(
            balances.get_account_balances,
        )


class BalancesResourceWithStreamingResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.get_account_balances = to_streamed_response_wrapper(
            balances.get_account_balances,
        )


class AsyncBalancesResourceWithStreamingResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.get_account_balances = async_to_streamed_response_wrapper(
            balances.get_account_balances,
        )
