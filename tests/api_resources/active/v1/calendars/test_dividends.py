# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.calendars import (
    DividendGetDividendsCalendarResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDividends:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_dividends_calendar(self, client: ClearStreet) -> None:
        dividend = client.active.v1.calendars.dividends.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_dividends_calendar(self, client: ClearStreet) -> None:
        response = client.active.v1.calendars.dividends.with_raw_response.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dividend = response.parse()
        assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_dividends_calendar(self, client: ClearStreet) -> None:
        with client.active.v1.calendars.dividends.with_streaming_response.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dividend = response.parse()
            assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDividends:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_dividends_calendar(self, async_client: AsyncClearStreet) -> None:
        dividend = await async_client.active.v1.calendars.dividends.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_dividends_calendar(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.calendars.dividends.with_raw_response.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dividend = await response.parse()
        assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_dividends_calendar(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.calendars.dividends.with_streaming_response.get_dividends_calendar(
            from_date="from_date",
            to_date="to_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dividend = await response.parse()
            assert_matches_type(DividendGetDividendsCalendarResponse, dividend, path=["response"])

        assert cast(Any, response.is_closed) is True
