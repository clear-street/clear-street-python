# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.omni_ai import (
    EntitlementGetEntitlementsResponse,
    EntitlementDeleteEntitlementResponse,
    EntitlementCreateEntitlementsResponse,
    EntitlementGetEntitlementAgreementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_entitlements(self, client: ClearStreet) -> None:
        entitlement = client.v1.omni_ai.entitlements.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        )
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_entitlements(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.entitlements.with_raw_response.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_entitlements(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.entitlements.with_streaming_response.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_entitlement(self, client: ClearStreet) -> None:
        entitlement = client.v1.omni_ai.entitlements.delete_entitlement(
            "entitlement_id",
        )
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_entitlement(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
            "entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_entitlement(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.entitlements.with_streaming_response.delete_entitlement(
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
            client.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_entitlement_agreements(self, client: ClearStreet) -> None:
        entitlement = client.v1.omni_ai.entitlements.get_entitlement_agreements()
        assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_entitlement_agreements(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.entitlements.with_raw_response.get_entitlement_agreements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_entitlement_agreements(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.entitlements.with_streaming_response.get_entitlement_agreements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_entitlements(self, client: ClearStreet) -> None:
        entitlement = client.v1.omni_ai.entitlements.get_entitlements()
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_entitlements_with_all_params(self, client: ClearStreet) -> None:
        entitlement = client.v1.omni_ai.entitlements.get_entitlements(
            trading_account_id=0,
        )
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_entitlements(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.entitlements.with_raw_response.get_entitlements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = response.parse()
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_entitlements(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.entitlements.with_streaming_response.get_entitlements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = response.parse()
            assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.v1.omni_ai.entitlements.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        )
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.entitlements.with_raw_response.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_entitlements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.entitlements.with_streaming_response.create_entitlements(
            account_ids=[100019, 100021],
            agreement_id="01JZ0000000000000000000000",
            entitlement_codes=["omni.account_data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementCreateEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.v1.omni_ai.entitlements.delete_entitlement(
            "entitlement_id",
        )
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
            "entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementDeleteEntitlementResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_entitlement(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.entitlements.with_streaming_response.delete_entitlement(
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
            await async_client.v1.omni_ai.entitlements.with_raw_response.delete_entitlement(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.v1.omni_ai.entitlements.get_entitlement_agreements()
        assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.entitlements.with_raw_response.get_entitlement_agreements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        async with (
            async_client.v1.omni_ai.entitlements.with_streaming_response.get_entitlement_agreements()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementGetEntitlementAgreementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_entitlements(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.v1.omni_ai.entitlements.get_entitlements()
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_entitlements_with_all_params(self, async_client: AsyncClearStreet) -> None:
        entitlement = await async_client.v1.omni_ai.entitlements.get_entitlements(
            trading_account_id=0,
        )
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_entitlements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.entitlements.with_raw_response.get_entitlements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement = await response.parse()
        assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_entitlements(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.entitlements.with_streaming_response.get_entitlements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement = await response.parse()
            assert_matches_type(EntitlementGetEntitlementsResponse, entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True
