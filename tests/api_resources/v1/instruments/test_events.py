# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.instruments import (
    EventGetInstrumentEventsResponse,
    EventGetAllInstrumentEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_instrument_events(self, client: ClearStreet) -> None:
        event = client.v1.instruments.events.get_all_instrument_events()
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_instrument_events_with_all_params(self, client: ClearStreet) -> None:
        event = client.v1.instruments.events.get_all_instrument_events(
            event_types=["EARNINGS"],
            from_date="from_date",
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            to_date="to_date",
        )
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_all_instrument_events(self, client: ClearStreet) -> None:
        response = client.v1.instruments.events.with_raw_response.get_all_instrument_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_all_instrument_events(self, client: ClearStreet) -> None:
        with client.v1.instruments.events.with_streaming_response.get_all_instrument_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_events(self, client: ClearStreet) -> None:
        event = client.v1.instruments.events.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_events_with_all_params(self, client: ClearStreet) -> None:
        event = client.v1.instruments.events.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_events(self, client: ClearStreet) -> None:
        response = client.v1.instruments.events.with_raw_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_events(self, client: ClearStreet) -> None:
        with client.v1.instruments.events.with_streaming_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_events(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instruments.events.with_raw_response.get_instrument_events(
                instrument_id="",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        event = await async_client.v1.instruments.events.get_all_instrument_events()
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_instrument_events_with_all_params(self, async_client: AsyncClearStreet) -> None:
        event = await async_client.v1.instruments.events.get_all_instrument_events(
            event_types=["EARNINGS"],
            from_date="from_date",
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            to_date="to_date",
        )
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.events.with_raw_response.get_all_instrument_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.events.with_streaming_response.get_all_instrument_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetAllInstrumentEventsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        event = await async_client.v1.instruments.events.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_events_with_all_params(self, async_client: AsyncClearStreet) -> None:
        event = await async_client.v1.instruments.events.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.events.with_raw_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.events.with_streaming_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetInstrumentEventsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instruments.events.with_raw_response.get_instrument_events(
                instrument_id="",
            )
