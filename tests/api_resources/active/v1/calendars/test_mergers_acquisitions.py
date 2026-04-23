# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_date
from clear_street.types.active.v1.calendars import (
    MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMergersAcquisitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_mergers_and_acquisitions_calendar(self, client: ClearStreet) -> None:
        mergers_acquisition = client.active.v1.calendars.mergers_acquisitions.get_mergers_and_acquisitions_calendar()
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_mergers_and_acquisitions_calendar_with_all_params(self, client: ClearStreet) -> None:
        mergers_acquisition = client.active.v1.calendars.mergers_acquisitions.get_mergers_and_acquisitions_calendar(
            from_=parse_date("2019-12-27"),
            to=parse_date("2019-12-27"),
        )
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_mergers_and_acquisitions_calendar(self, client: ClearStreet) -> None:
        response = (
            client.active.v1.calendars.mergers_acquisitions.with_raw_response.get_mergers_and_acquisitions_calendar()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mergers_acquisition = response.parse()
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_mergers_and_acquisitions_calendar(self, client: ClearStreet) -> None:
        with client.active.v1.calendars.mergers_acquisitions.with_streaming_response.get_mergers_and_acquisitions_calendar() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mergers_acquisition = response.parse()
            assert_matches_type(
                MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncMergersAcquisitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_mergers_and_acquisitions_calendar(self, async_client: AsyncClearStreet) -> None:
        mergers_acquisition = (
            await async_client.active.v1.calendars.mergers_acquisitions.get_mergers_and_acquisitions_calendar()
        )
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_mergers_and_acquisitions_calendar_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        mergers_acquisition = (
            await async_client.active.v1.calendars.mergers_acquisitions.get_mergers_and_acquisitions_calendar(
                from_=parse_date("2019-12-27"),
                to=parse_date("2019-12-27"),
            )
        )
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_mergers_and_acquisitions_calendar(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.calendars.mergers_acquisitions.with_raw_response.get_mergers_and_acquisitions_calendar()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mergers_acquisition = await response.parse()
        assert_matches_type(
            MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_mergers_and_acquisitions_calendar(
        self, async_client: AsyncClearStreet
    ) -> None:
        async with async_client.active.v1.calendars.mergers_acquisitions.with_streaming_response.get_mergers_and_acquisitions_calendar() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mergers_acquisition = await response.parse()
            assert_matches_type(
                MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse, mergers_acquisition, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
