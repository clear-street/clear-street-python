# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1 import (
    WatchlistGetWatchlistsResponse,
    WatchlistCreateWatchlistResponse,
    WatchlistDeleteWatchlistResponse,
    WatchlistAddWatchlistItemResponse,
    WatchlistGetWatchlistByIDResponse,
    WatchlistDeleteWatchlistItemResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatchlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_watchlist_item(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_add_watchlist_item(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_add_watchlist_item(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_watchlist_item(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.v1.watchlist.with_raw_response.add_watchlist_item(
                watchlist_id="",
                instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_create_watchlist(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.create_watchlist(
            name="name",
        )
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_create_watchlist(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.create_watchlist(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_create_watchlist(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.create_watchlist(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_watchlist(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_delete_watchlist(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_delete_watchlist(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_watchlist(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.v1.watchlist.with_raw_response.delete_watchlist(
                "",
            )

    @parametrize
    def test_method_delete_watchlist_item(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_delete_watchlist_item(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_delete_watchlist_item(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_watchlist_item(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.v1.watchlist.with_raw_response.delete_watchlist_item(
                item_id="660e8400-e29b-41d4-a716-446655440001",
                watchlist_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.v1.watchlist.with_raw_response.delete_watchlist_item(
                item_id="",
                watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @parametrize
    def test_method_get_watchlist_by_id(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_get_watchlist_by_id(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_get_watchlist_by_id(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_watchlist_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.v1.watchlist.with_raw_response.get_watchlist_by_id(
                "",
            )

    @parametrize
    def test_method_get_watchlists(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.get_watchlists()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    def test_method_get_watchlists_with_all_params(self, client: ClearStreet) -> None:
        watchlist = client.v1.watchlist.get_watchlists(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_get_watchlists(self, client: ClearStreet) -> None:
        response = client.v1.watchlist.with_raw_response.get_watchlists()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_get_watchlists(self, client: ClearStreet) -> None:
        with client.v1.watchlist.with_streaming_response.get_watchlists() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatchlist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.add_watchlist_item(
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistAddWatchlistItemResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.v1.watchlist.with_raw_response.add_watchlist_item(
                watchlist_id="",
                instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.create_watchlist(
            name="name",
        )
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.create_watchlist(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.create_watchlist(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistDeleteWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.v1.watchlist.with_raw_response.delete_watchlist(
                "",
            )

    @parametrize
    async def test_method_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.delete_watchlist_item(
            item_id="660e8400-e29b-41d4-a716-446655440001",
            watchlist_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistDeleteWatchlistItemResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_watchlist_item(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.v1.watchlist.with_raw_response.delete_watchlist_item(
                item_id="660e8400-e29b-41d4-a716-446655440001",
                watchlist_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.v1.watchlist.with_raw_response.delete_watchlist_item(
                item_id="",
                watchlist_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @parametrize
    async def test_method_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.v1.watchlist.with_raw_response.get_watchlist_by_id(
                "",
            )

    @parametrize
    async def test_method_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.get_watchlists()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    async def test_method_get_watchlists_with_all_params(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.v1.watchlist.get_watchlists(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.watchlist.with_raw_response.get_watchlists()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.watchlist.with_streaming_response.get_watchlists() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True
