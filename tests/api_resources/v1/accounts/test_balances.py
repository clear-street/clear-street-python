# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.accounts import BalanceGetAccountBalancesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_account_balances(self, client: ClearStreet) -> None:
        balance = client.v1.accounts.balances.get_account_balances(
            account_id=0,
        )
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_account_balances_with_all_params(self, client: ClearStreet) -> None:
        balance = client.v1.accounts.balances.get_account_balances(
            account_id=0,
            top_margin_contributors_limit=1,
        )
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_account_balances(self, client: ClearStreet) -> None:
        response = client.v1.accounts.balances.with_raw_response.get_account_balances(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_account_balances(self, client: ClearStreet) -> None:
        with client.v1.accounts.balances.with_streaming_response.get_account_balances(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        balance = await async_client.v1.accounts.balances.get_account_balances(
            account_id=0,
        )
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_account_balances_with_all_params(self, async_client: AsyncClearStreet) -> None:
        balance = await async_client.v1.accounts.balances.get_account_balances(
            account_id=0,
            top_margin_contributors_limit=1,
        )
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.balances.with_raw_response.get_account_balances(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_account_balances(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.balances.with_streaming_response.get_account_balances(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceGetAccountBalancesResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True
