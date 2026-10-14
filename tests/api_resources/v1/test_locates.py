# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet._utils import parse_date
from clearstreet.types.v1 import (
    LocateGetLocatesResponse,
    LocateGetLocateByIDResponse,
    LocateGetLocateRatesResponse,
    LocateGetLocateRateByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_locate_by_id(self, client: ClearStreet) -> None:
        locate = client.v1.locates.get_locate_by_id(
            id="id",
            account_id=0,
        )
        assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

    @parametrize
    def test_raw_response_get_locate_by_id(self, client: ClearStreet) -> None:
        response = client.v1.locates.with_raw_response.get_locate_by_id(
            id="id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

    @parametrize
    def test_streaming_response_get_locate_by_id(self, client: ClearStreet) -> None:
        with client.v1.locates.with_streaming_response.get_locate_by_id(
            id="id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_locate_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.locates.with_raw_response.get_locate_by_id(
                id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_locate_rate_by_id(self, client: ClearStreet) -> None:
        locate = client.v1.locates.get_locate_rate_by_id(
            "x",
        )
        assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

    @parametrize
    def test_raw_response_get_locate_rate_by_id(self, client: ClearStreet) -> None:
        response = client.v1.locates.with_raw_response.get_locate_rate_by_id(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

    @parametrize
    def test_streaming_response_get_locate_rate_by_id(self, client: ClearStreet) -> None:
        with client.v1.locates.with_streaming_response.get_locate_rate_by_id(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_locate_rate_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.locates.with_raw_response.get_locate_rate_by_id(
                "",
            )

    @parametrize
    def test_method_get_locate_rates(self, client: ClearStreet) -> None:
        locate = client.v1.locates.get_locate_rates(
            instrument_ids=["x"],
        )
        assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

    @parametrize
    def test_raw_response_get_locate_rates(self, client: ClearStreet) -> None:
        response = client.v1.locates.with_raw_response.get_locate_rates(
            instrument_ids=["x"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

    @parametrize
    def test_streaming_response_get_locate_rates(self, client: ClearStreet) -> None:
        with client.v1.locates.with_streaming_response.get_locate_rates(
            instrument_ids=["x"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_locates(self, client: ClearStreet) -> None:
        locate = client.v1.locates.get_locates(
            account_id=0,
        )
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    def test_method_get_locates_with_all_params(self, client: ClearStreet) -> None:
        locate = client.v1.locates.get_locates(
            account_id=0,
            effective_date=parse_date("2019-12-27"),
            instrument_ids=["x"],
            status=["REQUESTED"],
        )
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    def test_raw_response_get_locates(self, client: ClearStreet) -> None:
        response = client.v1.locates.with_raw_response.get_locates(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = response.parse()
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    def test_streaming_response_get_locates(self, client: ClearStreet) -> None:
        with client.v1.locates.with_streaming_response.get_locates(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = response.parse()
            assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_locate_by_id(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.v1.locates.get_locate_by_id(
            id="id",
            account_id=0,
        )
        assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

    @parametrize
    async def test_raw_response_get_locate_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.locates.with_raw_response.get_locate_by_id(
            id="id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

    @parametrize
    async def test_streaming_response_get_locate_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.locates.with_streaming_response.get_locate_by_id(
            id="id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateGetLocateByIDResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_locate_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.locates.with_raw_response.get_locate_by_id(
                id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_locate_rate_by_id(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.v1.locates.get_locate_rate_by_id(
            "x",
        )
        assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

    @parametrize
    async def test_raw_response_get_locate_rate_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.locates.with_raw_response.get_locate_rate_by_id(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

    @parametrize
    async def test_streaming_response_get_locate_rate_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.locates.with_streaming_response.get_locate_rate_by_id(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateGetLocateRateByIDResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_locate_rate_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.locates.with_raw_response.get_locate_rate_by_id(
                "",
            )

    @parametrize
    async def test_method_get_locate_rates(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.v1.locates.get_locate_rates(
            instrument_ids=["x"],
        )
        assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

    @parametrize
    async def test_raw_response_get_locate_rates(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.locates.with_raw_response.get_locate_rates(
            instrument_ids=["x"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

    @parametrize
    async def test_streaming_response_get_locate_rates(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.locates.with_streaming_response.get_locate_rates(
            instrument_ids=["x"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateGetLocateRatesResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_locates(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.v1.locates.get_locates(
            account_id=0,
        )
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    async def test_method_get_locates_with_all_params(self, async_client: AsyncClearStreet) -> None:
        locate = await async_client.v1.locates.get_locates(
            account_id=0,
            effective_date=parse_date("2019-12-27"),
            instrument_ids=["x"],
            status=["REQUESTED"],
        )
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    async def test_raw_response_get_locates(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.locates.with_raw_response.get_locates(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate = await response.parse()
        assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

    @parametrize
    async def test_streaming_response_get_locates(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.locates.with_streaming_response.get_locates(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate = await response.parse()
            assert_matches_type(LocateGetLocatesResponse, locate, path=["response"])

        assert cast(Any, response.is_closed) is True
