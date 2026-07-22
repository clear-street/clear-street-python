# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet._utils import parse_date
from clearstreet.types.v1 import (
    InstrumentGetInstrumentsResponse,
    InstrumentGetInstrumentByIDResponse,
    InstrumentSearchInstrumentsResponse,
    InstrumentGetOptionContractsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstruments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_instrument_by_id(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    def test_method_get_instrument_by_id_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_options_expiry_dates=True,
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    def test_raw_response_get_instrument_by_id(self, client: ClearStreet) -> None:
        response = client.v1.instruments.with_raw_response.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    def test_streaming_response_get_instrument_by_id(self, client: ClearStreet) -> None:
        with client.v1.instruments.with_streaming_response.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_instrument_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instruments.with_raw_response.get_instrument_by_id(
                instrument_id="",
            )

    @parametrize
    def test_method_get_instruments(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_instruments()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_method_get_instruments_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_instruments(
            easy_to_borrow=True,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            is_liquidation_only=True,
            is_marginable=True,
            is_ptp=True,
            is_short_prohibited=True,
            is_threshold_security=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_raw_response_get_instruments(self, client: ClearStreet) -> None:
        response = client.v1.instruments.with_raw_response.get_instruments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_streaming_response_get_instruments(self, client: ClearStreet) -> None:
        with client.v1.instruments.with_streaming_response.get_instruments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_option_contracts(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_option_contracts()
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    def test_method_get_option_contracts_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.get_option_contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlying_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    def test_raw_response_get_option_contracts(self, client: ClearStreet) -> None:
        response = client.v1.instruments.with_raw_response.get_option_contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    def test_streaming_response_get_option_contracts(self, client: ClearStreet) -> None:
        with client.v1.instruments.with_streaming_response.get_option_contracts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_instruments(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.search_instruments(
            q="q",
        )
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_method_search_instruments_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.v1.instruments.search_instruments(
            q="q",
            asset_class="asset_class",
            country="country",
            currency="currency",
            include_inactive=True,
            include_ptp=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_raw_response_search_instruments(self, client: ClearStreet) -> None:
        response = client.v1.instruments.with_raw_response.search_instruments(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    def test_streaming_response_search_instruments(self, client: ClearStreet) -> None:
        with client.v1.instruments.with_streaming_response.search_instruments(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstruments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    async def test_method_get_instrument_by_id_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_options_expiry_dates=True,
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    async def test_raw_response_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.with_raw_response.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @parametrize
    async def test_streaming_response_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.with_streaming_response.get_instrument_by_id(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instruments.with_raw_response.get_instrument_by_id(
                instrument_id="",
            )

    @parametrize
    async def test_method_get_instruments(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_instruments()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_method_get_instruments_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_instruments(
            easy_to_borrow=True,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            is_liquidation_only=True,
            is_marginable=True,
            is_ptp=True,
            is_short_prohibited=True,
            is_threshold_security=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_raw_response_get_instruments(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.with_raw_response.get_instruments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_streaming_response_get_instruments(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.with_streaming_response.get_instruments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_option_contracts()
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    async def test_method_get_option_contracts_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.get_option_contracts(
            contract_type="CALL",
            expiry=parse_date("2019-12-27"),
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            underlier="underlier",
            underlying_instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    async def test_raw_response_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.with_raw_response.get_option_contracts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

    @parametrize
    async def test_streaming_response_get_option_contracts(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.with_streaming_response.get_option_contracts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentGetOptionContractsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_instruments(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.search_instruments(
            q="q",
        )
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_method_search_instruments_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.v1.instruments.search_instruments(
            q="q",
            asset_class="asset_class",
            country="country",
            currency="currency",
            include_inactive=True,
            include_ptp=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_raw_response_search_instruments(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instruments.with_raw_response.search_instruments(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

    @parametrize
    async def test_streaming_response_search_instruments(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instruments.with_streaming_response.search_instruments(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentSearchInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True
