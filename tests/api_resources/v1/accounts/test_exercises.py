# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.accounts import (
    ExerciseGetExercisesResponse,
    ExerciseCancelExerciseResponse,
    ExerciseSubmitExercisesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExercises:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_exercise(self, client: ClearStreet) -> None:
        exercise = client.v1.accounts.exercises.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_exercise(self, client: ClearStreet) -> None:
        response = client.v1.accounts.exercises.with_raw_response.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = response.parse()
        assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_exercise(self, client: ClearStreet) -> None:
        with client.v1.accounts.exercises.with_streaming_response.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = response.parse()
            assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_exercise(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exercise_id` but received ''"):
            client.v1.accounts.exercises.with_raw_response.cancel_exercise(
                exercise_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_exercises(self, client: ClearStreet) -> None:
        exercise = client.v1.accounts.exercises.get_exercises(
            account_id=0,
        )
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_exercises_with_all_params(self, client: ClearStreet) -> None:
        exercise = client.v1.accounts.exercises.get_exercises(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_exercises(self, client: ClearStreet) -> None:
        response = client.v1.accounts.exercises.with_raw_response.get_exercises(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = response.parse()
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_exercises(self, client: ClearStreet) -> None:
        with client.v1.accounts.exercises.with_streaming_response.get_exercises(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = response.parse()
            assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_exercises(self, client: ClearStreet) -> None:
        exercise = client.v1.accounts.exercises.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_exercises(self, client: ClearStreet) -> None:
        response = client.v1.accounts.exercises.with_raw_response.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = response.parse()
        assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_exercises(self, client: ClearStreet) -> None:
        with client.v1.accounts.exercises.with_streaming_response.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = response.parse()
            assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExercises:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_exercise(self, async_client: AsyncClearStreet) -> None:
        exercise = await async_client.v1.accounts.exercises.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_exercise(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.exercises.with_raw_response.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = await response.parse()
        assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_exercise(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.exercises.with_streaming_response.cancel_exercise(
            exercise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = await response.parse()
            assert_matches_type(ExerciseCancelExerciseResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_exercise(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exercise_id` but received ''"):
            await async_client.v1.accounts.exercises.with_raw_response.cancel_exercise(
                exercise_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_exercises(self, async_client: AsyncClearStreet) -> None:
        exercise = await async_client.v1.accounts.exercises.get_exercises(
            account_id=0,
        )
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_exercises_with_all_params(self, async_client: AsyncClearStreet) -> None:
        exercise = await async_client.v1.accounts.exercises.get_exercises(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_exercises(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.exercises.with_raw_response.get_exercises(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = await response.parse()
        assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_exercises(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.exercises.with_streaming_response.get_exercises(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = await response.parse()
            assert_matches_type(ExerciseGetExercisesResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_exercises(self, async_client: AsyncClearStreet) -> None:
        exercise = await async_client.v1.accounts.exercises.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_exercises(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.exercises.with_raw_response.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exercise = await response.parse()
        assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_exercises(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.exercises.with_streaming_response.submit_exercises(
            account_id=0,
            exercises=[
                {
                    "action": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exercise = await response.parse()
            assert_matches_type(ExerciseSubmitExercisesResponse, exercise, path=["response"])

        assert cast(Any, response.is_closed) is True
