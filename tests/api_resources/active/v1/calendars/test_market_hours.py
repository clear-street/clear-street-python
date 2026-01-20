# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.calendars import (
    MarketHourGetMarketHoursCalendarResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketHours:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_market_hours_calendar(self, client: ClearStreet) -> None:
        market_hour = client.active.v1.calendars.market_hours.get_market_hours_calendar(
            date="date",
        )
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_market_hours_calendar_with_all_params(self, client: ClearStreet) -> None:
        market_hour = client.active.v1.calendars.market_hours.get_market_hours_calendar(
            date="date",
            venue="venue",
        )
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_market_hours_calendar(self, client: ClearStreet) -> None:
        response = client.active.v1.calendars.market_hours.with_raw_response.get_market_hours_calendar(
            date="date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_hour = response.parse()
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_market_hours_calendar(self, client: ClearStreet) -> None:
        with client.active.v1.calendars.market_hours.with_streaming_response.get_market_hours_calendar(
            date="date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_hour = response.parse()
            assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketHours:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        market_hour = await async_client.active.v1.calendars.market_hours.get_market_hours_calendar(
            date="date",
        )
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_market_hours_calendar_with_all_params(self, async_client: AsyncClearStreet) -> None:
        market_hour = await async_client.active.v1.calendars.market_hours.get_market_hours_calendar(
            date="date",
            venue="venue",
        )
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.calendars.market_hours.with_raw_response.get_market_hours_calendar(
            date="date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_hour = await response.parse()
        assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.calendars.market_hours.with_streaming_response.get_market_hours_calendar(
            date="date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_hour = await response.parse()
            assert_matches_type(MarketHourGetMarketHoursCalendarResponse, market_hour, path=["response"])

        assert cast(Any, response.is_closed) is True
