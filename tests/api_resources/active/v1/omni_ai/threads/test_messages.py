# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.omni_ai.threads import (
    MessageListMessagesResponse,
    MessageCreateMessageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_message(self, client: ClearStreet) -> None:
        message = client.active.v1.omni_ai.threads.messages.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_message_with_all_params(self, client: ClearStreet) -> None:
        message = client.active.v1.omni_ai.threads.messages.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
            capabilities=["PREFILL_ORDER"],
        )
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_message(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.messages.with_raw_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_message(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.messages.with_streaming_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_message(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.active.v1.omni_ai.threads.messages.with_raw_response.create_message(
                thread_id="",
                account_id=19816,
                text="Compare that to AMD.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages(self, client: ClearStreet) -> None:
        message = client.active.v1.omni_ai.threads.messages.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages_with_all_params(self, client: ClearStreet) -> None:
        message = client.active.v1.omni_ai.threads.messages.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_messages(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.threads.messages.with_raw_response.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_messages(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.threads.messages.with_streaming_response.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListMessagesResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_messages(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.active.v1.omni_ai.threads.messages.with_raw_response.list_messages(
                thread_id="",
                account_id=0,
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_message(self, async_client: AsyncClearStreet) -> None:
        message = await async_client.active.v1.omni_ai.threads.messages.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_message_with_all_params(self, async_client: AsyncClearStreet) -> None:
        message = await async_client.active.v1.omni_ai.threads.messages.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
            capabilities=["PREFILL_ORDER"],
        )
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_message(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.messages.with_raw_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_message(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.messages.with_streaming_response.create_message(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=19816,
            text="Compare that to AMD.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_message(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.active.v1.omni_ai.threads.messages.with_raw_response.create_message(
                thread_id="",
                account_id=19816,
                text="Compare that to AMD.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncClearStreet) -> None:
        message = await async_client.active.v1.omni_ai.threads.messages.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncClearStreet) -> None:
        message = await async_client.active.v1.omni_ai.threads.messages.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.threads.messages.with_raw_response.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListMessagesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.threads.messages.with_streaming_response.list_messages(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListMessagesResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.active.v1.omni_ai.threads.messages.with_raw_response.list_messages(
                thread_id="",
                account_id=0,
            )
