# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.instruments import FundamentalGetInstrumentFundamentalsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFundamentals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        fundamental = client.v1.instruments.fundamentals.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        response = client.v1.instruments.fundamentals.with_raw_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fundamental = response.parse()
        assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        with client.v1.instruments.fundamentals.with_streaming_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fundamental = response.parse()
            assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instruments.fundamentals.with_raw_response.get_instrument_fundamentals(
                "",
            )


class TestAsyncFundamentals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        fundamental = await async_client.v1.instruments.fundamentals.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.fundamentals.with_raw_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fundamental = await response.parse()
        assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.fundamentals.with_streaming_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fundamental = await response.parse()
            assert_matches_type(FundamentalGetInstrumentFundamentalsResponse, fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instruments.fundamentals.with_raw_response.get_instrument_fundamentals(
                "",
            )
