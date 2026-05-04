# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_date
from clear_street.types.v1.instruments import OptionContractsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contracts(self, client: ClearStreet) -> None:
        option = client.v1.instruments.options.contracts()
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contracts_with_all_params(self, client: ClearStreet) -> None:
        option = client.v1.instruments.options.contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlier_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_contracts(self, client: ClearStreet) -> None:
        response = client.v1.instruments.options.with_raw_response.contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_contracts(self, client: ClearStreet) -> None:
        with client.v1.instruments.options.with_streaming_response.contracts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionContractsResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contracts(self, async_client: AsyncClearStreet) -> None:
        option = await async_client.v1.instruments.options.contracts()
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contracts_with_all_params(self, async_client: AsyncClearStreet) -> None:
        option = await async_client.v1.instruments.options.contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlier_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_contracts(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.options.with_raw_response.contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionContractsResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_contracts(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.options.with_streaming_response.contracts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionContractsResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True
