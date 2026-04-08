# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from .....types.active.v1.omni_ai import run_get_run_params, run_start_run_params, run_cancel_run_params
from .....types.active.v1.capability import Capability
from .....types.active.v1.omni_ai.run_get_run_response import RunGetRunResponse
from .....types.active.v1.omni_ai.run_start_run_response import RunStartRunResponse
from .....types.active.v1.omni_ai.run_cancel_run_response import RunCancelRunResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """AI assistant for conversational trading interactions."""

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def cancel_run(
        self,
        run_id: str,
        *,
        account_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCancelRunResponse:
        """
        Cancel a running assistant run.

        Args:
          account_id: Account ID for the request

          reason: Reason for cancellation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._delete(
            path_template("/active/v1/omni-ai/runs/{run_id}", run_id=run_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "reason": reason,
                },
                run_cancel_run_params.RunCancelRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunResponse,
        )

    def get_run(
        self,
        run_id: str,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetRunResponse:
        """
        Poll for the current status of a run and any new events since the last poll.

        Args:
          account_id: Account ID for the request

          page_size: Maximum events to return

          page_token: Page token for incremental polling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/active/v1/omni-ai/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    run_get_run_params.RunGetRunParams,
                ),
            ),
            cast_to=RunGetRunResponse,
        )

    def start_run(
        self,
        *,
        account_id: str,
        command_text: str,
        capabilities: List[Capability] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        thread_title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunStartRunResponse:
        """Begins an agentic conversation run.

        If thread_id is provided, continues an
        existing conversation; otherwise creates a new thread.

        Args:
          account_id: Account ID for the request

          command_text: The user's natural language command

          capabilities: Capabilities for structured actions

          thread_id: Optional thread ID to continue an existing conversation

          thread_title: Optional title for new threads

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/omni-ai/runs",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "command_text": command_text,
                    "capabilities": capabilities,
                    "thread_id": thread_id,
                    "thread_title": thread_title,
                },
                run_start_run_params.RunStartRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunStartRunResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    """AI assistant for conversational trading interactions."""

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def cancel_run(
        self,
        run_id: str,
        *,
        account_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCancelRunResponse:
        """
        Cancel a running assistant run.

        Args:
          account_id: Account ID for the request

          reason: Reason for cancellation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._delete(
            path_template("/active/v1/omni-ai/runs/{run_id}", run_id=run_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "reason": reason,
                },
                run_cancel_run_params.RunCancelRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunResponse,
        )

    async def get_run(
        self,
        run_id: str,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetRunResponse:
        """
        Poll for the current status of a run and any new events since the last poll.

        Args:
          account_id: Account ID for the request

          page_size: Maximum events to return

          page_token: Page token for incremental polling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/active/v1/omni-ai/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    run_get_run_params.RunGetRunParams,
                ),
            ),
            cast_to=RunGetRunResponse,
        )

    async def start_run(
        self,
        *,
        account_id: str,
        command_text: str,
        capabilities: List[Capability] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        thread_title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunStartRunResponse:
        """Begins an agentic conversation run.

        If thread_id is provided, continues an
        existing conversation; otherwise creates a new thread.

        Args:
          account_id: Account ID for the request

          command_text: The user's natural language command

          capabilities: Capabilities for structured actions

          thread_id: Optional thread ID to continue an existing conversation

          thread_title: Optional title for new threads

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/omni-ai/runs",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "command_text": command_text,
                    "capabilities": capabilities,
                    "thread_id": thread_id,
                    "thread_title": thread_title,
                },
                run_start_run_params.RunStartRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunStartRunResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.cancel_run = to_raw_response_wrapper(
            runs.cancel_run,
        )
        self.get_run = to_raw_response_wrapper(
            runs.get_run,
        )
        self.start_run = to_raw_response_wrapper(
            runs.start_run,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.cancel_run = async_to_raw_response_wrapper(
            runs.cancel_run,
        )
        self.get_run = async_to_raw_response_wrapper(
            runs.get_run,
        )
        self.start_run = async_to_raw_response_wrapper(
            runs.start_run,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.cancel_run = to_streamed_response_wrapper(
            runs.cancel_run,
        )
        self.get_run = to_streamed_response_wrapper(
            runs.get_run,
        )
        self.start_run = to_streamed_response_wrapper(
            runs.start_run,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.cancel_run = async_to_streamed_response_wrapper(
            runs.cancel_run,
        )
        self.get_run = async_to_streamed_response_wrapper(
            runs.get_run,
        )
        self.start_run = async_to_streamed_response_wrapper(
            runs.start_run,
        )
