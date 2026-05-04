# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.omni_ai import EntitlementAgreementListEntitlementAgreementsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlementAgreements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_entitlement_agreements(self, client: ClearStreet) -> None:
        entitlement_agreement = client.v1.omni_ai.entitlement_agreements.list_entitlement_agreements()
        assert_matches_type(
            EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_entitlement_agreements(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.entitlement_agreements.with_raw_response.list_entitlement_agreements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement_agreement = response.parse()
        assert_matches_type(
            EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_entitlement_agreements(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.entitlement_agreements.with_streaming_response.list_entitlement_agreements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement_agreement = response.parse()
            assert_matches_type(
                EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncEntitlementAgreements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        entitlement_agreement = await async_client.v1.omni_ai.entitlement_agreements.list_entitlement_agreements()
        assert_matches_type(
            EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.entitlement_agreements.with_raw_response.list_entitlement_agreements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entitlement_agreement = await response.parse()
        assert_matches_type(
            EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_entitlement_agreements(self, async_client: AsyncClearStreet) -> None:
        async with (
            async_client.v1.omni_ai.entitlement_agreements.with_streaming_response.list_entitlement_agreements()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entitlement_agreement = await response.parse()
            assert_matches_type(
                EntitlementAgreementListEntitlementAgreementsResponse, entitlement_agreement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
