# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.assistant import (
    PromptRunPromptResponse,
    PromptGetPromptResultResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_prompt_result(self, client: ClearStreet) -> None:
        prompt = client.active.v1.assistant.prompts.get_prompt_result(
            id="id",
        )
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_prompt_result_with_all_params(self, client: ClearStreet) -> None:
        prompt = client.active.v1.assistant.prompts.get_prompt_result(
            id="id",
            return_all_outputs=True,
        )
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_prompt_result(self, client: ClearStreet) -> None:
        response = client.active.v1.assistant.prompts.with_raw_response.get_prompt_result(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_prompt_result(self, client: ClearStreet) -> None:
        with client.active.v1.assistant.prompts.with_streaming_response.get_prompt_result(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_prompt_result(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.active.v1.assistant.prompts.with_raw_response.get_prompt_result(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_prompt(self, client: ClearStreet) -> None:
        prompt = client.active.v1.assistant.prompts.run_prompt(
            body={},
            slug="slug",
        )
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_prompt_with_all_params(self, client: ClearStreet) -> None:
        prompt = client.active.v1.assistant.prompts.run_prompt(
            body={},
            slug="slug",
            metadata={"foo": "string"},
        )
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_prompt(self, client: ClearStreet) -> None:
        response = client.active.v1.assistant.prompts.with_raw_response.run_prompt(
            body={},
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_prompt(self, client: ClearStreet) -> None:
        with client.active.v1.assistant.prompts.with_streaming_response.run_prompt(
            body={},
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_prompt_result(self, async_client: AsyncClearStreet) -> None:
        prompt = await async_client.active.v1.assistant.prompts.get_prompt_result(
            id="id",
        )
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_prompt_result_with_all_params(self, async_client: AsyncClearStreet) -> None:
        prompt = await async_client.active.v1.assistant.prompts.get_prompt_result(
            id="id",
            return_all_outputs=True,
        )
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_prompt_result(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.assistant.prompts.with_raw_response.get_prompt_result(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_prompt_result(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.assistant.prompts.with_streaming_response.get_prompt_result(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetPromptResultResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_prompt_result(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.active.v1.assistant.prompts.with_raw_response.get_prompt_result(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_prompt(self, async_client: AsyncClearStreet) -> None:
        prompt = await async_client.active.v1.assistant.prompts.run_prompt(
            body={},
            slug="slug",
        )
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_prompt_with_all_params(self, async_client: AsyncClearStreet) -> None:
        prompt = await async_client.active.v1.assistant.prompts.run_prompt(
            body={},
            slug="slug",
            metadata={"foo": "string"},
        )
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_prompt(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.assistant.prompts.with_raw_response.run_prompt(
            body={},
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_prompt(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.assistant.prompts.with_streaming_response.run_prompt(
            body={},
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptRunPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
