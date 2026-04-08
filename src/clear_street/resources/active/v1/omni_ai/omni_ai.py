# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .threads.threads import (
    ThreadsResource,
    AsyncThreadsResource,
    ThreadsResourceWithRawResponse,
    AsyncThreadsResourceWithRawResponse,
    ThreadsResourceWithStreamingResponse,
    AsyncThreadsResourceWithStreamingResponse,
)

__all__ = ["OmniAIResource", "AsyncOmniAIResource"]


class OmniAIResource(SyncAPIResource):
    @cached_property
    def feedback(self) -> FeedbackResource:
        """AI assistant for conversational trading interactions."""
        return FeedbackResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        """AI assistant for conversational trading interactions."""
        return RunsResource(self._client)

    @cached_property
    def threads(self) -> ThreadsResource:
        """AI assistant for conversational trading interactions."""
        return ThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OmniAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OmniAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OmniAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return OmniAIResourceWithStreamingResponse(self)


class AsyncOmniAIResource(AsyncAPIResource):
    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        """AI assistant for conversational trading interactions."""
        return AsyncFeedbackResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """AI assistant for conversational trading interactions."""
        return AsyncRunsResource(self._client)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        """AI assistant for conversational trading interactions."""
        return AsyncThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOmniAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOmniAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOmniAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncOmniAIResourceWithStreamingResponse(self)


class OmniAIResourceWithRawResponse:
    def __init__(self, omni_ai: OmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return FeedbackResourceWithRawResponse(self._omni_ai.feedback)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return RunsResourceWithRawResponse(self._omni_ai.runs)

    @cached_property
    def threads(self) -> ThreadsResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return ThreadsResourceWithRawResponse(self._omni_ai.threads)


class AsyncOmniAIResourceWithRawResponse:
    def __init__(self, omni_ai: AsyncOmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncFeedbackResourceWithRawResponse(self._omni_ai.feedback)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncRunsResourceWithRawResponse(self._omni_ai.runs)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithRawResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncThreadsResourceWithRawResponse(self._omni_ai.threads)


class OmniAIResourceWithStreamingResponse:
    def __init__(self, omni_ai: OmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return FeedbackResourceWithStreamingResponse(self._omni_ai.feedback)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return RunsResourceWithStreamingResponse(self._omni_ai.runs)

    @cached_property
    def threads(self) -> ThreadsResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return ThreadsResourceWithStreamingResponse(self._omni_ai.threads)


class AsyncOmniAIResourceWithStreamingResponse:
    def __init__(self, omni_ai: AsyncOmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncFeedbackResourceWithStreamingResponse(self._omni_ai.feedback)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncRunsResourceWithStreamingResponse(self._omni_ai.runs)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithStreamingResponse:
        """AI assistant for conversational trading interactions."""
        return AsyncThreadsResourceWithStreamingResponse(self._omni_ai.threads)
