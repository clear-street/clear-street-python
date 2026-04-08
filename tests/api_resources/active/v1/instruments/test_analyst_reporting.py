# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_date
from clear_street.types.active.v1.instruments import (
    AnalystReportingGetInstrumentAnalystConsensusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalystReporting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        analyst_reporting = client.active.v1.instruments.analyst_reporting.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_instrument_analyst_consensus_with_all_params(self, client: ClearStreet) -> None:
        analyst_reporting = client.active.v1.instruments.analyst_reporting.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
            from_=parse_date("2019-12-27"),
            to=parse_date("2019-12-27"),
        )
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        response = client.active.v1.instruments.analyst_reporting.with_raw_response.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyst_reporting = response.parse()
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        with client.active.v1.instruments.analyst_reporting.with_streaming_response.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyst_reporting = response.parse()
            assert_matches_type(
                AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_instrument_analyst_consensus(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            client.active.v1.instruments.analyst_reporting.with_raw_response.get_instrument_analyst_consensus(
                security_id="",
                security_id_source="CMS",
            )


class TestAsyncAnalystReporting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        analyst_reporting = await async_client.active.v1.instruments.analyst_reporting.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_instrument_analyst_consensus_with_all_params(
        self, async_client: AsyncClearStreet
    ) -> None:
        analyst_reporting = await async_client.active.v1.instruments.analyst_reporting.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
            from_=parse_date("2019-12-27"),
            to=parse_date("2019-12-27"),
        )
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.instruments.analyst_reporting.with_raw_response.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyst_reporting = await response.parse()
        assert_matches_type(AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.instruments.analyst_reporting.with_streaming_response.get_instrument_analyst_consensus(
            security_id="security_id",
            security_id_source="CMS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyst_reporting = await response.parse()
            assert_matches_type(
                AnalystReportingGetInstrumentAnalystConsensusResponse, analyst_reporting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_instrument_analyst_consensus(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `security_id` but received ''"):
            await (
                async_client.active.v1.instruments.analyst_reporting.with_raw_response.get_instrument_analyst_consensus(
                    security_id="",
                    security_id_source="CMS",
                )
            )
