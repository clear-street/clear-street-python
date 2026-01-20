# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .prompts import (
    PromptsResource,
    AsyncPromptsResource,
    PromptsResourceWithRawResponse,
    AsyncPromptsResourceWithRawResponse,
    PromptsResourceWithStreamingResponse,
    AsyncPromptsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AssistantResource", "AsyncAssistantResource"]


class AssistantResource(SyncAPIResource):
    @cached_property
    def prompts(self) -> PromptsResource:
        return PromptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssistantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AssistantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssistantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AssistantResourceWithStreamingResponse(self)


class AsyncAssistantResource(AsyncAPIResource):
    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        return AsyncPromptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssistantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssistantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssistantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncAssistantResourceWithStreamingResponse(self)


class AssistantResourceWithRawResponse:
    def __init__(self, assistant: AssistantResource) -> None:
        self._assistant = assistant

    @cached_property
    def prompts(self) -> PromptsResourceWithRawResponse:
        return PromptsResourceWithRawResponse(self._assistant.prompts)


class AsyncAssistantResourceWithRawResponse:
    def __init__(self, assistant: AsyncAssistantResource) -> None:
        self._assistant = assistant

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithRawResponse:
        return AsyncPromptsResourceWithRawResponse(self._assistant.prompts)


class AssistantResourceWithStreamingResponse:
    def __init__(self, assistant: AssistantResource) -> None:
        self._assistant = assistant

    @cached_property
    def prompts(self) -> PromptsResourceWithStreamingResponse:
        return PromptsResourceWithStreamingResponse(self._assistant.prompts)


class AsyncAssistantResourceWithStreamingResponse:
    def __init__(self, assistant: AsyncAssistantResource) -> None:
        self._assistant = assistant

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithStreamingResponse:
        return AsyncPromptsResourceWithStreamingResponse(self._assistant.prompts)
