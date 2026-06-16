# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    InstrumentIDOrSymbol,
    position_get_positions_params,
    position_close_position_params,
    position_close_positions_params,
    position_get_position_instructions_params,
    position_submit_position_instructions_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.position_get_positions_response import PositionGetPositionsResponse
from ...types.v1.position_close_position_response import PositionClosePositionResponse
from ...types.v1.position_close_positions_response import PositionClosePositionsResponse
from ...types.v1.position_get_position_instructions_response import PositionGetPositionInstructionsResponse
from ...types.v1.position_cancel_position_instruction_response import PositionCancelPositionInstructionResponse
from ...types.v1.position_submit_position_instructions_response import PositionSubmitPositionInstructionsResponse

__all__ = ["PositionsResource", "AsyncPositionsResource"]


class PositionsResource(SyncAPIResource):
    """View positions and manage position instructions."""

    @cached_property
    def with_raw_response(self) -> PositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return PositionsResourceWithStreamingResponse(self)

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
    ) -> PositionCancelPositionInstructionResponse:
        """Cancel an outstanding position instruction by its server-assigned `id`.

        Returns
        the updated instruction with status `CANCEL_REQUESTED`. The terminal `CANCELLED`
        or `CANCEL_FAILED` state arrives asynchronously and is observable via subsequent
        GETs.

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
            cast_to=PositionCancelPositionInstructionResponse,
        )

    def close_position(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        account_id: int,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionResponse:
        """
        Delete a position within an account for an instrument.

        Retrieves orders generated to close the position.

        Args:
          instrument_id: Instrument identifier

          cancel_orders: Whether to cancel existing open orders for the position before submitting
              closing orders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._delete(
            path_template(
                "/v1/accounts/{account_id}/positions/{instrument_id}",
                account_id=account_id,
                instrument_id=instrument_id,
            ),
            body=maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_position_params.PositionClosePositionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionResponse,
        )

    def close_positions(
        self,
        account_id: int,
        *,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionsResponse:
        """
        Delete all positions within an account.

        Closes all positions for the specified trading account.

        Args:
          cancel_orders: Whether to cancel existing open orders for the position before submitting
              closing orders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/v1/accounts/{account_id}/positions", account_id=account_id),
            body=maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_positions_params.PositionClosePositionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionsResponse,
        )

    def get_position_instructions(
        self,
        account_id: int,
        *,
        instrument_id: InstrumentIDOrSymbol | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionInstructionsResponse:
        """
        Returns the current lifecycle state of the account's position instructions.
        Optionally filter by a specific contract.

        Note: instructions that fail pre-acceptance validation on `POST` — duplicates,
        `DO_NOT_EXERCISE` / `CONTRARY_EXERCISE` on a non-expiry day, insufficient
        position, or an unresolvable instrument — are rejected (with `status = REJECTED`
        and a `rejection_reason`) without being persisted, so they surface only in the
        `POST` response and never appear in this list.

        Args:
          instrument_id: Limit results to a single contract. Accepts the instrument id or the OSI symbol.

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
                    position_get_position_instructions_params.PositionGetPositionInstructionsParams,
                ),
            ),
            cast_to=PositionGetPositionInstructionsResponse,
        )

    def get_positions(
        self,
        account_id: int,
        *,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        sort_by: Literal[
            "SYMBOL",
            "INSTRUMENT_TYPE",
            "QUANTITY",
            "MARKET_VALUE",
            "POSITION_TYPE",
            "UNREALIZED_PNL",
            "DAILY_UNREALIZED_PNL",
            "DAILY_REALIZED_PNL",
        ]
        | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionsResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          instrument_ids: Comma-separated instrument identifiers

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          sort_by: Field to sort by

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/positions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "instrument_ids": instrument_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    position_get_positions_params.PositionGetPositionsParams,
                ),
            ),
            cast_to=PositionGetPositionsResponse,
        )

    def submit_position_instructions(
        self,
        account_id: int,
        *,
        instructions: Iterable[position_submit_position_instructions_params.Instruction],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionSubmitPositionInstructionsResponse:
        """
        Submit one or more position instructions (Exercise, Do-Not-Exercise, Contrary
        Exercise Advice) against the account.

        Batch semantics:

        - **All rows accepted** → `200 OK`. Every row is in `data` with `status = SENT`.
        - **Partial success** → `207 Multi-Status`. `data` contains every row; rejected
          rows carry `status = REJECTED` and `rejection_reason`. The top-level `error`
          summarizes the batch failure.
        - **All rows rejected** → `4xx`/`5xx`. The HTTP status reflects the aggregate
          cause: `409` when every row was a duplicate, `400` for validation failures
          like DNE/CEA on a non-expiry day, `503` if the clearing service is
          unavailable. `data` still contains every row carrying `status = REJECTED` and
          `rejection_reason` so callers can attribute failures by `instruction_id`; the
          top-level `error` summarizes the batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            body=maybe_transform(instructions, Iterable[position_submit_position_instructions_params.Instruction]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionSubmitPositionInstructionsResponse,
        )


class AsyncPositionsResource(AsyncAPIResource):
    """View positions and manage position instructions."""

    @cached_property
    def with_raw_response(self) -> AsyncPositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncPositionsResourceWithStreamingResponse(self)

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
    ) -> PositionCancelPositionInstructionResponse:
        """Cancel an outstanding position instruction by its server-assigned `id`.

        Returns
        the updated instruction with status `CANCEL_REQUESTED`. The terminal `CANCELLED`
        or `CANCEL_FAILED` state arrives asynchronously and is observable via subsequent
        GETs.

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
            cast_to=PositionCancelPositionInstructionResponse,
        )

    async def close_position(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        account_id: int,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionResponse:
        """
        Delete a position within an account for an instrument.

        Retrieves orders generated to close the position.

        Args:
          instrument_id: Instrument identifier

          cancel_orders: Whether to cancel existing open orders for the position before submitting
              closing orders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._delete(
            path_template(
                "/v1/accounts/{account_id}/positions/{instrument_id}",
                account_id=account_id,
                instrument_id=instrument_id,
            ),
            body=await async_maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_position_params.PositionClosePositionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionResponse,
        )

    async def close_positions(
        self,
        account_id: int,
        *,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionsResponse:
        """
        Delete all positions within an account.

        Closes all positions for the specified trading account.

        Args:
          cancel_orders: Whether to cancel existing open orders for the position before submitting
              closing orders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/v1/accounts/{account_id}/positions", account_id=account_id),
            body=await async_maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_positions_params.PositionClosePositionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionsResponse,
        )

    async def get_position_instructions(
        self,
        account_id: int,
        *,
        instrument_id: InstrumentIDOrSymbol | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionInstructionsResponse:
        """
        Returns the current lifecycle state of the account's position instructions.
        Optionally filter by a specific contract.

        Note: instructions that fail pre-acceptance validation on `POST` — duplicates,
        `DO_NOT_EXERCISE` / `CONTRARY_EXERCISE` on a non-expiry day, insufficient
        position, or an unresolvable instrument — are rejected (with `status = REJECTED`
        and a `rejection_reason`) without being persisted, so they surface only in the
        `POST` response and never appear in this list.

        Args:
          instrument_id: Limit results to a single contract. Accepts the instrument id or the OSI symbol.

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
                    position_get_position_instructions_params.PositionGetPositionInstructionsParams,
                ),
            ),
            cast_to=PositionGetPositionInstructionsResponse,
        )

    async def get_positions(
        self,
        account_id: int,
        *,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        sort_by: Literal[
            "SYMBOL",
            "INSTRUMENT_TYPE",
            "QUANTITY",
            "MARKET_VALUE",
            "POSITION_TYPE",
            "UNREALIZED_PNL",
            "DAILY_UNREALIZED_PNL",
            "DAILY_REALIZED_PNL",
        ]
        | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionsResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          instrument_ids: Comma-separated instrument identifiers

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          sort_by: Field to sort by

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/positions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "instrument_ids": instrument_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    position_get_positions_params.PositionGetPositionsParams,
                ),
            ),
            cast_to=PositionGetPositionsResponse,
        )

    async def submit_position_instructions(
        self,
        account_id: int,
        *,
        instructions: Iterable[position_submit_position_instructions_params.Instruction],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionSubmitPositionInstructionsResponse:
        """
        Submit one or more position instructions (Exercise, Do-Not-Exercise, Contrary
        Exercise Advice) against the account.

        Batch semantics:

        - **All rows accepted** → `200 OK`. Every row is in `data` with `status = SENT`.
        - **Partial success** → `207 Multi-Status`. `data` contains every row; rejected
          rows carry `status = REJECTED` and `rejection_reason`. The top-level `error`
          summarizes the batch failure.
        - **All rows rejected** → `4xx`/`5xx`. The HTTP status reflects the aggregate
          cause: `409` when every row was a duplicate, `400` for validation failures
          like DNE/CEA on a non-expiry day, `503` if the clearing service is
          unavailable. `data` still contains every row carrying `status = REJECTED` and
          `rejection_reason` so callers can attribute failures by `instruction_id`; the
          top-level `error` summarizes the batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/v1/accounts/{account_id}/positions/instructions", account_id=account_id),
            body=await async_maybe_transform(
                instructions, Iterable[position_submit_position_instructions_params.Instruction]
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionSubmitPositionInstructionsResponse,
        )


class PositionsResourceWithRawResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.cancel_position_instruction = to_raw_response_wrapper(
            positions.cancel_position_instruction,
        )
        self.close_position = to_raw_response_wrapper(
            positions.close_position,
        )
        self.close_positions = to_raw_response_wrapper(
            positions.close_positions,
        )
        self.get_position_instructions = to_raw_response_wrapper(
            positions.get_position_instructions,
        )
        self.get_positions = to_raw_response_wrapper(
            positions.get_positions,
        )
        self.submit_position_instructions = to_raw_response_wrapper(
            positions.submit_position_instructions,
        )


class AsyncPositionsResourceWithRawResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.cancel_position_instruction = async_to_raw_response_wrapper(
            positions.cancel_position_instruction,
        )
        self.close_position = async_to_raw_response_wrapper(
            positions.close_position,
        )
        self.close_positions = async_to_raw_response_wrapper(
            positions.close_positions,
        )
        self.get_position_instructions = async_to_raw_response_wrapper(
            positions.get_position_instructions,
        )
        self.get_positions = async_to_raw_response_wrapper(
            positions.get_positions,
        )
        self.submit_position_instructions = async_to_raw_response_wrapper(
            positions.submit_position_instructions,
        )


class PositionsResourceWithStreamingResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.cancel_position_instruction = to_streamed_response_wrapper(
            positions.cancel_position_instruction,
        )
        self.close_position = to_streamed_response_wrapper(
            positions.close_position,
        )
        self.close_positions = to_streamed_response_wrapper(
            positions.close_positions,
        )
        self.get_position_instructions = to_streamed_response_wrapper(
            positions.get_position_instructions,
        )
        self.get_positions = to_streamed_response_wrapper(
            positions.get_positions,
        )
        self.submit_position_instructions = to_streamed_response_wrapper(
            positions.submit_position_instructions,
        )


class AsyncPositionsResourceWithStreamingResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.cancel_position_instruction = async_to_streamed_response_wrapper(
            positions.cancel_position_instruction,
        )
        self.close_position = async_to_streamed_response_wrapper(
            positions.close_position,
        )
        self.close_positions = async_to_streamed_response_wrapper(
            positions.close_positions,
        )
        self.get_position_instructions = async_to_streamed_response_wrapper(
            positions.get_position_instructions,
        )
        self.get_positions = async_to_streamed_response_wrapper(
            positions.get_positions,
        )
        self.submit_position_instructions = async_to_streamed_response_wrapper(
            positions.submit_position_instructions,
        )
