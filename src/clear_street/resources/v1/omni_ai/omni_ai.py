# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .threads import (
    ThreadsResource,
    AsyncThreadsResource,
    ThreadsResourceWithRawResponse,
    AsyncThreadsResourceWithRawResponse,
    ThreadsResourceWithStreamingResponse,
    AsyncThreadsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from .responses import (
    ResponsesResource,
    AsyncResponsesResource,
    ResponsesResourceWithRawResponse,
    AsyncResponsesResourceWithRawResponse,
    ResponsesResourceWithStreamingResponse,
    AsyncResponsesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)

__all__ = ["OmniAIResource", "AsyncOmniAIResource"]


class OmniAIResource(SyncAPIResource):
    @cached_property
    def entitlements(self) -> EntitlementsResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return EntitlementsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return MessagesResource(self._client)

    @cached_property
    def responses(self) -> ResponsesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ResponsesResource(self._client)

    @cached_property
    def threads(self) -> ThreadsResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OmniAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OmniAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OmniAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return OmniAIResourceWithStreamingResponse(self)


class AsyncOmniAIResource(AsyncAPIResource):
    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncMessagesResource(self._client)

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncResponsesResource(self._client)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOmniAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOmniAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOmniAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncOmniAIResourceWithStreamingResponse(self)


class OmniAIResourceWithRawResponse:
    def __init__(self, omni_ai: OmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return EntitlementsResourceWithRawResponse(self._omni_ai.entitlements)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return MessagesResourceWithRawResponse(self._omni_ai.messages)

    @cached_property
    def responses(self) -> ResponsesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ResponsesResourceWithRawResponse(self._omni_ai.responses)

    @cached_property
    def threads(self) -> ThreadsResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ThreadsResourceWithRawResponse(self._omni_ai.threads)


class AsyncOmniAIResourceWithRawResponse:
    def __init__(self, omni_ai: AsyncOmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncEntitlementsResourceWithRawResponse(self._omni_ai.entitlements)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncMessagesResourceWithRawResponse(self._omni_ai.messages)

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncResponsesResourceWithRawResponse(self._omni_ai.responses)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncThreadsResourceWithRawResponse(self._omni_ai.threads)


class OmniAIResourceWithStreamingResponse:
    def __init__(self, omni_ai: OmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return EntitlementsResourceWithStreamingResponse(self._omni_ai.entitlements)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return MessagesResourceWithStreamingResponse(self._omni_ai.messages)

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ResponsesResourceWithStreamingResponse(self._omni_ai.responses)

    @cached_property
    def threads(self) -> ThreadsResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return ThreadsResourceWithStreamingResponse(self._omni_ai.threads)


class AsyncOmniAIResourceWithStreamingResponse:
    def __init__(self, omni_ai: AsyncOmniAIResource) -> None:
        self._omni_ai = omni_ai

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncEntitlementsResourceWithStreamingResponse(self._omni_ai.entitlements)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncMessagesResourceWithStreamingResponse(self._omni_ai.messages)

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncResponsesResourceWithStreamingResponse(self._omni_ai.responses)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
        """
        return AsyncThreadsResourceWithStreamingResponse(self._omni_ai.threads)
