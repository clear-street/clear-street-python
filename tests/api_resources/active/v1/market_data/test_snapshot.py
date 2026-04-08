# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.market_data import SnapshotGetSnapshotsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_snapshots(self, client: ClearStreet) -> None:
        snapshot = client.active.v1.market_data.snapshot.get_snapshots()
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_snapshots_with_all_params(self, client: ClearStreet) -> None:
        snapshot = client.active.v1.market_data.snapshot.get_snapshots(
            ids="ids",
            security_id=["string"],
            security_id_source=["string"],
        )
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_snapshots(self, client: ClearStreet) -> None:
        response = client.active.v1.market_data.snapshot.with_raw_response.get_snapshots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_snapshots(self, client: ClearStreet) -> None:
        with client.active.v1.market_data.snapshot.with_streaming_response.get_snapshots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSnapshot:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        snapshot = await async_client.active.v1.market_data.snapshot.get_snapshots()
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_snapshots_with_all_params(self, async_client: AsyncClearStreet) -> None:
        snapshot = await async_client.active.v1.market_data.snapshot.get_snapshots(
            ids="ids",
            security_id=["string"],
            security_id_source=["string"],
        )
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.market_data.snapshot.with_raw_response.get_snapshots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_snapshots(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.market_data.snapshot.with_streaming_response.get_snapshots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotGetSnapshotsResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True
