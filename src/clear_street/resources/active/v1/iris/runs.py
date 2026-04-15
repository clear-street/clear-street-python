# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
from .....types.active.v1.iris import (
    run_get_run_deprecated_params,
    run_start_run_deprecated_params,
    run_cancel_run_deprecated_params,
)
from .....types.active.v1.capability import Capability
from .....types.active.v1.iris.run_get_run_deprecated_response import RunGetRunDeprecatedResponse
from .....types.active.v1.iris.run_start_run_deprecated_response import RunStartRunDeprecatedResponse
from .....types.active.v1.iris.run_cancel_run_deprecated_response import RunCancelRunDeprecatedResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def cancel_run_deprecated(
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
    ) -> RunCancelRunDeprecatedResponse:
        """
        **Deprecated**: Use `DELETE /omni-ai/runs/{run_id}` instead.

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
            path_template("/active/v1/iris/runs/{run_id}", run_id=run_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "reason": reason,
                },
                run_cancel_run_deprecated_params.RunCancelRunDeprecatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_run_deprecated(
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
    ) -> RunGetRunDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/runs/{run_id}` instead.

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
            path_template("/active/v1/iris/runs/{run_id}", run_id=run_id),
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
                    run_get_run_deprecated_params.RunGetRunDeprecatedParams,
                ),
            ),
            cast_to=RunGetRunDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def start_run_deprecated(
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
    ) -> RunStartRunDeprecatedResponse:
        """
        **Deprecated**: Use `POST /omni-ai/runs` instead.

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
            "/active/v1/iris/runs",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "command_text": command_text,
                    "capabilities": capabilities,
                    "thread_id": thread_id,
                    "thread_title": thread_title,
                },
                run_start_run_deprecated_params.RunStartRunDeprecatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunStartRunDeprecatedResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def cancel_run_deprecated(
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
    ) -> RunCancelRunDeprecatedResponse:
        """
        **Deprecated**: Use `DELETE /omni-ai/runs/{run_id}` instead.

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
            path_template("/active/v1/iris/runs/{run_id}", run_id=run_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "reason": reason,
                },
                run_cancel_run_deprecated_params.RunCancelRunDeprecatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_run_deprecated(
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
    ) -> RunGetRunDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/runs/{run_id}` instead.

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
            path_template("/active/v1/iris/runs/{run_id}", run_id=run_id),
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
                    run_get_run_deprecated_params.RunGetRunDeprecatedParams,
                ),
            ),
            cast_to=RunGetRunDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def start_run_deprecated(
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
    ) -> RunStartRunDeprecatedResponse:
        """
        **Deprecated**: Use `POST /omni-ai/runs` instead.

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
            "/active/v1/iris/runs",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "command_text": command_text,
                    "capabilities": capabilities,
                    "thread_id": thread_id,
                    "thread_title": thread_title,
                },
                run_start_run_deprecated_params.RunStartRunDeprecatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunStartRunDeprecatedResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.cancel_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.cancel_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.get_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.start_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.cancel_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.cancel_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.get_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.start_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.cancel_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.cancel_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.get_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start_run_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.start_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.cancel_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.cancel_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.get_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start_run_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.start_run_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
