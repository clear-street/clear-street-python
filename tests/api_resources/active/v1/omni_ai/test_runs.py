# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.omni_ai import (
    RunGetRunResponse,
    RunStartRunResponse,
    RunCancelRunResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_run(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_run_with_all_params(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            reason="reason",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_run(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.runs.with_raw_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_run(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.runs.with_streaming_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCancelRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_run(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.active.v1.omni_ai.runs.with_raw_response.cancel_run(
                run_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_run(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_run_with_all_params(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            page_size=0,
            page_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_run(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.runs.with_raw_response.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_run(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.runs.with_streaming_response.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_run(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.active.v1.omni_ai.runs.with_raw_response.get_run(
                run_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_run(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.start_run(
            account_id="account_id",
            command_text="command_text",
        )
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_run_with_all_params(self, client: ClearStreet) -> None:
        run = client.active.v1.omni_ai.runs.start_run(
            account_id="account_id",
            command_text="command_text",
            capabilities=["NAVIGATE"],
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            thread_title="thread_title",
        )
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_run(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.runs.with_raw_response.start_run(
            account_id="account_id",
            command_text="command_text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_run(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.runs.with_streaming_response.start_run(
            account_id="account_id",
            command_text="command_text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunStartRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run_with_all_params(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            reason="reason",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_run(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.runs.with_raw_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_run(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.runs.with_streaming_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCancelRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_run(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.active.v1.omni_ai.runs.with_raw_response.cancel_run(
                run_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_run(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_run_with_all_params(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            page_size=0,
            page_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_run(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.runs.with_raw_response.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_run(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.runs.with_streaming_response.get_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_run(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.active.v1.omni_ai.runs.with_raw_response.get_run(
                run_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_run(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.start_run(
            account_id="account_id",
            command_text="command_text",
        )
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_run_with_all_params(self, async_client: AsyncClearStreet) -> None:
        run = await async_client.active.v1.omni_ai.runs.start_run(
            account_id="account_id",
            command_text="command_text",
            capabilities=["NAVIGATE"],
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            thread_title="thread_title",
        )
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_run(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.runs.with_raw_response.start_run(
            account_id="account_id",
            command_text="command_text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunStartRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_run(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.runs.with_streaming_response.start_run(
            account_id="account_id",
            command_text="command_text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunStartRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True
