# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clear_street import ClearStreet, AsyncClearStreet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebsocket:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_websocket_handler(self, client: ClearStreet) -> None:
        websocket = client.v1.websocket.websocket_handler()
        assert websocket is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_websocket_handler(self, client: ClearStreet) -> None:
        response = client.v1.websocket.with_raw_response.websocket_handler()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websocket = response.parse()
        assert websocket is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_websocket_handler(self, client: ClearStreet) -> None:
        with client.v1.websocket.with_streaming_response.websocket_handler() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websocket = response.parse()
            assert websocket is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWebsocket:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_websocket_handler(self, async_client: AsyncClearStreet) -> None:
        websocket = await async_client.v1.websocket.websocket_handler()
        assert websocket is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_websocket_handler(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.websocket.with_raw_response.websocket_handler()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websocket = await response.parse()
        assert websocket is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_websocket_handler(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.websocket.with_streaming_response.websocket_handler() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websocket = await response.parse()
            assert websocket is None

        assert cast(Any, response.is_closed) is True
