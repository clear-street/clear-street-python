# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1 import APIVersionGetVersionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_version(self, client: ClearStreet) -> None:
        api_version = client.v1.api_version.get_version()
        assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_version(self, client: ClearStreet) -> None:
        response = client.v1.api_version.with_raw_response.get_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_version = response.parse()
        assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_version(self, client: ClearStreet) -> None:
        with client.v1.api_version.with_streaming_response.get_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_version = response.parse()
            assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIVersion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_version(self, async_client: AsyncClearStreet) -> None:
        api_version = await async_client.v1.api_version.get_version()
        assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_version(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.api_version.with_raw_response.get_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_version = await response.parse()
        assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_version(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.api_version.with_streaming_response.get_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_version = await response.parse()
            assert_matches_type(APIVersionGetVersionResponse, api_version, path=["response"])

        assert cast(Any, response.is_closed) is True
