# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.accounts.positions import (
    instruction_get_position_instructions_params,
    instruction_submit_position_instructions_params,
)
from .....types.v1.accounts.positions.instruction_get_position_instructions_response import (
    InstructionGetPositionInstructionsResponse,
)
from .....types.v1.accounts.positions.instruction_cancel_position_instruction_response import (
    InstructionCancelPositionInstructionResponse,
)
from .....types.v1.accounts.positions.instruction_submit_position_instructions_response import (
    InstructionSubmitPositionInstructionsResponse,
)

__all__ = ["InstructionsResource", "AsyncInstructionsResource"]


class InstructionsResource(SyncAPIResource):
    """Submit and monitor option exercise, DNE, CEA, and cancel instructions."""

    @cached_property
    def with_raw_response(self) -> InstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return InstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return InstructionsResourceWithStreamingResponse(self)

    def cancel_position_instruction(
        self,
        instruction_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstructionCancelPositionInstructionResponse:
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
        if not instruction_id:
            raise ValueError(f"Expected a non-empty value for `instruction_id` but received {instruction_id!r}")
        return self._delete(
            path_template(
                "/v1/accounts/{account_id}/positions/instructions/{instruction_id}",
                account_id=account_id,
                instruction_id=instruction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionCancelPositionInstructionResponse,
        )

    def get_position_instructions(
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
    ) -> InstructionGetPositionInstructionsResponse:
        """
        Returns the current lifecycle state of exercise / DNE / CEA instructions for the
        account. Optionally filter by a specific instrument.

        Args:
          instrument_id: Filter by OEMS instrument id or symbol (CMS / OSI).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_id": instrument_id},
                    instruction_get_position_instructions_params.InstructionGetPositionInstructionsParams,
                ),
            ),
            cast_to=InstructionGetPositionInstructionsResponse,
        )

    def submit_position_instructions(
        self,
        account_id: int,
        *,
        instructions: Iterable[instruction_submit_position_instructions_params.Instruction],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstructionSubmitPositionInstructionsResponse:
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
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            body=maybe_transform(instructions, Iterable[instruction_submit_position_instructions_params.Instruction]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionSubmitPositionInstructionsResponse,
        )


class AsyncInstructionsResource(AsyncAPIResource):
    """Submit and monitor option exercise, DNE, CEA, and cancel instructions."""

    @cached_property
    def with_raw_response(self) -> AsyncInstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncInstructionsResourceWithStreamingResponse(self)

    async def cancel_position_instruction(
        self,
        instruction_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstructionCancelPositionInstructionResponse:
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
        if not instruction_id:
            raise ValueError(f"Expected a non-empty value for `instruction_id` but received {instruction_id!r}")
        return await self._delete(
            path_template(
                "/v1/accounts/{account_id}/positions/instructions/{instruction_id}",
                account_id=account_id,
                instruction_id=instruction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionCancelPositionInstructionResponse,
        )

    async def get_position_instructions(
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
    ) -> InstructionGetPositionInstructionsResponse:
        """
        Returns the current lifecycle state of exercise / DNE / CEA instructions for the
        account. Optionally filter by a specific instrument.

        Args:
          instrument_id: Filter by OEMS instrument id or symbol (CMS / OSI).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_id": instrument_id},
                    instruction_get_position_instructions_params.InstructionGetPositionInstructionsParams,
                ),
            ),
            cast_to=InstructionGetPositionInstructionsResponse,
        )

    async def submit_position_instructions(
        self,
        account_id: int,
        *,
        instructions: Iterable[instruction_submit_position_instructions_params.Instruction],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstructionSubmitPositionInstructionsResponse:
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
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            body=await async_maybe_transform(
                instructions, Iterable[instruction_submit_position_instructions_params.Instruction]
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionSubmitPositionInstructionsResponse,
        )


class InstructionsResourceWithRawResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.cancel_position_instruction = to_raw_response_wrapper(
            instructions.cancel_position_instruction,
        )
        self.get_position_instructions = to_raw_response_wrapper(
            instructions.get_position_instructions,
        )
        self.submit_position_instructions = to_raw_response_wrapper(
            instructions.submit_position_instructions,
        )


class AsyncInstructionsResourceWithRawResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.cancel_position_instruction = async_to_raw_response_wrapper(
            instructions.cancel_position_instruction,
        )
        self.get_position_instructions = async_to_raw_response_wrapper(
            instructions.get_position_instructions,
        )
        self.submit_position_instructions = async_to_raw_response_wrapper(
            instructions.submit_position_instructions,
        )


class InstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.cancel_position_instruction = to_streamed_response_wrapper(
            instructions.cancel_position_instruction,
        )
        self.get_position_instructions = to_streamed_response_wrapper(
            instructions.get_position_instructions,
        )
        self.submit_position_instructions = to_streamed_response_wrapper(
            instructions.submit_position_instructions,
        )


class AsyncInstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.cancel_position_instruction = async_to_streamed_response_wrapper(
            instructions.cancel_position_instruction,
        )
        self.get_position_instructions = async_to_streamed_response_wrapper(
            instructions.get_position_instructions,
        )
        self.submit_position_instructions = async_to_streamed_response_wrapper(
            instructions.submit_position_instructions,
        )
