# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    account_get_accounts_params,
    account_patch_account_by_id_params,
    account_get_account_balances_params,
    account_get_portfolio_history_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.risk_settings_param import RiskSettingsParam
from ...types.v1.account_get_accounts_response import AccountGetAccountsResponse
from ...types.v1.account_get_account_by_id_response import AccountGetAccountByIDResponse
from ...types.v1.account_patch_account_by_id_response import AccountPatchAccountByIDResponse
from ...types.v1.account_get_account_balances_response import AccountGetAccountBalancesResponse
from ...types.v1.account_get_portfolio_history_response import AccountGetPortfolioHistoryResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """Manage trading accounts, balances, and portfolio history."""

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

    def get_account_balances(
        self,
        account_id: int,
        *,
        top_margin_contributors_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountBalancesResponse:
        """
        Fetch account balance information

        Args:
          top_margin_contributors_limit: Limit the number of top margin contributors returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/balances", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"top_margin_contributors_limit": top_margin_contributors_limit},
                    account_get_account_balances_params.AccountGetAccountBalancesParams,
                ),
            ),
            cast_to=AccountGetAccountBalancesResponse,
        )

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
            path_template("/v1/accounts/{account_id}", account_id=account_id),
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
            "/v1/accounts",
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
    ) -> AccountGetPortfolioHistoryResponse:
        """
        Retrieves daily portfolio history for the specified account.

        Args:
          start_date: Start date for the portfolio history range, in YYYY-MM-DD format.

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
                    account_get_portfolio_history_params.AccountGetPortfolioHistoryParams,
                ),
            ),
            cast_to=AccountGetPortfolioHistoryResponse,
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
            path_template("/v1/accounts/{account_id}", account_id=account_id),
            body=maybe_transform({"risk": risk}, account_patch_account_by_id_params.AccountPatchAccountByIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountPatchAccountByIDResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """Manage trading accounts, balances, and portfolio history."""

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

    async def get_account_balances(
        self,
        account_id: int,
        *,
        top_margin_contributors_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetAccountBalancesResponse:
        """
        Fetch account balance information

        Args:
          top_margin_contributors_limit: Limit the number of top margin contributors returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/balances", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"top_margin_contributors_limit": top_margin_contributors_limit},
                    account_get_account_balances_params.AccountGetAccountBalancesParams,
                ),
            ),
            cast_to=AccountGetAccountBalancesResponse,
        )

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
            path_template("/v1/accounts/{account_id}", account_id=account_id),
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
            "/v1/accounts",
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
    ) -> AccountGetPortfolioHistoryResponse:
        """
        Retrieves daily portfolio history for the specified account.

        Args:
          start_date: Start date for the portfolio history range, in YYYY-MM-DD format.

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
                    account_get_portfolio_history_params.AccountGetPortfolioHistoryParams,
                ),
            ),
            cast_to=AccountGetPortfolioHistoryResponse,
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
            path_template("/v1/accounts/{account_id}", account_id=account_id),
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

        self.get_account_balances = to_raw_response_wrapper(
            accounts.get_account_balances,
        )
        self.get_account_by_id = to_raw_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = to_raw_response_wrapper(
            accounts.get_accounts,
        )
        self.get_portfolio_history = to_raw_response_wrapper(
            accounts.get_portfolio_history,
        )
        self.patch_account_by_id = to_raw_response_wrapper(
            accounts.patch_account_by_id,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.get_account_balances = async_to_raw_response_wrapper(
            accounts.get_account_balances,
        )
        self.get_account_by_id = async_to_raw_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = async_to_raw_response_wrapper(
            accounts.get_accounts,
        )
        self.get_portfolio_history = async_to_raw_response_wrapper(
            accounts.get_portfolio_history,
        )
        self.patch_account_by_id = async_to_raw_response_wrapper(
            accounts.patch_account_by_id,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.get_account_balances = to_streamed_response_wrapper(
            accounts.get_account_balances,
        )
        self.get_account_by_id = to_streamed_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = to_streamed_response_wrapper(
            accounts.get_accounts,
        )
        self.get_portfolio_history = to_streamed_response_wrapper(
            accounts.get_portfolio_history,
        )
        self.patch_account_by_id = to_streamed_response_wrapper(
            accounts.patch_account_by_id,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.get_account_balances = async_to_streamed_response_wrapper(
            accounts.get_account_balances,
        )
        self.get_account_by_id = async_to_streamed_response_wrapper(
            accounts.get_account_by_id,
        )
        self.get_accounts = async_to_streamed_response_wrapper(
            accounts.get_accounts,
        )
        self.get_portfolio_history = async_to_streamed_response_wrapper(
            accounts.get_portfolio_history,
        )
        self.patch_account_by_id = async_to_streamed_response_wrapper(
            accounts.patch_account_by_id,
        )
