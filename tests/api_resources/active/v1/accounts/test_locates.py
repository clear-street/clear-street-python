# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.accounts import (
    LocateGetLocateRequestsResponse,
    LocateCreateLocateRequestResponse,
    LocateUpdateLocateRequestResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_locate_request(self, client: ClearStreet) -> None:
        locate = client.active.v1.accounts.locates.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        )
        assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_locate_request(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.locates.with_raw_response.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_locate_request(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.locates.with_streaming_response.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_locate_requests(self, client: ClearStreet) -> None:
        locate = client.active.v1.accounts.locates.get_locate_requests(
            account_id=0,
        )
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_locate_requests_with_all_params(self, client: ClearStreet) -> None:
        locate = client.active.v1.accounts.locates.get_locate_requests(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            reference_id="reference_id",
            status="PENDING",
        )
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_locate_requests(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.locates.with_raw_response.get_locate_requests(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_locate_requests(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.locates.with_streaming_response.get_locate_requests(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_locate_request(self, client: ClearStreet) -> None:
        locate = client.active.v1.accounts.locates.update_locate_request(
            account_id=0,
            accept=True,
        )
        assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_locate_request(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.locates.with_raw_response.update_locate_request(
            account_id=0,
            accept=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_locate_request(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.locates.with_streaming_response.update_locate_request(
            account_id=0,
            accept=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_locate_request(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.active.v1.accounts.locates.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        )
        assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_locate_request(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.locates.with_raw_response.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_locate_request(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.locates.with_streaming_response.create_locate_request(
            account_id=0,
            body=[
                {
                    "quantity": 500,
                    "symbol": "AAPL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateCreateLocateRequestResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_locate_requests(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.active.v1.accounts.locates.get_locate_requests(
            account_id=0,
        )
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_locate_requests_with_all_params(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.active.v1.accounts.locates.get_locate_requests(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            reference_id="reference_id",
            status="PENDING",
        )
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_locate_requests(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.locates.with_raw_response.get_locate_requests(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_locate_requests(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.locates.with_streaming_response.get_locate_requests(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateGetLocateRequestsResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_locate_request(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.active.v1.accounts.locates.update_locate_request(
            account_id=0,
            accept=True,
        )
        assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_locate_request(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.locates.with_raw_response.update_locate_request(
            account_id=0,
            accept=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_locate_request(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.locates.with_streaming_response.update_locate_request(
            account_id=0,
            accept=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateUpdateLocateRequestResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True
