# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.omni_ai import (
    EntitlementListEntitlementsResponse,
    EntitlementDeleteEntitlementResponse,
    EntitlementCreateEntitlementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_entitlements(self, client: ClearStreet) -> None:
        entitlement = client.active.v1.omni_ai.entitlements.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        )
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_entitlements(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.entitlements.with_raw_response.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_entitlements(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.entitlements.with_streaming_response.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_entitlement(self, client: ClearStreet) -> None:
        entitlement = client.active.v1.omni_ai.entitlements.delete_entitlement(
            "entitlement_id",
        )
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_entitlement(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
            "entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_entitlement(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.entitlements.with_streaming_response.delete_entitlement(
            "entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_entitlement(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entitlement_id` but received ''"):
            client.active.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_entitlements(self, client: ClearStreet) -> None:
        entitlement = client.active.v1.omni_ai.entitlements.list_entitlements()
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_entitlements_with_all_params(self, client: ClearStreet) -> None:
        entitlement = client.active.v1.omni_ai.entitlements.list_entitlements(
            trading_account_id=0,
        )
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_entitlements(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.entitlements.with_raw_response.list_entitlements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_entitlements(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.entitlements.with_streaming_response.list_entitlements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.active.v1.omni_ai.entitlements.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        )
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.entitlements.with_raw_response.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.entitlements.with_streaming_response.create_entitlements(
            agreement_id="01JZ0000000000000000000000",
            requested_entitlement_codes=["omni.account_data"],
            trading_account_ids=[100019, 100021],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.active.v1.omni_ai.entitlements.delete_entitlement(
            "entitlement_id",
        )
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
            "entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.entitlements.with_streaming_response.delete_entitlement(
            "entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entitlement_id` but received ''"):
            await async_client.active.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_entitlements(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.active.v1.omni_ai.entitlements.list_entitlements()
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_entitlements_with_all_params(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.active.v1.omni_ai.entitlements.list_entitlements(
            trading_account_id=0,
        )
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_entitlements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.entitlements.with_raw_response.list_entitlements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_entitlements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.entitlements.with_streaming_response.list_entitlements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementListEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True
