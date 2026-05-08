# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1 import (
    CalendarGetClockResponse,
    CalendarGetMarketHoursCalendarResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalendar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_clock(self, client: ClearStreet) -> None:
        calendar = client.v1.calendar.get_clock()
        assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_clock(self, client: ClearStreet) -> None:
        response = client.v1.calendar.with_raw_response.get_clock()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = response.parse()
        assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_clock(self, client: ClearStreet) -> None:
        with client.v1.calendar.with_streaming_response.get_clock() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = response.parse()
            assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_market_hours_calendar(self, client: ClearStreet) -> None:
        calendar = client.v1.calendar.get_market_hours_calendar(
            date="date",
        )
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_market_hours_calendar_with_all_params(self, client: ClearStreet) -> None:
        calendar = client.v1.calendar.get_market_hours_calendar(
            date="date",
            market="us_equities",
        )
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_market_hours_calendar(self, client: ClearStreet) -> None:
        response = client.v1.calendar.with_raw_response.get_market_hours_calendar(
            date="date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = response.parse()
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_market_hours_calendar(self, client: ClearStreet) -> None:
        with client.v1.calendar.with_streaming_response.get_market_hours_calendar(
            date="date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = response.parse()
            assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalendar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_clock(self, async_client: AsyncClearStreet) -> None:
        calendar = await async_client.v1.calendar.get_clock()
        assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_clock(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.calendar.with_raw_response.get_clock()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = await response.parse()
        assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_clock(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.calendar.with_streaming_response.get_clock() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = await response.parse()
            assert_matches_type(CalendarGetClockResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        calendar = await async_client.v1.calendar.get_market_hours_calendar(
            date="date",
        )
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_market_hours_calendar_with_all_params(self, async_client: AsyncClearStreet) -> None:
        calendar = await async_client.v1.calendar.get_market_hours_calendar(
            date="date",
            market="us_equities",
        )
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.calendar.with_raw_response.get_market_hours_calendar(
            date="date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = await response.parse()
        assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_market_hours_calendar(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.calendar.with_streaming_response.get_market_hours_calendar(
            date="date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = await response.parse()
            assert_matches_type(CalendarGetMarketHoursCalendarResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True
