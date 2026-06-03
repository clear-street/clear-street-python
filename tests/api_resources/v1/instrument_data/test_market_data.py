# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.instrument_data import (
    MarketDataGetSnapshotsResponse,
    MarketDataGetDailySummariesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_summaries(self, client: ClearStreet) -> None:
        market_data = client.v1.instrument_data.market_data.get_daily_summaries(
            instrument_ids="instrument_ids",
        )
        assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_summaries(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.market_data.with_raw_response.get_daily_summaries(
            instrument_ids="instrument_ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_data = response.parse()
        assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_summaries(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.market_data.with_streaming_response.get_daily_summaries(
            instrument_ids="instrument_ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_data = response.parse()
            assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_snapshots(self, client: ClearStreet) -> None:
        market_data = client.v1.instrument_data.market_data.get_snapshots()
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_snapshots_with_all_params(self, client: ClearStreet) -> None:
        market_data = client.v1.instrument_data.market_data.get_snapshots(
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_snapshots(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.market_data.with_raw_response.get_snapshots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_data = response.parse()
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_snapshots(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.market_data.with_streaming_response.get_snapshots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_data = response.parse()
            assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_summaries(self, async_client: AsyncClearStreet) -> None:
        market_data = await async_client.v1.instrument_data.market_data.get_daily_summaries(
            instrument_ids="instrument_ids",
        )
        assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_summaries(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.market_data.with_raw_response.get_daily_summaries(
            instrument_ids="instrument_ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_data = await response.parse()
        assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_summaries(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.market_data.with_streaming_response.get_daily_summaries(
            instrument_ids="instrument_ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_data = await response.parse()
            assert_matches_type(MarketDataGetDailySummariesResponse, market_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        market_data = await async_client.v1.instrument_data.market_data.get_snapshots()
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_snapshots_with_all_params(self, async_client: AsyncClearStreet) -> None:
        market_data = await async_client.v1.instrument_data.market_data.get_snapshots(
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.market_data.with_raw_response.get_snapshots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_data = await response.parse()
        assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.market_data.with_streaming_response.get_snapshots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_data = await response.parse()
            assert_matches_type(MarketDataGetSnapshotsResponse, market_data, path=["response"])

        assert cast(Any, response.is_closed) is True
