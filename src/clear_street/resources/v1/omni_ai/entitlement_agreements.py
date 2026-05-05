# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.omni_ai.entitlement_agreement_get_entitlement_agreements_response import (
    EntitlementAgreementGetEntitlementAgreementsResponse,
)

__all__ = ["EntitlementAgreementsResource", "AsyncEntitlementAgreementsResource"]


class EntitlementAgreementsResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> EntitlementAgreementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return EntitlementAgreementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitlementAgreementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return EntitlementAgreementsResourceWithStreamingResponse(self)

    def get_entitlement_agreements(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementAgreementGetEntitlementAgreementsResponse:
        """List current signable entitlement agreements for consent UX."""
        return self._get(
            "/v1/omni-ai/entitlement-agreements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementAgreementGetEntitlementAgreementsResponse,
        )


class AsyncEntitlementAgreementsResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEntitlementAgreementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitlementAgreementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitlementAgreementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncEntitlementAgreementsResourceWithStreamingResponse(self)

    async def get_entitlement_agreements(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementAgreementGetEntitlementAgreementsResponse:
        """List current signable entitlement agreements for consent UX."""
        return await self._get(
            "/v1/omni-ai/entitlement-agreements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementAgreementGetEntitlementAgreementsResponse,
        )


class EntitlementAgreementsResourceWithRawResponse:
    def __init__(self, entitlement_agreements: EntitlementAgreementsResource) -> None:
        self._entitlement_agreements = entitlement_agreements

        self.get_entitlement_agreements = to_raw_response_wrapper(
            entitlement_agreements.get_entitlement_agreements,
        )


class AsyncEntitlementAgreementsResourceWithRawResponse:
    def __init__(self, entitlement_agreements: AsyncEntitlementAgreementsResource) -> None:
        self._entitlement_agreements = entitlement_agreements

        self.get_entitlement_agreements = async_to_raw_response_wrapper(
            entitlement_agreements.get_entitlement_agreements,
        )


class EntitlementAgreementsResourceWithStreamingResponse:
    def __init__(self, entitlement_agreements: EntitlementAgreementsResource) -> None:
        self._entitlement_agreements = entitlement_agreements

        self.get_entitlement_agreements = to_streamed_response_wrapper(
            entitlement_agreements.get_entitlement_agreements,
        )


class AsyncEntitlementAgreementsResourceWithStreamingResponse:
    def __init__(self, entitlement_agreements: AsyncEntitlementAgreementsResource) -> None:
        self._entitlement_agreements = entitlement_agreements

        self.get_entitlement_agreements = async_to_streamed_response_wrapper(
            entitlement_agreements.get_entitlement_agreements,
        )
