# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1 import (
    WatchlistGetWatchlistsResponse,
    WatchlistCreateWatchlistResponse,
    WatchlistGetWatchlistByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatchlists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_watchlist(self, client: ClearStreet) -> None:
        watchlist = client.active.v1.watchlists.create_watchlist(
            name="name",
        )
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_watchlist(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.with_raw_response.create_watchlist(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_watchlist(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.with_streaming_response.create_watchlist(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_watchlist(self, client: ClearStreet) -> None:
        watchlist = client.active.v1.watchlists.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(object, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_watchlist(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.with_raw_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(object, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_watchlist(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.with_streaming_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(object, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_watchlist(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.active.v1.watchlists.with_raw_response.delete_watchlist(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_watchlist_by_id(self, client: ClearStreet) -> None:
        watchlist = client.active.v1.watchlists.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_watchlist_by_id(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.with_raw_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_watchlist_by_id(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.with_streaming_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_watchlist_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            client.active.v1.watchlists.with_raw_response.get_watchlist_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_watchlists(self, client: ClearStreet) -> None:
        watchlist = client.active.v1.watchlists.get_watchlists()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_watchlists_with_all_params(self, client: ClearStreet) -> None:
        watchlist = client.active.v1.watchlists.get_watchlists(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_watchlists(self, client: ClearStreet) -> None:
        response = client.active.v1.watchlists.with_raw_response.get_watchlists()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_watchlists(self, client: ClearStreet) -> None:
        with client.active.v1.watchlists.with_streaming_response.get_watchlists() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatchlists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.active.v1.watchlists.create_watchlist(
            name="name",
        )
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.with_raw_response.create_watchlist(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_watchlist(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.with_streaming_response.create_watchlist(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistCreateWatchlistResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.active.v1.watchlists.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(object, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.with_raw_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(object, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.with_streaming_response.delete_watchlist(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(object, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_watchlist(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.active.v1.watchlists.with_raw_response.delete_watchlist(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.active.v1.watchlists.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.with_raw_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.with_streaming_response.get_watchlist_by_id(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistGetWatchlistByIDResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_watchlist_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watchlist_id` but received ''"):
            await async_client.active.v1.watchlists.with_raw_response.get_watchlist_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.active.v1.watchlists.get_watchlists()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_watchlists_with_all_params(self, async_client: AsyncClearStreet) -> None:
        watchlist = await async_client.active.v1.watchlists.get_watchlists(
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.watchlists.with_raw_response.get_watchlists()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_watchlists(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.watchlists.with_streaming_response.get_watchlists() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistGetWatchlistsResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True
