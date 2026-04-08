# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.iris import (
    ThreadGetThreadDeprecatedResponse,
    ThreadListThreadsDeprecatedResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_thread_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = client.active.v1.iris.threads.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_thread_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.active.v1.iris.threads.with_raw_response.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_thread_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            with client.active.v1.iris.threads.with_streaming_response.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                thread = response.parse()
                assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_thread_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
                client.active.v1.iris.threads.with_raw_response.get_thread_deprecated(
                    thread_id="",
                    account_id="account_id",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_threads_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = client.active.v1.iris.threads.list_threads_deprecated(
                account_id="account_id",
            )

        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_threads_deprecated_with_all_params(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = client.active.v1.iris.threads.list_threads_deprecated(
                account_id="account_id",
                page_size=0,
                page_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_threads_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.active.v1.iris.threads.with_raw_response.list_threads_deprecated(
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_threads_deprecated(self, client: ClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            with client.active.v1.iris.threads.with_streaming_response.list_threads_deprecated(
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                thread = response.parse()
                assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_thread_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = await async_client.active.v1.iris.threads.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_thread_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.active.v1.iris.threads.with_raw_response.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.active.v1.iris.threads.with_streaming_response.get_thread_deprecated(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                thread = await response.parse()
                assert_matches_type(ThreadGetThreadDeprecatedResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_thread_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
                await async_client.active.v1.iris.threads.with_raw_response.get_thread_deprecated(
                    thread_id="",
                    account_id="account_id",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_threads_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = await async_client.active.v1.iris.threads.list_threads_deprecated(
                account_id="account_id",
            )

        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_threads_deprecated_with_all_params(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            thread = await async_client.active.v1.iris.threads.list_threads_deprecated(
                account_id="account_id",
                page_size=0,
                page_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_threads_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.active.v1.iris.threads.with_raw_response.list_threads_deprecated(
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_threads_deprecated(self, async_client: AsyncClearStreet) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.active.v1.iris.threads.with_streaming_response.list_threads_deprecated(
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                thread = await response.parse()
                assert_matches_type(ThreadListThreadsDeprecatedResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True
