# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1 import OmniFeedGetFeedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOmniFeed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_feed(self, client: ClearStreet) -> None:
        omni_feed = client.v1.omni_feed.get_feed()
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    def test_method_get_feed_with_all_params(self, client: ClearStreet) -> None:
        omni_feed = client.v1.omni_feed.get_feed(
            account_id=0,
            cursor="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    def test_raw_response_get_feed(self, client: ClearStreet) -> None:
        response = client.v1.omni_feed.with_raw_response.get_feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_feed = response.parse()
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    def test_streaming_response_get_feed(self, client: ClearStreet) -> None:
        with client.v1.omni_feed.with_streaming_response.get_feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_feed = response.parse()
            assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_post_feed_event(self, client: ClearStreet) -> None:
        omni_feed = client.v1.omni_feed.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        )
        assert omni_feed is None

    @parametrize
    def test_raw_response_post_feed_event(self, client: ClearStreet) -> None:
        response = client.v1.omni_feed.with_raw_response.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_feed = response.parse()
        assert omni_feed is None

    @parametrize
    def test_streaming_response_post_feed_event(self, client: ClearStreet) -> None:
        with client.v1.omni_feed.with_streaming_response.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_feed = response.parse()
            assert omni_feed is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOmniFeed:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_feed(self, async_client: AsyncClearStreet) -> None:
        omni_feed = await async_client.v1.omni_feed.get_feed()
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    async def test_method_get_feed_with_all_params(self, async_client: AsyncClearStreet) -> None:
        omni_feed = await async_client.v1.omni_feed.get_feed(
            account_id=0,
            cursor="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    async def test_raw_response_get_feed(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_feed.with_raw_response.get_feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_feed = await response.parse()
        assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

    @parametrize
    async def test_streaming_response_get_feed(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_feed.with_streaming_response.get_feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_feed = await response.parse()
            assert_matches_type(OmniFeedGetFeedResponse, omni_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_post_feed_event(self, async_client: AsyncClearStreet) -> None:
        omni_feed = await async_client.v1.omni_feed.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        )
        assert omni_feed is None

    @parametrize
    async def test_raw_response_post_feed_event(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_feed.with_raw_response.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_feed = await response.parse()
        assert omni_feed is None

    @parametrize
    async def test_streaming_response_post_feed_event(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_feed.with_streaming_response.post_feed_event(
            event={
                "item_id": "0198f3a2-4b3d-7c1e-9f2a-3b4c5d6e7f80",
                "type": "seen",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_feed = await response.parse()
            assert omni_feed is None

        assert cast(Any, response.is_closed) is True
