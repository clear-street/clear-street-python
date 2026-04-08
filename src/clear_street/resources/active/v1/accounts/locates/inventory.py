# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
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
from ......types.active.v1.accounts.locates import inventory_get_locate_inventory_params
from ......types.active.v1.accounts.locates.inventory_get_locate_inventory_response import (
    InventoryGetLocateInventoryResponse,
)

__all__ = ["InventoryResource", "AsyncInventoryResource"]


class InventoryResource(SyncAPIResource):
    """Manage locate requests for short selling."""

    @cached_property
    def with_raw_response(self) -> InventoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return InventoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return InventoryResourceWithStreamingResponse(self)

    def get_locate_inventory(
        self,
        account_id: int,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryGetLocateInventoryResponse:
        """
        Retrieves available inventory for short stock locates.

        Args:
          symbol: The instrument symbol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/active/v1/accounts/{account_id}/locates/inventory", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"symbol": symbol}, inventory_get_locate_inventory_params.InventoryGetLocateInventoryParams
                ),
            ),
            cast_to=InventoryGetLocateInventoryResponse,
        )


class AsyncInventoryResource(AsyncAPIResource):
    """Manage locate requests for short selling."""

    @cached_property
    def with_raw_response(self) -> AsyncInventoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncInventoryResourceWithStreamingResponse(self)

    async def get_locate_inventory(
        self,
        account_id: int,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryGetLocateInventoryResponse:
        """
        Retrieves available inventory for short stock locates.

        Args:
          symbol: The instrument symbol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/active/v1/accounts/{account_id}/locates/inventory", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"symbol": symbol}, inventory_get_locate_inventory_params.InventoryGetLocateInventoryParams
                ),
            ),
            cast_to=InventoryGetLocateInventoryResponse,
        )


class InventoryResourceWithRawResponse:
    def __init__(self, inventory: InventoryResource) -> None:
        self._inventory = inventory

        self.get_locate_inventory = to_raw_response_wrapper(
            inventory.get_locate_inventory,
        )


class AsyncInventoryResourceWithRawResponse:
    def __init__(self, inventory: AsyncInventoryResource) -> None:
        self._inventory = inventory

        self.get_locate_inventory = async_to_raw_response_wrapper(
            inventory.get_locate_inventory,
        )


class InventoryResourceWithStreamingResponse:
    def __init__(self, inventory: InventoryResource) -> None:
        self._inventory = inventory

        self.get_locate_inventory = to_streamed_response_wrapper(
            inventory.get_locate_inventory,
        )


class AsyncInventoryResourceWithStreamingResponse:
    def __init__(self, inventory: AsyncInventoryResource) -> None:
        self._inventory = inventory

        self.get_locate_inventory = async_to_streamed_response_wrapper(
            inventory.get_locate_inventory,
        )
