# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_date
from clear_street.types.active.v1.instruments.options import (
    ContractGetOptionContractsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_option_contracts(self, client: ClearStreet) -> None:
        contract = client.active.v1.instruments.options.contracts.get_option_contracts()
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_option_contracts_with_all_params(self, client: ClearStreet) -> None:
        contract = client.active.v1.instruments.options.contracts.get_option_contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlier_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            underlier_security_id="underlier_security_id",
            underlier_security_id_source="CMS",
        )
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_option_contracts(self, client: ClearStreet) -> None:
        response = client.active.v1.instruments.options.contracts.with_raw_response.get_option_contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_option_contracts(self, client: ClearStreet) -> None:
        with client.active.v1.instruments.options.contracts.with_streaming_response.get_option_contracts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        contract = await async_client.active.v1.instruments.options.contracts.get_option_contracts()
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_option_contracts_with_all_params(self, async_client: AsyncClearStreet) -> None:
        contract = await async_client.active.v1.instruments.options.contracts.get_option_contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlier_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            underlier_security_id="underlier_security_id",
            underlier_security_id_source="CMS",
        )
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.options.contracts.with_raw_response.get_option_contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        async with (
            async_client.active.v1.instruments.options.contracts.with_streaming_response.get_option_contracts()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractGetOptionContractsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
