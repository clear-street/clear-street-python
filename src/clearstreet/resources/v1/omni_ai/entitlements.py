# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.v1.omni_ai import entitlement_get_entitlements_params, entitlement_create_entitlements_params
from ....types.v1.entitlement_code import EntitlementCode
from ....types.v1.omni_ai.entitlement_get_entitlements_response import EntitlementGetEntitlementsResponse
from ....types.v1.omni_ai.entitlement_delete_entitlement_response import EntitlementDeleteEntitlementResponse
from ....types.v1.omni_ai.entitlement_create_entitlements_response import EntitlementCreateEntitlementsResponse
from ....types.v1.omni_ai.entitlement_get_entitlement_agreements_response import (
    EntitlementGetEntitlementAgreementsResponse,
)

__all__ = ["EntitlementsResource", "AsyncEntitlementsResource"]


class EntitlementsResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use account_ids.
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
        account_ids: Iterable[int],
        agreement_id: str,
        entitlement_codes: List[EntitlementCode],
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
                    "account_ids": account_ids,
                    "agreement_id": agreement_id,
                    "entitlement_codes": entitlement_codes,
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

    def get_entitlement_agreements(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementGetEntitlementAgreementsResponse:
        """List current signable entitlement agreements for consent UX."""
        return self._get(
            "/v1/omni-ai/entitlement-agreements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementGetEntitlementAgreementsResponse,
        )

    def get_entitlements(
        self,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementGetEntitlementsResponse:
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
                    {"account_id": account_id}, entitlement_get_entitlements_params.EntitlementGetEntitlementsParams
                ),
            ),
            cast_to=EntitlementGetEntitlementsResponse,
        )


class AsyncEntitlementsResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use account_ids.
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
        account_ids: Iterable[int],
        agreement_id: str,
        entitlement_codes: List[EntitlementCode],
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
                    "account_ids": account_ids,
                    "agreement_id": agreement_id,
                    "entitlement_codes": entitlement_codes,
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

    async def get_entitlement_agreements(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementGetEntitlementAgreementsResponse:
        """List current signable entitlement agreements for consent UX."""
        return await self._get(
            "/v1/omni-ai/entitlement-agreements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementGetEntitlementAgreementsResponse,
        )

    async def get_entitlements(
        self,
        *,
        account_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementGetEntitlementsResponse:
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
                    {"account_id": account_id}, entitlement_get_entitlements_params.EntitlementGetEntitlementsParams
                ),
            ),
            cast_to=EntitlementGetEntitlementsResponse,
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
        self.get_entitlement_agreements = to_raw_response_wrapper(
            entitlements.get_entitlement_agreements,
        )
        self.get_entitlements = to_raw_response_wrapper(
            entitlements.get_entitlements,
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
        self.get_entitlement_agreements = async_to_raw_response_wrapper(
            entitlements.get_entitlement_agreements,
        )
        self.get_entitlements = async_to_raw_response_wrapper(
            entitlements.get_entitlements,
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
        self.get_entitlement_agreements = to_streamed_response_wrapper(
            entitlements.get_entitlement_agreements,
        )
        self.get_entitlements = to_streamed_response_wrapper(
            entitlements.get_entitlements,
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
        self.get_entitlement_agreements = async_to_streamed_response_wrapper(
            entitlements.get_entitlement_agreements,
        )
        self.get_entitlements = async_to_streamed_response_wrapper(
            entitlements.get_entitlements,
        )
