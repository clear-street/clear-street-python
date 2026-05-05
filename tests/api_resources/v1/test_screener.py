# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1 import (
    ScreenerGetScreenerResponse,
    ScreenerSearchScreenerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreener:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_screener(self, client: ClearStreet) -> None:
        screener = client.v1.screener.get_screener()
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_screener_with_all_params(self, client: ClearStreet) -> None:
        screener = client.v1.screener.get_screener(
            field_filter=["string"],
            filter={"foo": "string"},
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_screener(self, client: ClearStreet) -> None:
        response = client.v1.screener.with_raw_response.get_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = response.parse()
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_screener(self, client: ClearStreet) -> None:
        with client.v1.screener.with_streaming_response.get_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = response.parse()
            assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_screener(self, client: ClearStreet) -> None:
        screener = client.v1.screener.search_screener()
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_screener_with_all_params(self, client: ClearStreet) -> None:
        screener = client.v1.screener.search_screener(
            field_filter=[
                {
                    "name": "market_cap",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
                {
                    "name": "price",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
                {
                    "name": "volume",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
            ],
            filters=[
                {
                    "left": {
                        "name": "market_cap",
                        "lookback": "ONE_WEEK",
                        "period": "QUARTER",
                        "value_type": "DECIMAL",
                    },
                    "op": {
                        "name": "GTE",
                        "args": ["LEFT_INCLUSIVE"],
                    },
                    "right": [
                        {
                            "value": 1000000000,
                            "variable": {
                                "name": "today",
                                "lookback": "ONE_WEEK",
                                "modifier": {
                                    "args": [30, "DAY"],
                                    "name": "SUB",
                                },
                                "period": "QUARTER",
                            },
                        }
                    ],
                }
            ],
            page_size=25,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by={
                "name": "market_cap",
                "lookback": "ONE_WEEK",
                "period": "QUARTER",
                "value_type": "DECIMAL",
            },
            sort_case_sensitive=True,
            sort_direction="ASC",
            sorts=[
                {
                    "field": {
                        "name": "market_cap",
                        "lookback": "ONE_WEEK",
                        "period": "QUARTER",
                        "value_type": "DECIMAL",
                    },
                    "direction": "DESC",
                }
            ],
        )
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_screener(self, client: ClearStreet) -> None:
        response = client.v1.screener.with_raw_response.search_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = response.parse()
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_screener(self, client: ClearStreet) -> None:
        with client.v1.screener.with_streaming_response.search_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = response.parse()
            assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScreener:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_screener(self, async_client: AsyncClearStreet) -> None:
        screener = await async_client.v1.screener.get_screener()
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_screener_with_all_params(self, async_client: AsyncClearStreet) -> None:
        screener = await async_client.v1.screener.get_screener(
            field_filter=["string"],
            filter={"foo": "string"},
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_screener(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.screener.with_raw_response.get_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = await response.parse()
        assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_screener(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.screener.with_streaming_response.get_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = await response.parse()
            assert_matches_type(ScreenerGetScreenerResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_screener(self, async_client: AsyncClearStreet) -> None:
        screener = await async_client.v1.screener.search_screener()
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_screener_with_all_params(self, async_client: AsyncClearStreet) -> None:
        screener = await async_client.v1.screener.search_screener(
            field_filter=[
                {
                    "name": "market_cap",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
                {
                    "name": "price",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
                {
                    "name": "volume",
                    "lookback": "ONE_WEEK",
                    "period": "QUARTER",
                    "value_type": "DECIMAL",
                },
            ],
            filters=[
                {
                    "left": {
                        "name": "market_cap",
                        "lookback": "ONE_WEEK",
                        "period": "QUARTER",
                        "value_type": "DECIMAL",
                    },
                    "op": {
                        "name": "GTE",
                        "args": ["LEFT_INCLUSIVE"],
                    },
                    "right": [
                        {
                            "value": 1000000000,
                            "variable": {
                                "name": "today",
                                "lookback": "ONE_WEEK",
                                "modifier": {
                                    "args": [30, "DAY"],
                                    "name": "SUB",
                                },
                                "period": "QUARTER",
                            },
                        }
                    ],
                }
            ],
            page_size=25,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by={
                "name": "market_cap",
                "lookback": "ONE_WEEK",
                "period": "QUARTER",
                "value_type": "DECIMAL",
            },
            sort_case_sensitive=True,
            sort_direction="ASC",
            sorts=[
                {
                    "field": {
                        "name": "market_cap",
                        "lookback": "ONE_WEEK",
                        "period": "QUARTER",
                        "value_type": "DECIMAL",
                    },
                    "direction": "DESC",
                }
            ],
        )
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_screener(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.screener.with_raw_response.search_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = await response.parse()
        assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_screener(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.screener.with_streaming_response.search_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = await response.parse()
            assert_matches_type(ScreenerSearchScreenerResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True
