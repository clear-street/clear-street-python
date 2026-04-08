# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.watchlists import ItemAddWatchlistItemResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_watchlist_item(self, client: ClearStreet) -> None:
        item = client.active.v1.watchlists.items.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_watchlist_item_with_all_params(self, client: ClearStreet) -> None:
        item = client.active.v1.watchlists.items.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_watchlist_item(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.items.with_raw_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_watchlist_item(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.items.with_streaming_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_watchlist_item(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.active.v1.watchlists.items.with_raw_response.add_watchlist_item(
                watchlist_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_watchlist_item(self, client: ClearStreet) -> None:
        item = client.active.v1.watchlists.items.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_watchlist_item(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_watchlist_item(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.items.with_streaming_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_watchlist_item(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
                item_id="660e8400-e29b-41d4-a716-446655440001",
                watchlist_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
                item_id="",
                watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        item = await async_client.active.v1.watchlists.items.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_watchlist_item_with_all_params(self, async_client: AsyncClearStreet) -> None:
        item = await async_client.active.v1.watchlists.items.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            security_id="security_id",
            security_id_source="CMS",
        )
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.items.with_raw_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.items.with_streaming_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemAddWatchlistItemResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.active.v1.watchlists.items.with_raw_response.add_watchlist_item(
                watchlist_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        item = await async_client.active.v1.watchlists.items.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.items.with_streaming_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
                item_id="660e8400-e29b-41d4-a716-446655440001",
                watchlist_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.active.v1.watchlists.items.with_raw_response.delete_watchlist_item(
                item_id="",
                watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            )
