# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_date
from clear_street.types.v1.accounts import (
    PortfolioHistoryGetPortfolioHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortfolioHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_portfolio_history(self, client: ClearStreet) -> None:
        portfolio_history = client.v1.accounts.portfolio_history.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_portfolio_history_with_all_params(self, client: ClearStreet) -> None:
        portfolio_history = client.v1.accounts.portfolio_history.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
            end_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_portfolio_history(self, client: ClearStreet) -> None:
        response = client.v1.accounts.portfolio_history.with_raw_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio_history = response.parse()
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_portfolio_history(self, client: ClearStreet) -> None:
        with client.v1.accounts.portfolio_history.with_streaming_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio_history = response.parse()
            assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPortfolioHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        portfolio_history = await async_client.v1.accounts.portfolio_history.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_portfolio_history_with_all_params(self, async_client: AsyncClearStreet) -> None:
        portfolio_history = await async_client.v1.accounts.portfolio_history.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
            end_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.portfolio_history.with_raw_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio_history = await response.parse()
        assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_portfolio_history(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.portfolio_history.with_streaming_response.get_portfolio_history(
            account_id=0,
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio_history = await response.parse()
            assert_matches_type(PortfolioHistoryGetPortfolioHistoryResponse, portfolio_history, path=["response"])

        assert cast(Any, response.is_closed) is True
