# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1 import (
    AlertGetAlertsResponse,
    AlertCreateAlertResponse,
    AlertGetAlertByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_alert(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        )
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    def test_method_create_alert_with_all_params(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
            account_id=19816,
        )
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_create_alert(self, client: ClearStreet) -> None:
        response = client.v1.alerts.with_raw_response.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_create_alert(self, client: ClearStreet) -> None:
        with client.v1.alerts.with_streaming_response.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_alert(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert alert is None

    @parametrize
    def test_raw_response_delete_alert(self, client: ClearStreet) -> None:
        response = client.v1.alerts.with_raw_response.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert alert is None

    @parametrize
    def test_streaming_response_delete_alert(self, client: ClearStreet) -> None:
        with client.v1.alerts.with_streaming_response.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_alert(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            client.v1.alerts.with_raw_response.delete_alert(
                "",
            )

    @parametrize
    def test_method_get_alert_by_id(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_get_alert_by_id(self, client: ClearStreet) -> None:
        response = client.v1.alerts.with_raw_response.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_get_alert_by_id(self, client: ClearStreet) -> None:
        with client.v1.alerts.with_streaming_response.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_alert_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            client.v1.alerts.with_raw_response.get_alert_by_id(
                "",
            )

    @parametrize
    def test_method_get_alerts(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.get_alerts()
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    def test_method_get_alerts_with_all_params(self, client: ClearStreet) -> None:
        alert = client.v1.alerts.get_alerts(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            status="status",
        )
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_get_alerts(self, client: ClearStreet) -> None:
        response = client.v1.alerts.with_raw_response.get_alerts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_get_alerts(self, client: ClearStreet) -> None:
        with client.v1.alerts.with_streaming_response.get_alerts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAlerts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_alert(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        )
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    async def test_method_create_alert_with_all_params(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
            account_id=19816,
        )
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_create_alert(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.alerts.with_raw_response.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_create_alert(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.alerts.with_streaming_response.create_alert(
            condition={
                "conditions": [
                    {
                        "op": "lte",
                        "signal": "market.day_change_pct",
                        "subject": {"instrument_id": "NVDA"},
                        "value": -5,
                    }
                ],
                "match": "all",
            },
            schedule="every_1m",
            trigger="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertCreateAlertResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_alert(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert alert is None

    @parametrize
    async def test_raw_response_delete_alert(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.alerts.with_raw_response.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert alert is None

    @parametrize
    async def test_streaming_response_delete_alert(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.alerts.with_streaming_response.delete_alert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_alert(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            await async_client.v1.alerts.with_raw_response.delete_alert(
                "",
            )

    @parametrize
    async def test_method_get_alert_by_id(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_get_alert_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.alerts.with_raw_response.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_get_alert_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.alerts.with_streaming_response.get_alert_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertGetAlertByIDResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_alert_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            await async_client.v1.alerts.with_raw_response.get_alert_by_id(
                "",
            )

    @parametrize
    async def test_method_get_alerts(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.get_alerts()
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    async def test_method_get_alerts_with_all_params(self, async_client: AsyncClearStreet) -> None:
        alert = await async_client.v1.alerts.get_alerts(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            status="status",
        )
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_get_alerts(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.alerts.with_raw_response.get_alerts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_get_alerts(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.alerts.with_streaming_response.get_alerts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertGetAlertsResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True
