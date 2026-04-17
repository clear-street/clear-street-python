# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.active.v1.omni_ai import FeedbackCreateFeedbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_feedback(self, client: ClearStreet) -> None:
        feedback = client.active.v1.omni_ai.feedback.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_feedback_with_all_params(self, client: ClearStreet) -> None:
        feedback = client.active.v1.omni_ai.feedback.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            metadata={},
        )
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_feedback(self, client: ClearStreet) -> None:
        response = client.active.v1.omni_ai.feedback.with_raw_response.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_feedback(self, client: ClearStreet) -> None:
        with client.active.v1.omni_ai.feedback.with_streaming_response.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_feedback(self, async_client: AsyncClearStreet) -> None:
        feedback = await async_client.active.v1.omni_ai.feedback.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_feedback_with_all_params(self, async_client: AsyncClearStreet) -> None:
        feedback = await async_client.active.v1.omni_ai.feedback.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            metadata={},
        )
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_feedback(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.omni_ai.feedback.with_raw_response.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_feedback(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.omni_ai.feedback.with_streaming_response.create_feedback(
            account_id="account_id",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackCreateFeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
