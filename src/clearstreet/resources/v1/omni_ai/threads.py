# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
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
from ....types.v1.omni_ai import (
    thread_get_threads_params,
    thread_get_messages_params,
    thread_create_thread_params,
    thread_create_message_params,
    thread_get_thread_by_id_params,
    thread_get_thread_response_params,
)
from ....types.v1.omni_ai.turn_context_param import TurnContextParam
from ....types.v1.omni_ai.thread_get_threads_response import ThreadGetThreadsResponse
from ....types.v1.omni_ai.thread_get_messages_response import ThreadGetMessagesResponse
from ....types.v1.omni_ai.thread_create_thread_response import ThreadCreateThreadResponse
from ....types.v1.omni_ai.thread_create_message_response import ThreadCreateMessageResponse
from ....types.v1.omni_ai.thread_get_thread_by_id_response import ThreadGetThreadByIDResponse
from ....types.v1.omni_ai.thread_get_thread_response_response import ThreadGetThreadResponseResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use account_ids.
    """

    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ThreadsResourceWithStreamingResponse(self)

    def create_message(
        self,
        thread_id: str,
        *,
        text: str,
        account_id: Optional[int] | Omit = omit,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        context: Optional[TurnContextParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateMessageResponse:
        """
        Append a user message to an existing thread and start an assistant response.
        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Only one response may be active per thread. Wait for it to reach a terminal
        status before submitting another turn; otherwise this endpoint returns 409.

        The first accepted selected-account message links an unlinked thread. A linked
        thread keeps its account regardless of omission or another selection. A changed
        scope also returns 409 without accepting a turn.

        Args:
          account_id: Selected account for creation or the first account-linked turn. Omit for an
              unlinked conversation. An existing account link remains authoritative even when
              another account is selected.

          context: Snapshots for this instant-chat message. Omission does not remove earlier
              attachments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._post(
            path_template("/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            body=maybe_transform(
                {
                    "text": text,
                    "account_id": account_id,
                    "capabilities": capabilities,
                    "context": context,
                },
                thread_create_message_params.ThreadCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateMessageResponse,
        )

    def create_thread(
        self,
        *,
        type: Literal["instant", "deep_insights"],
        account_id: Optional[int] | Omit = omit,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        context: Optional[TurnContextParam] | Omit = omit,
        target: Optional[thread_create_thread_params.Target] | Omit = omit,
        text: Optional[str] | Omit = omit,
        thesis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateThreadResponse:
        """Atomically create a conversation and submit its first user turn.

        Use `instant`
        with `text` for a prompt, or `deep_insights` with a ticker `target` and optional
        `thesis` for long-form research.

        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Omit `account_id` to start without an account. The first accepted turn with a
        selected account links that account permanently. Reuse `Idempotency-Key` only
        for an identical request.

        Args:
          type: Thread creation mode.

          account_id: Selected account for creation or the first account-linked turn. Omit for an
              unlinked conversation. An existing account link remains authoritative even when
              another account is selected.

          context: Snapshots for the first instant-chat message. Omit to attach no new context.

          target: Deep-insights target payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/omni-ai/threads",
            body=maybe_transform(
                {
                    "type": type,
                    "account_id": account_id,
                    "capabilities": capabilities,
                    "context": context,
                    "target": target,
                    "text": text,
                    "thesis": thesis,
                },
                thread_create_thread_params.ThreadCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateThreadResponse,
        )

    def get_messages(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetMessagesResponse:
        """
        List finalized messages, including messages created before the account link.
        Return the latest page by default, in chronological order within each page. Use
        the returned page token to navigate history.

        In-progress assistant output is not included. Poll
        `GET /omni-ai/responses/{response_id}` until the response reaches a terminal
        status, then read its finalized message here.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
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
                    thread_get_messages_params.ThreadGetMessagesParams,
                ),
            ),
            cast_to=ThreadGetMessagesResponse,
        )

    def get_thread_by_id(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadByIDResponse:
        """Read an owned thread's metadata.

        Use `GET /omni-ai/threads/{thread_id}/messages`
        for conversation history.

        Omission or another account selection does not change authorization.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/omni-ai/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, thread_get_thread_by_id_params.ThreadGetThreadByIDParams
                ),
            ),
            cast_to=ThreadGetThreadByIDResponse,
        )

    def get_thread_response(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadResponseResponse:
        """Look up the currently active response without knowing its `response_id`.

        Use
        this endpoint when reopening a thread whose assistant turn may still be in
        progress.

        An idle owned thread returns HTTP 200 with `data: null`.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/omni-ai/threads/{thread_id}/response", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, thread_get_thread_response_params.ThreadGetThreadResponseParams
                ),
            ),
            cast_to=ThreadGetThreadResponseResponse,
        )

    def get_threads(
        self,
        *,
        account_id: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadsResponse:
        """List authorized conversation metadata, newest first.

        Use `page_size` and
        `page_token` for pagination, and the messages endpoint for conversation history.

        With `account_id`, list only conversations linked to that account and require
        current account access. Without it, list only conversations with no linked
        account.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/omni-ai/threads",
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
                    thread_get_threads_params.ThreadGetThreadsParams,
                ),
            ),
            cast_to=ThreadGetThreadsResponse,
        )


class AsyncThreadsResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use account_ids.
    """

    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncThreadsResourceWithStreamingResponse(self)

    async def create_message(
        self,
        thread_id: str,
        *,
        text: str,
        account_id: Optional[int] | Omit = omit,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        context: Optional[TurnContextParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateMessageResponse:
        """
        Append a user message to an existing thread and start an assistant response.
        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Only one response may be active per thread. Wait for it to reach a terminal
        status before submitting another turn; otherwise this endpoint returns 409.

        The first accepted selected-account message links an unlinked thread. A linked
        thread keeps its account regardless of omission or another selection. A changed
        scope also returns 409 without accepting a turn.

        Args:
          account_id: Selected account for creation or the first account-linked turn. Omit for an
              unlinked conversation. An existing account link remains authoritative even when
              another account is selected.

          context: Snapshots for this instant-chat message. Omission does not remove earlier
              attachments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._post(
            path_template("/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "account_id": account_id,
                    "capabilities": capabilities,
                    "context": context,
                },
                thread_create_message_params.ThreadCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateMessageResponse,
        )

    async def create_thread(
        self,
        *,
        type: Literal["instant", "deep_insights"],
        account_id: Optional[int] | Omit = omit,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        context: Optional[TurnContextParam] | Omit = omit,
        target: Optional[thread_create_thread_params.Target] | Omit = omit,
        text: Optional[str] | Omit = omit,
        thesis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateThreadResponse:
        """Atomically create a conversation and submit its first user turn.

        Use `instant`
        with `text` for a prompt, or `deep_insights` with a ticker `target` and optional
        `thesis` for long-form research.

        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Omit `account_id` to start without an account. The first accepted turn with a
        selected account links that account permanently. Reuse `Idempotency-Key` only
        for an identical request.

        Args:
          type: Thread creation mode.

          account_id: Selected account for creation or the first account-linked turn. Omit for an
              unlinked conversation. An existing account link remains authoritative even when
              another account is selected.

          context: Snapshots for the first instant-chat message. Omit to attach no new context.

          target: Deep-insights target payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/omni-ai/threads",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "account_id": account_id,
                    "capabilities": capabilities,
                    "context": context,
                    "target": target,
                    "text": text,
                    "thesis": thesis,
                },
                thread_create_thread_params.ThreadCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateThreadResponse,
        )

    async def get_messages(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetMessagesResponse:
        """
        List finalized messages, including messages created before the account link.
        Return the latest page by default, in chronological order within each page. Use
        the returned page token to navigate history.

        In-progress assistant output is not included. Poll
        `GET /omni-ai/responses/{response_id}` until the response reaches a terminal
        status, then read its finalized message here.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
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
                    thread_get_messages_params.ThreadGetMessagesParams,
                ),
            ),
            cast_to=ThreadGetMessagesResponse,
        )

    async def get_thread_by_id(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadByIDResponse:
        """Read an owned thread's metadata.

        Use `GET /omni-ai/threads/{thread_id}/messages`
        for conversation history.

        Omission or another account selection does not change authorization.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/omni-ai/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, thread_get_thread_by_id_params.ThreadGetThreadByIDParams
                ),
            ),
            cast_to=ThreadGetThreadByIDResponse,
        )

    async def get_thread_response(
        self,
        thread_id: str,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadResponseResponse:
        """Look up the currently active response without knowing its `response_id`.

        Use
        this endpoint when reopening a thread whose assistant turn may still be in
        progress.

        An idle owned thread returns HTTP 200 with `data: null`.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/omni-ai/threads/{thread_id}/response", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, thread_get_thread_response_params.ThreadGetThreadResponseParams
                ),
            ),
            cast_to=ThreadGetThreadResponseResponse,
        )

    async def get_threads(
        self,
        *,
        account_id: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadsResponse:
        """List authorized conversation metadata, newest first.

        Use `page_size` and
        `page_token` for pagination, and the messages endpoint for conversation history.

        With `account_id`, list only conversations linked to that account and require
        current account access. Without it, list only conversations with no linked
        account.

        Args:
          account_id: Lists only conversations for this account, or unlinked conversations when
              omitted. Other reads authorize the resource's linked account. Omit when no
              account is selected; empty values and the string null are invalid.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/omni-ai/threads",
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
                    thread_get_threads_params.ThreadGetThreadsParams,
                ),
            ),
            cast_to=ThreadGetThreadsResponse,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create_message = to_raw_response_wrapper(
            threads.create_message,
        )
        self.create_thread = to_raw_response_wrapper(
            threads.create_thread,
        )
        self.get_messages = to_raw_response_wrapper(
            threads.get_messages,
        )
        self.get_thread_by_id = to_raw_response_wrapper(
            threads.get_thread_by_id,
        )
        self.get_thread_response = to_raw_response_wrapper(
            threads.get_thread_response,
        )
        self.get_threads = to_raw_response_wrapper(
            threads.get_threads,
        )


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create_message = async_to_raw_response_wrapper(
            threads.create_message,
        )
        self.create_thread = async_to_raw_response_wrapper(
            threads.create_thread,
        )
        self.get_messages = async_to_raw_response_wrapper(
            threads.get_messages,
        )
        self.get_thread_by_id = async_to_raw_response_wrapper(
            threads.get_thread_by_id,
        )
        self.get_thread_response = async_to_raw_response_wrapper(
            threads.get_thread_response,
        )
        self.get_threads = async_to_raw_response_wrapper(
            threads.get_threads,
        )


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create_message = to_streamed_response_wrapper(
            threads.create_message,
        )
        self.create_thread = to_streamed_response_wrapper(
            threads.create_thread,
        )
        self.get_messages = to_streamed_response_wrapper(
            threads.get_messages,
        )
        self.get_thread_by_id = to_streamed_response_wrapper(
            threads.get_thread_by_id,
        )
        self.get_thread_response = to_streamed_response_wrapper(
            threads.get_thread_response,
        )
        self.get_threads = to_streamed_response_wrapper(
            threads.get_threads,
        )


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create_message = async_to_streamed_response_wrapper(
            threads.create_message,
        )
        self.create_thread = async_to_streamed_response_wrapper(
            threads.create_thread,
        )
        self.get_messages = async_to_streamed_response_wrapper(
            threads.get_messages,
        )
        self.get_thread_by_id = async_to_streamed_response_wrapper(
            threads.get_thread_by_id,
        )
        self.get_thread_response = async_to_streamed_response_wrapper(
            threads.get_thread_response,
        )
        self.get_threads = async_to_streamed_response_wrapper(
            threads.get_threads,
        )
