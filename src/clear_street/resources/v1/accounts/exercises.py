# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.accounts import exercise_get_exercises_params, exercise_submit_exercises_params
from ....types.v1.accounts.exercise_get_exercises_response import ExerciseGetExercisesResponse
from ....types.v1.accounts.exercise_cancel_exercise_response import ExerciseCancelExerciseResponse
from ....types.v1.accounts.exercise_submit_exercises_response import ExerciseSubmitExercisesResponse

__all__ = ["ExercisesResource", "AsyncExercisesResource"]


class ExercisesResource(SyncAPIResource):
    """Submit and monitor option exercise, DNE, CEA, and cancel instructions."""

    @cached_property
    def with_raw_response(self) -> ExercisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ExercisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExercisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ExercisesResourceWithStreamingResponse(self)

    def cancel_exercise(
        self,
        exercise_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseCancelExerciseResponse:
        """
        Cancel an outstanding exercise / DNE / CEA instruction by its server- assigned
        `id`. Returns the updated instruction with status `CANCEL_REQUESTED`; the
        terminal `CANCELLED` / `CANCEL_FAILED` state arrives asynchronously via
        subsequent GETs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not exercise_id:
            raise ValueError(f"Expected a non-empty value for `exercise_id` but received {exercise_id!r}")
        return self._delete(
            path_template(
                "/v1/accounts/{account_id}/exercises/{exercise_id}", account_id=account_id, exercise_id=exercise_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExerciseCancelExerciseResponse,
        )

    def get_exercises(
        self,
        account_id: int,
        *,
        instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseGetExercisesResponse:
        """
        Returns the current lifecycle state of exercise / DNE / CEA instructions for the
        account. Optionally filter by a specific instrument.

        Args:
          instrument_id: Filter by OEMS instrument id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/exercises", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_id": instrument_id}, exercise_get_exercises_params.ExerciseGetExercisesParams
                ),
            ),
            cast_to=ExerciseGetExercisesResponse,
        )

    def submit_exercises(
        self,
        account_id: int,
        *,
        exercises: Iterable[exercise_submit_exercises_params.Exercise],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseSubmitExercisesResponse:
        """Submit one or more option lifecycle instructions against the account.

        Each row
        is routed to `oems-csc` independently; per-row rejections are surfaced on the
        corresponding response entry without failing the batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/v1/accounts/{account_id}/exercises", account_id=account_id),
            body=maybe_transform(exercises, Iterable[exercise_submit_exercises_params.Exercise]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExerciseSubmitExercisesResponse,
        )


class AsyncExercisesResource(AsyncAPIResource):
    """Submit and monitor option exercise, DNE, CEA, and cancel instructions."""

    @cached_property
    def with_raw_response(self) -> AsyncExercisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExercisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExercisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncExercisesResourceWithStreamingResponse(self)

    async def cancel_exercise(
        self,
        exercise_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseCancelExerciseResponse:
        """
        Cancel an outstanding exercise / DNE / CEA instruction by its server- assigned
        `id`. Returns the updated instruction with status `CANCEL_REQUESTED`; the
        terminal `CANCELLED` / `CANCEL_FAILED` state arrives asynchronously via
        subsequent GETs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not exercise_id:
            raise ValueError(f"Expected a non-empty value for `exercise_id` but received {exercise_id!r}")
        return await self._delete(
            path_template(
                "/v1/accounts/{account_id}/exercises/{exercise_id}", account_id=account_id, exercise_id=exercise_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExerciseCancelExerciseResponse,
        )

    async def get_exercises(
        self,
        account_id: int,
        *,
        instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseGetExercisesResponse:
        """
        Returns the current lifecycle state of exercise / DNE / CEA instructions for the
        account. Optionally filter by a specific instrument.

        Args:
          instrument_id: Filter by OEMS instrument id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/exercises", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_id": instrument_id}, exercise_get_exercises_params.ExerciseGetExercisesParams
                ),
            ),
            cast_to=ExerciseGetExercisesResponse,
        )

    async def submit_exercises(
        self,
        account_id: int,
        *,
        exercises: Iterable[exercise_submit_exercises_params.Exercise],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExerciseSubmitExercisesResponse:
        """Submit one or more option lifecycle instructions against the account.

        Each row
        is routed to `oems-csc` independently; per-row rejections are surfaced on the
        corresponding response entry without failing the batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/v1/accounts/{account_id}/exercises", account_id=account_id),
            body=await async_maybe_transform(exercises, Iterable[exercise_submit_exercises_params.Exercise]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExerciseSubmitExercisesResponse,
        )


class ExercisesResourceWithRawResponse:
    def __init__(self, exercises: ExercisesResource) -> None:
        self._exercises = exercises

        self.cancel_exercise = to_raw_response_wrapper(
            exercises.cancel_exercise,
        )
        self.get_exercises = to_raw_response_wrapper(
            exercises.get_exercises,
        )
        self.submit_exercises = to_raw_response_wrapper(
            exercises.submit_exercises,
        )


class AsyncExercisesResourceWithRawResponse:
    def __init__(self, exercises: AsyncExercisesResource) -> None:
        self._exercises = exercises

        self.cancel_exercise = async_to_raw_response_wrapper(
            exercises.cancel_exercise,
        )
        self.get_exercises = async_to_raw_response_wrapper(
            exercises.get_exercises,
        )
        self.submit_exercises = async_to_raw_response_wrapper(
            exercises.submit_exercises,
        )


class ExercisesResourceWithStreamingResponse:
    def __init__(self, exercises: ExercisesResource) -> None:
        self._exercises = exercises

        self.cancel_exercise = to_streamed_response_wrapper(
            exercises.cancel_exercise,
        )
        self.get_exercises = to_streamed_response_wrapper(
            exercises.get_exercises,
        )
        self.submit_exercises = to_streamed_response_wrapper(
            exercises.submit_exercises,
        )


class AsyncExercisesResourceWithStreamingResponse:
    def __init__(self, exercises: AsyncExercisesResource) -> None:
        self._exercises = exercises

        self.cancel_exercise = async_to_streamed_response_wrapper(
            exercises.cancel_exercise,
        )
        self.get_exercises = async_to_streamed_response_wrapper(
            exercises.get_exercises,
        )
        self.submit_exercises = async_to_streamed_response_wrapper(
            exercises.submit_exercises,
        )
