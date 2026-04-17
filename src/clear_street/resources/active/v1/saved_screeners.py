# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.active.v1 import saved_screener_create_screener_params, saved_screener_update_screener_params
from ....types.active.v1.saved_screener_filter_param import SavedScreenerFilterParam
from ....types.active.v1.saved_screener_list_screeners_response import SavedScreenerListScreenersResponse
from ....types.active.v1.saved_screener_create_screener_response import SavedScreenerCreateScreenerResponse
from ....types.active.v1.saved_screener_update_screener_response import SavedScreenerUpdateScreenerResponse
from ....types.active.v1.saved_screener_get_screener_by_id_response import SavedScreenerGetScreenerByIDResponse

__all__ = ["SavedScreenersResource", "AsyncSavedScreenersResource"]


class SavedScreenersResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> SavedScreenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return SavedScreenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SavedScreenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return SavedScreenersResourceWithStreamingResponse(self)

    def create_screener(
        self,
        *,
        field_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Iterable[SavedScreenerFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sort_direction: Optional[Literal["ASC", "DESC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerCreateScreenerResponse:
        """
        Create a saved screener configuration.

        Persists a screener configuration for the authenticated user.

        Args:
          field_filter: List of field names to include when running this screener

          filters: Filter criteria for this screener

          name: The name for this screener configuration

          sort_by: Field name to sort results by

          sort_direction: Sort direction for results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/saved-screeners",
            body=maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sort_by": sort_by,
                    "sort_direction": sort_direction,
                },
                saved_screener_create_screener_params.SavedScreenerCreateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerCreateScreenerResponse,
        )

    def delete_screener(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved screener configuration.

        Deletes the screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_screener_by_id(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerGetScreenerByIDResponse:
        """
        Get a saved screener configuration by ID.

        Returns a single screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return self._get(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerGetScreenerByIDResponse,
        )

    def list_screeners(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerListScreenersResponse:
        """
        List saved screener configurations.

        Returns all screener configurations for the authenticated user.
        """
        return self._get(
            "/active/v1/saved-screeners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerListScreenersResponse,
        )

    def update_screener(
        self,
        screener_id: str,
        *,
        field_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Iterable[SavedScreenerFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sort_direction: Optional[Literal["ASC", "DESC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerUpdateScreenerResponse:
        """
        Update a saved screener configuration.

        Replaces the screener configuration for the authenticated user. If `name` is
        null, the existing name is preserved.

        Args:
          field_filter: List of field names to include when running this screener

          filters: Filter criteria for this screener

          name: The name for this screener configuration

          sort_by: Field name to sort results by

          sort_direction: Sort direction for results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return self._put(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            body=maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sort_by": sort_by,
                    "sort_direction": sort_direction,
                },
                saved_screener_update_screener_params.SavedScreenerUpdateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerUpdateScreenerResponse,
        )


class AsyncSavedScreenersResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncSavedScreenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSavedScreenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSavedScreenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncSavedScreenersResourceWithStreamingResponse(self)

    async def create_screener(
        self,
        *,
        field_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Iterable[SavedScreenerFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sort_direction: Optional[Literal["ASC", "DESC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerCreateScreenerResponse:
        """
        Create a saved screener configuration.

        Persists a screener configuration for the authenticated user.

        Args:
          field_filter: List of field names to include when running this screener

          filters: Filter criteria for this screener

          name: The name for this screener configuration

          sort_by: Field name to sort results by

          sort_direction: Sort direction for results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/saved-screeners",
            body=await async_maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sort_by": sort_by,
                    "sort_direction": sort_direction,
                },
                saved_screener_create_screener_params.SavedScreenerCreateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerCreateScreenerResponse,
        )

    async def delete_screener(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved screener configuration.

        Deletes the screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_screener_by_id(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerGetScreenerByIDResponse:
        """
        Get a saved screener configuration by ID.

        Returns a single screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return await self._get(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerGetScreenerByIDResponse,
        )

    async def list_screeners(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerListScreenersResponse:
        """
        List saved screener configurations.

        Returns all screener configurations for the authenticated user.
        """
        return await self._get(
            "/active/v1/saved-screeners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerListScreenersResponse,
        )

    async def update_screener(
        self,
        screener_id: str,
        *,
        field_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Iterable[SavedScreenerFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sort_direction: Optional[Literal["ASC", "DESC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedScreenerUpdateScreenerResponse:
        """
        Update a saved screener configuration.

        Replaces the screener configuration for the authenticated user. If `name` is
        null, the existing name is preserved.

        Args:
          field_filter: List of field names to include when running this screener

          filters: Filter criteria for this screener

          name: The name for this screener configuration

          sort_by: Field name to sort results by

          sort_direction: Sort direction for results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return await self._put(
            path_template("/active/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            body=await async_maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sort_by": sort_by,
                    "sort_direction": sort_direction,
                },
                saved_screener_update_screener_params.SavedScreenerUpdateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedScreenerUpdateScreenerResponse,
        )


class SavedScreenersResourceWithRawResponse:
    def __init__(self, saved_screeners: SavedScreenersResource) -> None:
        self._saved_screeners = saved_screeners

        self.create_screener = to_raw_response_wrapper(
            saved_screeners.create_screener,
        )
        self.delete_screener = to_raw_response_wrapper(
            saved_screeners.delete_screener,
        )
        self.get_screener_by_id = to_raw_response_wrapper(
            saved_screeners.get_screener_by_id,
        )
        self.list_screeners = to_raw_response_wrapper(
            saved_screeners.list_screeners,
        )
        self.update_screener = to_raw_response_wrapper(
            saved_screeners.update_screener,
        )


class AsyncSavedScreenersResourceWithRawResponse:
    def __init__(self, saved_screeners: AsyncSavedScreenersResource) -> None:
        self._saved_screeners = saved_screeners

        self.create_screener = async_to_raw_response_wrapper(
            saved_screeners.create_screener,
        )
        self.delete_screener = async_to_raw_response_wrapper(
            saved_screeners.delete_screener,
        )
        self.get_screener_by_id = async_to_raw_response_wrapper(
            saved_screeners.get_screener_by_id,
        )
        self.list_screeners = async_to_raw_response_wrapper(
            saved_screeners.list_screeners,
        )
        self.update_screener = async_to_raw_response_wrapper(
            saved_screeners.update_screener,
        )


class SavedScreenersResourceWithStreamingResponse:
    def __init__(self, saved_screeners: SavedScreenersResource) -> None:
        self._saved_screeners = saved_screeners

        self.create_screener = to_streamed_response_wrapper(
            saved_screeners.create_screener,
        )
        self.delete_screener = to_streamed_response_wrapper(
            saved_screeners.delete_screener,
        )
        self.get_screener_by_id = to_streamed_response_wrapper(
            saved_screeners.get_screener_by_id,
        )
        self.list_screeners = to_streamed_response_wrapper(
            saved_screeners.list_screeners,
        )
        self.update_screener = to_streamed_response_wrapper(
            saved_screeners.update_screener,
        )


class AsyncSavedScreenersResourceWithStreamingResponse:
    def __init__(self, saved_screeners: AsyncSavedScreenersResource) -> None:
        self._saved_screeners = saved_screeners

        self.create_screener = async_to_streamed_response_wrapper(
            saved_screeners.create_screener,
        )
        self.delete_screener = async_to_streamed_response_wrapper(
            saved_screeners.delete_screener,
        )
        self.get_screener_by_id = async_to_streamed_response_wrapper(
            saved_screeners.get_screener_by_id,
        )
        self.list_screeners = async_to_streamed_response_wrapper(
            saved_screeners.list_screeners,
        )
        self.update_screener = async_to_streamed_response_wrapper(
            saved_screeners.update_screener,
        )
