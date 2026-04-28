# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.instruments import (
    BalanceSheetGetInstrumentBalanceSheetStatementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalanceSheets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        balance_sheet = client.active.v1.instruments.balance_sheets.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_balance_sheet_statements_with_all_params(self, client: ClearStreet) -> None:
        balance_sheet = client.active.v1.instruments.balance_sheets.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        response = (
            client.active.v1.instruments.balance_sheets.with_raw_response.get_instrument_balance_sheet_statements(
                security_id="security_id",
                security_id_source="CMS",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_sheet = response.parse()
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        with (
            client.active.v1.instruments.balance_sheets.with_streaming_response.get_instrument_balance_sheet_statements(
                security_id="security_id",
                security_id_source="CMS",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_sheet = response.parse()
            assert_matches_type(
                BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            client.active.v1.instruments.balance_sheets.with_raw_response.get_instrument_balance_sheet_statements(
                security_id="",
                security_id_source="CMS",
            )


class TestAsyncBalanceSheets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        balance_sheet = await async_client.active.v1.instruments.balance_sheets.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_balance_sheet_statements_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        balance_sheet = await async_client.active.v1.instruments.balance_sheets.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.balance_sheets.with_raw_response.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_sheet = await response.parse()
        assert_matches_type(BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_balance_sheet_statements(
        self, async_client: AsyncClearStreet
    ) -> None:
        async with async_client.active.v1.instruments.balance_sheets.with_streaming_response.get_instrument_balance_sheet_statements(
            security_id="security_id",
            security_id_source="CMS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_sheet = await response.parse()
            assert_matches_type(
                BalanceSheetGetInstrumentBalanceSheetStatementsResponse, balance_sheet, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            await async_client.active.v1.instruments.balance_sheets.with_raw_response.get_instrument_balance_sheet_statements(
                security_id="",
                security_id_source="CMS",
            )
