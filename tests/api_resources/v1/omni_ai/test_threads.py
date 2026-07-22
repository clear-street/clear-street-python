# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.omni_ai import (
    ThreadGetThreadsResponse,
    ThreadGetMessagesResponse,
    ThreadCreateThreadResponse,
    ThreadCreateMessageResponse,
    ThreadGetThreadByIDResponse,
    ThreadGetThreadResponseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_message(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    def test_method_create_message_with_all_params(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
            capabilities=["PREFILL_ORDER"],
        )
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_create_message(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_create_message(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_message(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.v1.omni_ai.threads.with_raw_response.create_message(
                thread_id="",
                account_id=19816,
                text="Compare that to AMD.",
            )

    @parametrize
    def test_method_create_thread(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @parametrize
    def test_method_create_thread_with_all_params(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.create_thread(
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

    @parametrize
    def test_raw_response_create_thread(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.create_thread(
            account_id=19816,
            type="instant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_create_thread(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.create_thread(
            account_id=19816,
            type="instant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_messages(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    def test_method_get_messages_with_all_params(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_get_messages(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_get_messages(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_messages(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.v1.omni_ai.threads.with_raw_response.get_messages(
                thread_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_thread_by_id(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_get_thread_by_id(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_get_thread_by_id(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_thread_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.v1.omni_ai.threads.with_raw_response.get_thread_by_id(
                thread_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_thread_response(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_get_thread_response(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_get_thread_response(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_thread_response(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.v1.omni_ai.threads.with_raw_response.get_thread_response(
                thread_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_threads(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_threads(
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    def test_method_get_threads_with_all_params(self, client: ClearStreet) -> None:
        thread = client.v1.omni_ai.threads.get_threads(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_get_threads(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.threads.with_raw_response.get_threads(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_get_threads(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.threads.with_streaming_response.get_threads(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_message(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    async def test_method_create_message_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
            capabilities=["PREFILL_ORDER"],
        )
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_create_message(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create_message(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadCreateMessageResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_message(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.v1.omni_ai.threads.with_raw_response.create_message(
                thread_id="",
                account_id=19816,
                text="Compare that to AMD.",
            )

    @parametrize
    async def test_method_create_thread(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.create_thread(
            account_id=19816,
            type="instant",
        )
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @parametrize
    async def test_method_create_thread_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.create_thread(
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

    @parametrize
    async def test_raw_response_create_thread(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.create_thread(
            account_id=19816,
            type="instant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create_thread(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.create_thread(
            account_id=19816,
            type="instant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadCreateThreadResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_messages(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    async def test_method_get_messages_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_get_messages(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_get_messages(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.get_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadGetMessagesResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_messages(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.v1.omni_ai.threads.with_raw_response.get_messages(
                thread_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_thread_by_id(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_get_thread_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_get_thread_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.get_thread_by_id(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadGetThreadByIDResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_thread_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.v1.omni_ai.threads.with_raw_response.get_thread_by_id(
                thread_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_thread_response(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_get_thread_response(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_get_thread_response(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.get_thread_response(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadGetThreadResponseResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_thread_response(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.v1.omni_ai.threads.with_raw_response.get_thread_response(
                thread_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_threads(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_threads(
            account_id=0,
        )
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    async def test_method_get_threads_with_all_params(self, async_client: AsyncClearStreet) -> None:
        thread = await async_client.v1.omni_ai.threads.get_threads(
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_get_threads(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.threads.with_raw_response.get_threads(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_get_threads(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.threads.with_streaming_response.get_threads(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadGetThreadsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True
