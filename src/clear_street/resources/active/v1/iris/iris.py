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

__all__ = ["IrisResource", "AsyncIrisResource"]


class IrisResource(SyncAPIResource):
    @cached_property
    def feedback(self) -> FeedbackResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return FeedbackResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return RunsResource(self._client)

    @cached_property
    def threads(self) -> ThreadsResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return ThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IrisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return IrisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IrisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return IrisResourceWithStreamingResponse(self)


class AsyncIrisResource(AsyncAPIResource):
    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncFeedbackResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncRunsResource(self._client)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIrisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIrisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIrisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncIrisResourceWithStreamingResponse(self)


class IrisResourceWithRawResponse:
    def __init__(self, iris: IrisResource) -> None:
        self._iris = iris

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return FeedbackResourceWithRawResponse(self._iris.feedback)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return RunsResourceWithRawResponse(self._iris.runs)

    @cached_property
    def threads(self) -> ThreadsResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return ThreadsResourceWithRawResponse(self._iris.threads)


class AsyncIrisResourceWithRawResponse:
    def __init__(self, iris: AsyncIrisResource) -> None:
        self._iris = iris

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncFeedbackResourceWithRawResponse(self._iris.feedback)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncRunsResourceWithRawResponse(self._iris.runs)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncThreadsResourceWithRawResponse(self._iris.threads)


class IrisResourceWithStreamingResponse:
    def __init__(self, iris: IrisResource) -> None:
        self._iris = iris

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return FeedbackResourceWithStreamingResponse(self._iris.feedback)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return RunsResourceWithStreamingResponse(self._iris.runs)

    @cached_property
    def threads(self) -> ThreadsResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return ThreadsResourceWithStreamingResponse(self._iris.threads)


class AsyncIrisResourceWithStreamingResponse:
    def __init__(self, iris: AsyncIrisResource) -> None:
        self._iris = iris

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncFeedbackResourceWithStreamingResponse(self._iris.feedback)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncRunsResourceWithStreamingResponse(self._iris.runs)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncThreadsResourceWithStreamingResponse(self._iris.threads)
