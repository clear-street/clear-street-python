# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet._utils import parse_date
from clearstreet.types.v1 import (
    AccountGetAccountsResponse,
    AccountGetAccountByIDResponse,
    AccountPatchAccountByIDResponse,
    AccountGetAccountBalancesResponse,
    AccountGetPortfolioHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_account_balances(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_account_balances(
            account_id=0,
        )
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    def test_method_get_account_balances_with_all_params(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_account_balances(
            account_id=0,
            top_margin_contributors_limit=1,
        )
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    def test_raw_response_get_account_balances(self, client: ClearStreet) -> None:
        response = client.v1.accounts.with_raw_response.get_account_balances(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_get_account_balances(self, client: ClearStreet) -> None:
        with client.v1.accounts.with_streaming_response.get_account_balances(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_account_by_id(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_account_by_id(
            0,
        )
        assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

    @parametrize
    def test_raw_response_get_account_by_id(self, client: ClearStreet) -> None:
        response = client.v1.accounts.with_raw_response.get_account_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_get_account_by_id(self, client: ClearStreet) -> None:
        with client.v1.accounts.with_streaming_response.get_account_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_accounts(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_accounts()
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    def test_method_get_accounts_with_all_params(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_accounts(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    def test_raw_response_get_accounts(self, client: ClearStreet) -> None:
        response = client.v1.accounts.with_raw_response.get_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_get_accounts(self, client: ClearStreet) -> None:
        with client.v1.accounts.with_streaming_response.get_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_portfolio_history(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    def test_method_get_portfolio_history_with_all_params(self, client: ClearStreet) -> None:
        account = client.v1.accounts.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
            end_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    def test_raw_response_get_portfolio_history(self, client: ClearStreet) -> None:
        response = client.v1.accounts.with_raw_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_get_portfolio_history(self, client: ClearStreet) -> None:
        with client.v1.accounts.with_streaming_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_patch_account_by_id(self, client: ClearStreet) -> None:
        account = client.v1.accounts.patch_account_by_id(
            account_id=0,
        )
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    def test_method_patch_account_by_id_with_all_params(self, client: ClearStreet) -> None:
        account = client.v1.accounts.patch_account_by_id(
            account_id=0,
            risk={"max_notional": "5000000.00"},
        )
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    def test_raw_response_patch_account_by_id(self, client: ClearStreet) -> None:
        response = client.v1.accounts.with_raw_response.patch_account_by_id(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_patch_account_by_id(self, client: ClearStreet) -> None:
        with client.v1.accounts.with_streaming_response.patch_account_by_id(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_account_balances(
            account_id=0,
        )
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    async def test_method_get_account_balances_with_all_params(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_account_balances(
            account_id=0,
            top_margin_contributors_limit=1,
        )
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.with_raw_response.get_account_balances(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.with_streaming_response.get_account_balances(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetAccountBalancesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_account_by_id(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_account_by_id(
            0,
        )
        assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_get_account_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.with_raw_response.get_account_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_get_account_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.with_streaming_response.get_account_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetAccountByIDResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_accounts(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_accounts()
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    async def test_method_get_accounts_with_all_params(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_accounts(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_get_accounts(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.with_raw_response.get_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_get_accounts(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.with_streaming_response.get_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    async def test_method_get_portfolio_history_with_all_params(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
            end_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.with_raw_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.with_streaming_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetPortfolioHistoryResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_patch_account_by_id(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.patch_account_by_id(
            account_id=0,
        )
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    async def test_method_patch_account_by_id_with_all_params(self, async_client: AsyncClearStreet) -> None:
        account = await async_client.v1.accounts.patch_account_by_id(
            account_id=0,
            risk={"max_notional": "5000000.00"},
        )
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_patch_account_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.with_raw_response.patch_account_by_id(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_patch_account_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.with_streaming_response.patch_account_by_id(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountPatchAccountByIDResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
