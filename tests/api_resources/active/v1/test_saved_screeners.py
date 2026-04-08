# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1 import (
    SavedScreenerListScreenersResponse,
    SavedScreenerCreateScreenerResponse,
    SavedScreenerUpdateScreenerResponse,
    SavedScreenerGetScreenerByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSavedScreeners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_screener(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.create_screener()
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_screener_with_all_params(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.create_screener(
            field_filter=["string"],
            filters=[
                {
                    "field_name": "field_name",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            name="name",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_screener(self, client: ClearStreet) -> None:
        response = client.active.v1.saved_screeners.with_raw_response.create_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = response.parse()
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_screener(self, client: ClearStreet) -> None:
        with client.active.v1.saved_screeners.with_streaming_response.create_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = response.parse()
            assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_screener(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert saved_screener is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_screener(self, client: ClearStreet) -> None:
        response = client.active.v1.saved_screeners.with_raw_response.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = response.parse()
        assert saved_screener is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_screener(self, client: ClearStreet) -> None:
        with client.active.v1.saved_screeners.with_streaming_response.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = response.parse()
            assert saved_screener is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_screener(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            client.active.v1.saved_screeners.with_raw_response.delete_screener(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_screener_by_id(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_screener_by_id(self, client: ClearStreet) -> None:
        response = client.active.v1.saved_screeners.with_raw_response.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = response.parse()
        assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_screener_by_id(self, client: ClearStreet) -> None:
        with client.active.v1.saved_screeners.with_streaming_response.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = response.parse()
            assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_screener_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            client.active.v1.saved_screeners.with_raw_response.get_screener_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_screeners(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.list_screeners()
        assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_screeners(self, client: ClearStreet) -> None:
        response = client.active.v1.saved_screeners.with_raw_response.list_screeners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = response.parse()
        assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_screeners(self, client: ClearStreet) -> None:
        with client.active.v1.saved_screeners.with_streaming_response.list_screeners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = response.parse()
            assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_screener(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_screener_with_all_params(self, client: ClearStreet) -> None:
        saved_screener = client.active.v1.saved_screeners.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
            field_filter=["string"],
            filters=[
                {
                    "field_name": "field_name",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            name="name",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_screener(self, client: ClearStreet) -> None:
        response = client.active.v1.saved_screeners.with_raw_response.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = response.parse()
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_screener(self, client: ClearStreet) -> None:
        with client.active.v1.saved_screeners.with_streaming_response.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = response.parse()
            assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_screener(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            client.active.v1.saved_screeners.with_raw_response.update_screener(
                screener_id="",
            )


class TestAsyncSavedScreeners:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_screener(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.create_screener()
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_screener_with_all_params(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.create_screener(
            field_filter=["string"],
            filters=[
                {
                    "field_name": "field_name",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            name="name",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_screener(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.saved_screeners.with_raw_response.create_screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = await response.parse()
        assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_screener(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.saved_screeners.with_streaming_response.create_screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = await response.parse()
            assert_matches_type(SavedScreenerCreateScreenerResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_screener(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert saved_screener is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_screener(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.saved_screeners.with_raw_response.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = await response.parse()
        assert saved_screener is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_screener(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.saved_screeners.with_streaming_response.delete_screener(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = await response.parse()
            assert saved_screener is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_screener(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            await async_client.active.v1.saved_screeners.with_raw_response.delete_screener(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_screener_by_id(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_screener_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.saved_screeners.with_raw_response.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = await response.parse()
        assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_screener_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.saved_screeners.with_streaming_response.get_screener_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = await response.parse()
            assert_matches_type(SavedScreenerGetScreenerByIDResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_screener_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            await async_client.active.v1.saved_screeners.with_raw_response.get_screener_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_screeners(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.list_screeners()
        assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_screeners(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.saved_screeners.with_raw_response.list_screeners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = await response.parse()
        assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_screeners(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.saved_screeners.with_streaming_response.list_screeners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = await response.parse()
            assert_matches_type(SavedScreenerListScreenersResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_screener(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_screener_with_all_params(self, async_client: AsyncClearStreet) -> None:
        saved_screener = await async_client.active.v1.saved_screeners.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
            field_filter=["string"],
            filters=[
                {
                    "field_name": "field_name",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            name="name",
            sort_by="sort_by",
            sort_direction="ASC",
        )
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_screener(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.saved_screeners.with_raw_response.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_screener = await response.parse()
        assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_screener(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.saved_screeners.with_streaming_response.update_screener(
            screener_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_screener = await response.parse()
            assert_matches_type(SavedScreenerUpdateScreenerResponse, saved_screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_screener(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screener_id` but received ''"):
            await async_client.active.v1.saved_screeners.with_raw_response.update_screener(
                screener_id="",
            )
