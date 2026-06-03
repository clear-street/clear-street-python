# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet._utils import parse_date
from clearstreet.types.v1 import (
    InstrumentDataGetInstrumentEventsResponse,
    InstrumentDataGetAllInstrumentEventsResponse,
    InstrumentDataGetInstrumentFundamentalsResponse,
    InstrumentDataGetInstrumentAnalystConsensusResponse,
    InstrumentDataGetInstrumentIncomeStatementsResponse,
    InstrumentDataGetInstrumentCashFlowStatementsResponse,
    InstrumentDataGetInstrumentBalanceSheetStatementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstrumentData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_instrument_events(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_all_instrument_events()
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_instrument_events_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_all_instrument_events(
            event_types=["EARNINGS"],
            from_date="from_date",
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_all_instrument_events(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_all_instrument_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_all_instrument_events(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_all_instrument_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_analyst_consensus_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_=parse_date("2019-12-27"),
            to=parse_date("2019-12-27"),
        )
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_analyst_consensus(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_balance_sheet_statements_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(
                InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_balance_sheet_statements(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_balance_sheet_statements(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_cash_flow_statements(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_cash_flow_statements_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_cash_flow_statements(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_cash_flow_statements(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(
                InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_cash_flow_statements(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_cash_flow_statements(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_events(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_events_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_events(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_events(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_events(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_events(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_fundamentals(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_fundamentals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_income_statements(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_income_statements_with_all_params(self, client: ClearStreet) -> None:
        instrument_data = client.v1.instrument_data.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_income_statements(self, client: ClearStreet) -> None:
        response = client.v1.instrument_data.with_raw_response.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = response.parse()
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_income_statements(self, client: ClearStreet) -> None:
        with client.v1.instrument_data.with_streaming_response.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = response.parse()
            assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_income_statements(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.instrument_data.with_raw_response.get_instrument_income_statements(
                instrument_id="",
            )


class TestAsyncInstrumentData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_all_instrument_events()
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_instrument_events_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_all_instrument_events(
            event_types=["EARNINGS"],
            from_date="from_date",
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_all_instrument_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_instrument_events(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_all_instrument_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(InstrumentDataGetAllInstrumentEventsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_analyst_consensus_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_=parse_date("2019-12-27"),
            to=parse_date("2019-12-27"),
        )
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_analyst_consensus(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(InstrumentDataGetInstrumentAnalystConsensusResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_analyst_consensus(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_balance_sheet_statements_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(
            InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_balance_sheet_statements(
        self, async_client: AsyncClearStreet
    ) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_balance_sheet_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(
                InstrumentDataGetInstrumentBalanceSheetStatementsResponse, instrument_data, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_balance_sheet_statements(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_balance_sheet_statements(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_cash_flow_statements(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_cash_flow_statements_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_cash_flow_statements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_cash_flow_statements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_cash_flow_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(
                InstrumentDataGetInstrumentCashFlowStatementsResponse, instrument_data, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_cash_flow_statements(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_cash_flow_statements(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_events_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_events(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(InstrumentDataGetInstrumentEventsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_events(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_events(
                instrument_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_fundamentals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(InstrumentDataGetInstrumentFundamentalsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_fundamentals(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_fundamentals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_income_statements(self, async_client: AsyncClearStreet) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_income_statements_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        instrument_data = await async_client.v1.instrument_data.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_date="from_date",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to_date="to_date",
        )
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_income_statements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.instrument_data.with_raw_response.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument_data = await response.parse()
        assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_income_statements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.instrument_data.with_streaming_response.get_instrument_income_statements(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument_data = await response.parse()
            assert_matches_type(InstrumentDataGetInstrumentIncomeStatementsResponse, instrument_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_income_statements(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.instrument_data.with_raw_response.get_instrument_income_statements(
                instrument_id="",
            )
