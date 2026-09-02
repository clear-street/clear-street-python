# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.private_markets import (
    OfferingGetOfferingsResponse,
    OfferingGetOfferingByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOfferings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_offering_by_id(self, client: ClearStreet) -> None:
        offering = client.v1.private_markets.offerings.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

    @parametrize
    def test_raw_response_get_offering_by_id(self, client: ClearStreet) -> None:
        response = client.v1.private_markets.offerings.with_raw_response.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offering = response.parse()
        assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

    @parametrize
    def test_streaming_response_get_offering_by_id(self, client: ClearStreet) -> None:
        with client.v1.private_markets.offerings.with_streaming_response.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offering = response.parse()
            assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_offering_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offering_id` but received ''"):
            client.v1.private_markets.offerings.with_raw_response.get_offering_by_id(
                offering_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_offerings(self, client: ClearStreet) -> None:
        offering = client.v1.private_markets.offerings.get_offerings(
            account_id=0,
        )
        assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

    @parametrize
    def test_raw_response_get_offerings(self, client: ClearStreet) -> None:
        response = client.v1.private_markets.offerings.with_raw_response.get_offerings(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offering = response.parse()
        assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

    @parametrize
    def test_streaming_response_get_offerings(self, client: ClearStreet) -> None:
        with client.v1.private_markets.offerings.with_streaming_response.get_offerings(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offering = response.parse()
            assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOfferings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_offering_by_id(self, async_client: AsyncClearStreet) -> None:
        offering = await async_client.v1.private_markets.offerings.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

    @parametrize
    async def test_raw_response_get_offering_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.private_markets.offerings.with_raw_response.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offering = await response.parse()
        assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

    @parametrize
    async def test_streaming_response_get_offering_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.private_markets.offerings.with_streaming_response.get_offering_by_id(
            offering_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offering = await response.parse()
            assert_matches_type(OfferingGetOfferingByIDResponse, offering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_offering_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offering_id` but received ''"):
            await async_client.v1.private_markets.offerings.with_raw_response.get_offering_by_id(
                offering_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_offerings(self, async_client: AsyncClearStreet) -> None:
        offering = await async_client.v1.private_markets.offerings.get_offerings(
            account_id=0,
        )
        assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

    @parametrize
    async def test_raw_response_get_offerings(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.private_markets.offerings.with_raw_response.get_offerings(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offering = await response.parse()
        assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

    @parametrize
    async def test_streaming_response_get_offerings(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.private_markets.offerings.with_streaming_response.get_offerings(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offering = await response.parse()
            assert_matches_type(OfferingGetOfferingsResponse, offering, path=["response"])

        assert cast(Any, response.is_closed) is True
