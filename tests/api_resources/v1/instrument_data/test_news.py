# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.instrument_data import NewsGetNewsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_news(self, client: ClearStreet) -> None:
        news = client.v1.instrument_data.news.get_news()
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_news_with_all_params(self, client: ClearStreet) -> None:
        news = client.v1.instrument_data.news.get_news(
            exclude_publishers="exclude_publishers",
            from_="from",
            include_publishers="include_publishers",
            instrument_ids=["string"],
            news_type="NEWS",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            search_query="search_query",
            sectors=["BASIC_MATERIALS"],
            to="to",
        )
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_news(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.news.with_raw_response.get_news()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_news(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.news.with_streaming_response.get_news() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsGetNewsResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_news(self, async_client: AsyncClearStreet) -> None:
        news = await async_client.v1.instrument_data.news.get_news()
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_news_with_all_params(self, async_client: AsyncClearStreet) -> None:
        news = await async_client.v1.instrument_data.news.get_news(
            exclude_publishers="exclude_publishers",
            from_="from",
            include_publishers="include_publishers",
            instrument_ids=["string"],
            news_type="NEWS",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            search_query="search_query",
            sectors=["BASIC_MATERIALS"],
            to="to",
        )
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_news(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.news.with_raw_response.get_news()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsGetNewsResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_news(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.news.with_streaming_response.get_news() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsGetNewsResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
