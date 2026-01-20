# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.calendars import (
    SummaryGetCalendarSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_calendar_summary(self, client: ClearStreet) -> None:
        summary = client.active.v1.calendars.summary.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_calendar_summary(self, client: ClearStreet) -> None:
        response = client.active.v1.calendars.summary.with_raw_response.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_calendar_summary(self, client: ClearStreet) -> None:
        with client.active.v1.calendars.summary.with_streaming_response.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_calendar_summary(self, async_client: AsyncClearStreet) -> None:
        summary = await async_client.active.v1.calendars.summary.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_calendar_summary(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.calendars.summary.with_raw_response.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_calendar_summary(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.calendars.summary.with_streaming_response.get_calendar_summary(
            from_date="from_date",
            to_date="to_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetCalendarSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
