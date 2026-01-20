# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.assistant import prompt_run_prompt_params, prompt_get_prompt_result_params
from .....types.active.v1.assistant.prompt_run_prompt_response import PromptRunPromptResponse
from .....types.active.v1.assistant.prompt_get_prompt_result_response import PromptGetPromptResultResponse

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return PromptsResourceWithStreamingResponse(self)

    def get_prompt_result(
        self,
        id: str,
        *,
        return_all_outputs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetPromptResultResponse:
        """
        Retrieve the status and outputs of a prompt workflow by ID.

        Args:
          return_all_outputs: When true, return intermediate outputs for all nodes in the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/active/v1/assistant/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"return_all_outputs": return_all_outputs},
                    prompt_get_prompt_result_params.PromptGetPromptResultParams,
                ),
            ),
            cast_to=PromptGetPromptResultResponse,
        )

    def run_prompt(
        self,
        *,
        body: object,
        slug: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptRunPromptResponse:
        """
        Forwards an arbitrary JSON payload to an Iris prompt identified by `slug` and
        returns a handle that can be used to poll for results.

        Args:
          body: JSON payload forwarded to the prompt workflow.

          slug: Unique slug identifying the prompt workflow to execute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/assistant/prompts",
            body=maybe_transform(
                {
                    "body": body,
                    "slug": slug,
                    "metadata": metadata,
                },
                prompt_run_prompt_params.PromptRunPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptRunPromptResponse,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def get_prompt_result(
        self,
        id: str,
        *,
        return_all_outputs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetPromptResultResponse:
        """
        Retrieve the status and outputs of a prompt workflow by ID.

        Args:
          return_all_outputs: When true, return intermediate outputs for all nodes in the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/active/v1/assistant/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_all_outputs": return_all_outputs},
                    prompt_get_prompt_result_params.PromptGetPromptResultParams,
                ),
            ),
            cast_to=PromptGetPromptResultResponse,
        )

    async def run_prompt(
        self,
        *,
        body: object,
        slug: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptRunPromptResponse:
        """
        Forwards an arbitrary JSON payload to an Iris prompt identified by `slug` and
        returns a handle that can be used to poll for results.

        Args:
          body: JSON payload forwarded to the prompt workflow.

          slug: Unique slug identifying the prompt workflow to execute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/assistant/prompts",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "slug": slug,
                    "metadata": metadata,
                },
                prompt_run_prompt_params.PromptRunPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptRunPromptResponse,
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.get_prompt_result = to_raw_response_wrapper(
            prompts.get_prompt_result,
        )
        self.run_prompt = to_raw_response_wrapper(
            prompts.run_prompt,
        )


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.get_prompt_result = async_to_raw_response_wrapper(
            prompts.get_prompt_result,
        )
        self.run_prompt = async_to_raw_response_wrapper(
            prompts.run_prompt,
        )


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.get_prompt_result = to_streamed_response_wrapper(
            prompts.get_prompt_result,
        )
        self.run_prompt = to_streamed_response_wrapper(
            prompts.run_prompt,
        )


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.get_prompt_result = async_to_streamed_response_wrapper(
            prompts.get_prompt_result,
        )
        self.run_prompt = async_to_streamed_response_wrapper(
            prompts.run_prompt,
        )
