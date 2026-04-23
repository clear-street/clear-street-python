# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .balances import (
    BalancesResource,
    AsyncBalancesResource,
    BalancesResourceWithRawResponse,
    AsyncBalancesResourceWithRawResponse,
    BalancesResourceWithStreamingResponse,
    AsyncBalancesResourceWithStreamingResponse,
)
from .positions import (
    PositionsResource,
    AsyncPositionsResource,
    PositionsResourceWithRawResponse,
    AsyncPositionsResourceWithRawResponse,
    PositionsResourceWithStreamingResponse,
    AsyncPositionsResourceWithStreamingResponse,
)
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
from .portfolio_history import (
    PortfolioHistoryResource,
    AsyncPortfolioHistoryResource,
    PortfolioHistoryResourceWithRawResponse,
    AsyncPortfolioHistoryResourceWithRawResponse,
    PortfolioHistoryResourceWithStreamingResponse,
    AsyncPortfolioHistoryResourceWithStreamingResponse,
)
from .....types.active.v1 import account_get_accounts_params, account_patch_account_by_id_params
from .....types.active.v1.risk_settings_param import RiskSettingsParam
from .....types.active.v1.account_get_accounts_response import AccountGetAccountsResponse
from .....types.active.v1.account_get_account_by_id_response import AccountGetAccountByIDResponse
from .....types.active.v1.account_patch_account_by_id_response import AccountPatchAccountByIDResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """Manage trading accounts and view balances."""

    @cached_property
    def balances(self) -> BalancesResource:
        """Manage trading accounts and view balances."""
        return BalancesResource(self._client)

    @cached_property
    def orders(self) -> OrdersResource:
        """Place, monitor, and manage trading orders."""
        return OrdersResource(self._client)

    @cached_property
    def portfolio_history(self) -> PortfolioHistoryResource:
        """Manage trading accounts and view balances."""
        return PortfolioHistoryResource(self._client)

    @cached_property
    def positions(self) -> PositionsResource:
        """View account positions."""
        return PositionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def get_account_by_id(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountByIDResponse:
        """
        Fetch account details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/active/v1/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGetAccountByIDResponse,
        )

    def get_accounts(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountsResponse:
        """
        List accounts the authenticated user has permission to access

        Args:
          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    account_get_accounts_params.AccountGetAccountsParams,
                ),
            ),
            cast_to=AccountGetAccountsResponse,
        )

    def patch_account_by_id(
        self,
        account_id: int,
        *,
        risk: Optional[RiskSettingsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountPatchAccountByIDResponse:
        """
        Update account risk settings

        Args:
          risk: Risk settings for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/active/v1/accounts/{account_id}", account_id=account_id),
            body=maybe_transform({"risk": risk}, account_patch_account_by_id_params.AccountPatchAccountByIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountPatchAccountByIDResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """Manage trading accounts and view balances."""

    @cached_property
    def balances(self) -> AsyncBalancesResource:
        """Manage trading accounts and view balances."""
        return AsyncBalancesResource(self._client)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResource(self._client)

    @cached_property
    def portfolio_history(self) -> AsyncPortfolioHistoryResource:
        """Manage trading accounts and view balances."""
        return AsyncPortfolioHistoryResource(self._client)

    @cached_property
    def positions(self) -> AsyncPositionsResource:
        """View account positions."""
        return AsyncPositionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def get_account_by_id(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountByIDResponse:
        """
        Fetch account details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/active/v1/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGetAccountByIDResponse,
        )

    async def get_accounts(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountsResponse:
        """
        List accounts the authenticated user has permission to access

        Args:
          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    account_get_accounts_params.AccountGetAccountsParams,
                ),
            ),
            cast_to=AccountGetAccountsResponse,
        )

    async def patch_account_by_id(
        self,
        account_id: int,
        *,
        risk: Optional[RiskSettingsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountPatchAccountByIDResponse:
        """
        Update account risk settings

        Args:
          risk: Risk settings for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/active/v1/accounts/{account_id}", account_id=account_id),
            body=await async_maybe_transform(
                {"risk": risk}, account_patch_account_by_id_params.AccountPatchAccountByIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountPatchAccountByIDResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.get_account_by_id = to_raw_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = to_raw_response_wrapper(
            accounts.get_accounts,
        )
        self.patch_account_by_id = to_raw_response_wrapper(
            accounts.patch_account_by_id,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return BalancesResourceWithRawResponse(self._accounts.balances)

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        """Place, monitor, and manage trading orders."""
        return OrdersResourceWithRawResponse(self._accounts.orders)

    @cached_property
    def portfolio_history(self) -> PortfolioHistoryResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return PortfolioHistoryResourceWithRawResponse(self._accounts.portfolio_history)

    @cached_property
    def positions(self) -> PositionsResourceWithRawResponse:
        """View account positions."""
        return PositionsResourceWithRawResponse(self._accounts.positions)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.get_account_by_id = async_to_raw_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = async_to_raw_response_wrapper(
            accounts.get_accounts,
        )
        self.patch_account_by_id = async_to_raw_response_wrapper(
            accounts.patch_account_by_id,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return AsyncBalancesResourceWithRawResponse(self._accounts.balances)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResourceWithRawResponse(self._accounts.orders)

    @cached_property
    def portfolio_history(self) -> AsyncPortfolioHistoryResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return AsyncPortfolioHistoryResourceWithRawResponse(self._accounts.portfolio_history)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithRawResponse:
        """View account positions."""
        return AsyncPositionsResourceWithRawResponse(self._accounts.positions)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.get_account_by_id = to_streamed_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = to_streamed_response_wrapper(
            accounts.get_accounts,
        )
        self.patch_account_by_id = to_streamed_response_wrapper(
            accounts.patch_account_by_id,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return BalancesResourceWithStreamingResponse(self._accounts.balances)

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        """Place, monitor, and manage trading orders."""
        return OrdersResourceWithStreamingResponse(self._accounts.orders)

    @cached_property
    def portfolio_history(self) -> PortfolioHistoryResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return PortfolioHistoryResourceWithStreamingResponse(self._accounts.portfolio_history)

    @cached_property
    def positions(self) -> PositionsResourceWithStreamingResponse:
        """View account positions."""
        return PositionsResourceWithStreamingResponse(self._accounts.positions)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.get_account_by_id = async_to_streamed_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = async_to_streamed_response_wrapper(
            accounts.get_accounts,
        )
        self.patch_account_by_id = async_to_streamed_response_wrapper(
            accounts.patch_account_by_id,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return AsyncBalancesResourceWithStreamingResponse(self._accounts.balances)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResourceWithStreamingResponse(self._accounts.orders)

    @cached_property
    def portfolio_history(self) -> AsyncPortfolioHistoryResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return AsyncPortfolioHistoryResourceWithStreamingResponse(self._accounts.portfolio_history)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithStreamingResponse:
        """View account positions."""
        return AsyncPositionsResourceWithStreamingResponse(self._accounts.positions)
