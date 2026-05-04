# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.v1.omni_ai import entitlement_list_entitlements_params, entitlement_create_entitlements_params
from ....types.v1.omni_ai.entitlement_list_entitlements_response import EntitlementListEntitlementsResponse
from ....types.v1.omni_ai.entitlement_delete_entitlement_response import EntitlementDeleteEntitlementResponse
from ....types.v1.omni_ai.entitlement_create_entitlements_response import EntitlementCreateEntitlementsResponse

__all__ = ["EntitlementsResource", "AsyncEntitlementsResource"]


class EntitlementsResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> EntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return EntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return EntitlementsResourceWithStreamingResponse(self)

    def create_entitlements(
        self,
        *,
        agreement_id: str,
        requested_entitlement_codes: SequenceNotStr[str],
        trading_account_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateEntitlementsResponse:
        """
        Record consent and upsert one-or-more active grants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/omni-ai/entitlements",
            body=maybe_transform(
                {
                    "agreement_id": agreement_id,
                    "requested_entitlement_codes": requested_entitlement_codes,
                    "trading_account_ids": trading_account_ids,
                },
                entitlement_create_entitlements_params.EntitlementCreateEntitlementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateEntitlementsResponse,
        )

    def delete_entitlement(
        self,
        entitlement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementDeleteEntitlementResponse:
        """
        Revoke one entitlement grant by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entitlement_id:
            raise ValueError(f"Expected a non-empty value for `entitlement_id` but received {entitlement_id!r}")
        return self._delete(
            path_template("/v1/omni-ai/entitlements/{entitlement_id}", entitlement_id=entitlement_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementDeleteEntitlementResponse,
        )

    def list_entitlements(
        self,
        *,
        trading_account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementListEntitlementsResponse:
        """
        List caller's active entitlement grants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/omni-ai/entitlements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"trading_account_id": trading_account_id},
                    entitlement_list_entitlements_params.EntitlementListEntitlementsParams,
                ),
            ),
            cast_to=EntitlementListEntitlementsResponse,
        )


class AsyncEntitlementsResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncEntitlementsResourceWithStreamingResponse(self)

    async def create_entitlements(
        self,
        *,
        agreement_id: str,
        requested_entitlement_codes: SequenceNotStr[str],
        trading_account_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateEntitlementsResponse:
        """
        Record consent and upsert one-or-more active grants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/omni-ai/entitlements",
            body=await async_maybe_transform(
                {
                    "agreement_id": agreement_id,
                    "requested_entitlement_codes": requested_entitlement_codes,
                    "trading_account_ids": trading_account_ids,
                },
                entitlement_create_entitlements_params.EntitlementCreateEntitlementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateEntitlementsResponse,
        )

    async def delete_entitlement(
        self,
        entitlement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementDeleteEntitlementResponse:
        """
        Revoke one entitlement grant by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entitlement_id:
            raise ValueError(f"Expected a non-empty value for `entitlement_id` but received {entitlement_id!r}")
        return await self._delete(
            path_template("/v1/omni-ai/entitlements/{entitlement_id}", entitlement_id=entitlement_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementDeleteEntitlementResponse,
        )

    async def list_entitlements(
        self,
        *,
        trading_account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementListEntitlementsResponse:
        """
        List caller's active entitlement grants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/omni-ai/entitlements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"trading_account_id": trading_account_id},
                    entitlement_list_entitlements_params.EntitlementListEntitlementsParams,
                ),
            ),
            cast_to=EntitlementListEntitlementsResponse,
        )


class EntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create_entitlements = to_raw_response_wrapper(
            entitlements.create_entitlements,
        )
        self.delete_entitlement = to_raw_response_wrapper(
            entitlements.delete_entitlement,
        )
        self.list_entitlements = to_raw_response_wrapper(
            entitlements.list_entitlements,
        )


class AsyncEntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create_entitlements = async_to_raw_response_wrapper(
            entitlements.create_entitlements,
        )
        self.delete_entitlement = async_to_raw_response_wrapper(
            entitlements.delete_entitlement,
        )
        self.list_entitlements = async_to_raw_response_wrapper(
            entitlements.list_entitlements,
        )


class EntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create_entitlements = to_streamed_response_wrapper(
            entitlements.create_entitlements,
        )
        self.delete_entitlement = to_streamed_response_wrapper(
            entitlements.delete_entitlement,
        )
        self.list_entitlements = to_streamed_response_wrapper(
            entitlements.list_entitlements,
        )


class AsyncEntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create_entitlements = async_to_streamed_response_wrapper(
            entitlements.create_entitlements,
        )
        self.delete_entitlement = async_to_streamed_response_wrapper(
            entitlements.delete_entitlement,
        )
        self.list_entitlements = async_to_streamed_response_wrapper(
            entitlements.list_entitlements,
        )
