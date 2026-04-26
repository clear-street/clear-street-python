# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.omni_ai import (
    ThreadResponseResponse,
    ThreadGetThreadResponse,
    ThreadListThreadsResponse,
    ThreadCreateThreadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_thread(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_thread_with_all_params(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
            capabilities=["PREFILL_ORDER"],
            target={
                "ticker": "ticker",
                "type": "ticker",
            },
            text="What changed in NVDA today?",
            thesis="thesis",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_thread(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.with_raw_response.create_thread(
            account_id=19816,
            type="instant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_thread(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.with_streaming_response.create_thread(
            account_id=19816,
            type="instant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_thread(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_thread(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.with_raw_response.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_thread(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.with_streaming_response.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_thread(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.active.v1.omni_ai.threads.with_raw_response.get_thread(
                thread_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_threads(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.list_threads(
            account_id=0,
        )
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_threads_with_all_params(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.list_threads(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_threads(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.with_raw_response.list_threads(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_threads(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.with_streaming_response.list_threads(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_response(self, client: ClearStreet) -> None:
        thread = client.active.v1.omni_ai.threads.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadResponseResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_response(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.with_raw_response.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadResponseResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_response(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.with_streaming_response.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadResponseResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_response(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.active.v1.omni_ai.threads.with_raw_response.response(
                thread_id="",
                account_id=0,
            )


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_thread(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_thread_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
            capabilities=["PREFILL_ORDER"],
            target={
                "ticker": "ticker",
                "type": "ticker",
            },
            text="What changed in NVDA today?",
            thesis="thesis",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_thread(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.with_raw_response.create_thread(
            account_id=19816,
            type="instant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_thread(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.with_streaming_response.create_thread(
            account_id=19816,
            type="instant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_thread(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_thread(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.with_raw_response.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.with_streaming_response.get_thread(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadGetThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_thread(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.active.v1.omni_ai.threads.with_raw_response.get_thread(
                thread_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_threads(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.list_threads(
            account_id=0,
        )
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_threads_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.list_threads(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_threads(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.with_raw_response.list_threads(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_threads(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.with_streaming_response.list_threads(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadListThreadsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_response(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.active.v1.omni_ai.threads.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadResponseResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_response(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.with_raw_response.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadResponseResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_response(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.with_streaming_response.response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadResponseResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_response(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.active.v1.omni_ai.threads.with_raw_response.response(
                thread_id="",
                account_id=0,
            )
