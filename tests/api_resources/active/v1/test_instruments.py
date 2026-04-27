# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1 import (
    InstrumentSearchResponse,
    InstrumentGetInstrumentsResponse,
    InstrumentGetInstrumentByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstruments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_by_id(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_by_id_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
            include_options_expiry_dates=True,
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_by_id(self, client: ClearStreet) -> None:
        response = client.active.v1.instruments.with_raw_response.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_by_id(self, client: ClearStreet) -> None:
        with client.active.v1.instruments.with_streaming_response.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            client.active.v1.instruments.with_raw_response.get_instrument_by_id(
                security_id="",
                security_id_source="CMS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instruments(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.get_instruments()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instruments_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.get_instruments(
            easy_to_borrow=True,
            id_filter="id_filter",
            instrument_type="COMMON_STOCK",
            is_liquidation_only=True,
            is_marginable=True,
            is_restricted=True,
            is_short_prohibited=True,
            is_threshold_security=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            security_id=["string"],
            security_id_source=["string"],
        )
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instruments(self, client: ClearStreet) -> None:
        response = client.active.v1.instruments.with_raw_response.get_instruments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instruments(self, client: ClearStreet) -> None:
        with client.active.v1.instruments.with_streaming_response.get_instruments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.search(
            q="q",
        )
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: ClearStreet) -> None:
        instrument = client.active.v1.instruments.search(
            q="q",
            asset_class="asset_class",
            country="country",
            currency="currency",
            cursor="cursor",
            include_inactive=True,
            include_restricted=True,
            limit=0,
        )
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: ClearStreet) -> None:
        response = client.active.v1.instruments.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: ClearStreet) -> None:
        with client.active.v1.instruments.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstruments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_by_id_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
            include_options_expiry_dates=True,
        )
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.with_raw_response.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.instruments.with_streaming_response.get_instrument_by_id(
            security_id="security_id",
            security_id_source="CMS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentGetInstrumentByIDResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            await async_client.active.v1.instruments.with_raw_response.get_instrument_by_id(
                security_id="",
                security_id_source="CMS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instruments(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.get_instruments()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instruments_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.get_instruments(
            easy_to_borrow=True,
            id_filter="id_filter",
            instrument_type="COMMON_STOCK",
            is_liquidation_only=True,
            is_marginable=True,
            is_restricted=True,
            is_short_prohibited=True,
            is_threshold_security=True,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            security_id=["string"],
            security_id_source=["string"],
        )
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instruments(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.with_raw_response.get_instruments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instruments(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.instruments.with_streaming_response.get_instruments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentGetInstrumentsResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.search(
            q="q",
        )
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument = await async_client.active.v1.instruments.search(
            q="q",
            asset_class="asset_class",
            country="country",
            currency="currency",
            cursor="cursor",
            include_inactive=True,
            include_restricted=True,
            limit=0,
        )
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.instruments.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(InstrumentSearchResponse, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True
