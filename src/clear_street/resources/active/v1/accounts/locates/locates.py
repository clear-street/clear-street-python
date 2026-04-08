# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable

import httpx

from .inventory import (
    InventoryResource,
    AsyncInventoryResource,
    InventoryResourceWithRawResponse,
    AsyncInventoryResourceWithRawResponse,
    InventoryResourceWithStreamingResponse,
    AsyncInventoryResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.active.v1.accounts import (
    LocateOrderStatus,
    locate_get_locate_requests_params,
    locate_create_locate_request_params,
    locate_update_locate_request_params,
)
from ......types.active.v1.accounts.locate_order_status import LocateOrderStatus
from ......types.active.v1.accounts.locate_get_locate_requests_response import LocateGetLocateRequestsResponse
from ......types.active.v1.accounts.locate_create_locate_request_response import LocateCreateLocateRequestResponse
from ......types.active.v1.accounts.locate_update_locate_request_response import LocateUpdateLocateRequestResponse

__all__ = ["LocatesResource", "AsyncLocatesResource"]


class LocatesResource(SyncAPIResource):
    """Manage locate requests for short selling."""

    @cached_property
    def inventory(self) -> InventoryResource:
        """Manage locate requests for short selling."""
        return InventoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LocatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return LocatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return LocatesResourceWithStreamingResponse(self)

    def create_locate_request(
        self,
        account_id: int,
        *,
        body: Iterable[locate_create_locate_request_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateCreateLocateRequestResponse:
        """
        Submits a new short stock locate request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            body=maybe_transform(body, Iterable[locate_create_locate_request_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateCreateLocateRequestResponse,
        )

    def get_locate_requests(
        self,
        account_id: int,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        reference_id: str | Omit = omit,
        status: LocateOrderStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRequestsResponse:
        """
        Retrieves all locate requests for the specified account.

        Args:
          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          reference_id: Filter by client reference ID

          status: Filter by locate order status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "reference_id": reference_id,
                        "status": status,
                    },
                    locate_get_locate_requests_params.LocateGetLocateRequestsParams,
                ),
            ),
            cast_to=LocateGetLocateRequestsResponse,
        )

    def update_locate_request(
        self,
        account_id: int,
        *,
        accept: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateUpdateLocateRequestResponse:
        """
        Modifies an existing locate request.

        Args:
          accept: Whether to accept (`true`) or decline (`false`) the locate offer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            body=maybe_transform(
                {"accept": accept}, locate_update_locate_request_params.LocateUpdateLocateRequestParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateUpdateLocateRequestResponse,
        )


class AsyncLocatesResource(AsyncAPIResource):
    """Manage locate requests for short selling."""

    @cached_property
    def inventory(self) -> AsyncInventoryResource:
        """Manage locate requests for short selling."""
        return AsyncInventoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncLocatesResourceWithStreamingResponse(self)

    async def create_locate_request(
        self,
        account_id: int,
        *,
        body: Iterable[locate_create_locate_request_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateCreateLocateRequestResponse:
        """
        Submits a new short stock locate request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            body=await async_maybe_transform(body, Iterable[locate_create_locate_request_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateCreateLocateRequestResponse,
        )

    async def get_locate_requests(
        self,
        account_id: int,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        reference_id: str | Omit = omit,
        status: LocateOrderStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRequestsResponse:
        """
        Retrieves all locate requests for the specified account.

        Args:
          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          reference_id: Filter by client reference ID

          status: Filter by locate order status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "reference_id": reference_id,
                        "status": status,
                    },
                    locate_get_locate_requests_params.LocateGetLocateRequestsParams,
                ),
            ),
            cast_to=LocateGetLocateRequestsResponse,
        )

    async def update_locate_request(
        self,
        account_id: int,
        *,
        accept: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateUpdateLocateRequestResponse:
        """
        Modifies an existing locate request.

        Args:
          accept: Whether to accept (`true`) or decline (`false`) the locate offer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/active/v1/accounts/{account_id}/locates", account_id=account_id),
            body=await async_maybe_transform(
                {"accept": accept}, locate_update_locate_request_params.LocateUpdateLocateRequestParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateUpdateLocateRequestResponse,
        )


class LocatesResourceWithRawResponse:
    def __init__(self, locates: LocatesResource) -> None:
        self._locates = locates

        self.create_locate_request = to_raw_response_wrapper(
            locates.create_locate_request,
        )
        self.get_locate_requests = to_raw_response_wrapper(
            locates.get_locate_requests,
        )
        self.update_locate_request = to_raw_response_wrapper(
            locates.update_locate_request,
        )

    @cached_property
    def inventory(self) -> InventoryResourceWithRawResponse:
        """Manage locate requests for short selling."""
        return InventoryResourceWithRawResponse(self._locates.inventory)


class AsyncLocatesResourceWithRawResponse:
    def __init__(self, locates: AsyncLocatesResource) -> None:
        self._locates = locates

        self.create_locate_request = async_to_raw_response_wrapper(
            locates.create_locate_request,
        )
        self.get_locate_requests = async_to_raw_response_wrapper(
            locates.get_locate_requests,
        )
        self.update_locate_request = async_to_raw_response_wrapper(
            locates.update_locate_request,
        )

    @cached_property
    def inventory(self) -> AsyncInventoryResourceWithRawResponse:
        """Manage locate requests for short selling."""
        return AsyncInventoryResourceWithRawResponse(self._locates.inventory)


class LocatesResourceWithStreamingResponse:
    def __init__(self, locates: LocatesResource) -> None:
        self._locates = locates

        self.create_locate_request = to_streamed_response_wrapper(
            locates.create_locate_request,
        )
        self.get_locate_requests = to_streamed_response_wrapper(
            locates.get_locate_requests,
        )
        self.update_locate_request = to_streamed_response_wrapper(
            locates.update_locate_request,
        )

    @cached_property
    def inventory(self) -> InventoryResourceWithStreamingResponse:
        """Manage locate requests for short selling."""
        return InventoryResourceWithStreamingResponse(self._locates.inventory)


class AsyncLocatesResourceWithStreamingResponse:
    def __init__(self, locates: AsyncLocatesResource) -> None:
        self._locates = locates

        self.create_locate_request = async_to_streamed_response_wrapper(
            locates.create_locate_request,
        )
        self.get_locate_requests = async_to_streamed_response_wrapper(
            locates.get_locate_requests,
        )
        self.update_locate_request = async_to_streamed_response_wrapper(
            locates.update_locate_request,
        )

    @cached_property
    def inventory(self) -> AsyncInventoryResourceWithStreamingResponse:
        """Manage locate requests for short selling."""
        return AsyncInventoryResourceWithStreamingResponse(self._locates.inventory)
