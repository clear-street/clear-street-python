# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ....._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active import SecurityIDSource
from .....types.active.v1.accounts import (
    position_get_positions_params,
    position_close_position_params,
    position_close_positions_params,
)
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.accounts.position_get_positions_response import PositionGetPositionsResponse
from .....types.active.v1.accounts.position_close_position_response import PositionClosePositionResponse
from .....types.active.v1.accounts.position_close_positions_response import PositionClosePositionsResponse

__all__ = ["PositionsResource", "AsyncPositionsResource"]


class PositionsResource(SyncAPIResource):
    """View account positions."""

    @cached_property
    def with_raw_response(self) -> PositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return PositionsResourceWithStreamingResponse(self)

    def close_position(
        self,
        security_id: str,
        *,
        account_id: int,
        security_id_source: SecurityIDSource,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          security_id_source: Security identifier source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return self._delete(
            path_template(
                "/active/v1/accounts/{account_id}/positions/{security_id_source}/{security_id}",
                account_id=account_id,
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            body=maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_position_params.PositionClosePositionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionResponse,
        )

    def close_positions(
        self,
        account_id: int,
        *,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionsResponse:
        """
        Closes all positions for the specified trading account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/active/v1/accounts/{account_id}/positions", account_id=account_id),
            body=maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_positions_params.PositionClosePositionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionsResponse,
        )

    def get_positions(
        self,
        account_id: int,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        sort_by: Literal[
            "SYMBOL",
            "INSTRUMENT_TYPE",
            "QUANTITY",
            "MARKET_VALUE",
            "POSITION_TYPE",
            "UNREALIZED_PNL",
            "DAILY_UNREALIZED_PNL",
        ]
        | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionsResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          sort_by: Field to sort by

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/active/v1/accounts/{account_id}/positions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    position_get_positions_params.PositionGetPositionsParams,
                ),
            ),
            cast_to=PositionGetPositionsResponse,
        )


class AsyncPositionsResource(AsyncAPIResource):
    """View account positions."""

    @cached_property
    def with_raw_response(self) -> AsyncPositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncPositionsResourceWithStreamingResponse(self)

    async def close_position(
        self,
        security_id: str,
        *,
        account_id: int,
        security_id_source: SecurityIDSource,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          security_id_source: Security identifier source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return await self._delete(
            path_template(
                "/active/v1/accounts/{account_id}/positions/{security_id_source}/{security_id}",
                account_id=account_id,
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            body=await async_maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_position_params.PositionClosePositionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionResponse,
        )

    async def close_positions(
        self,
        account_id: int,
        *,
        cancel_orders: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionClosePositionsResponse:
        """
        Closes all positions for the specified trading account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/active/v1/accounts/{account_id}/positions", account_id=account_id),
            body=await async_maybe_transform(
                {"cancel_orders": cancel_orders}, position_close_positions_params.PositionClosePositionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PositionClosePositionsResponse,
        )

    async def get_positions(
        self,
        account_id: int,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        sort_by: Literal[
            "SYMBOL",
            "INSTRUMENT_TYPE",
            "QUANTITY",
            "MARKET_VALUE",
            "POSITION_TYPE",
            "UNREALIZED_PNL",
            "DAILY_UNREALIZED_PNL",
        ]
        | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionGetPositionsResponse:
        """
        Retrieves all positions for the specified trading account.

        Args:
          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          sort_by: Field to sort by

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/active/v1/accounts/{account_id}/positions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    position_get_positions_params.PositionGetPositionsParams,
                ),
            ),
            cast_to=PositionGetPositionsResponse,
        )


class PositionsResourceWithRawResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.close_position = to_raw_response_wrapper(
            positions.close_position,
        )
        self.close_positions = to_raw_response_wrapper(
            positions.close_positions,
        )
        self.get_positions = to_raw_response_wrapper(
            positions.get_positions,
        )


class AsyncPositionsResourceWithRawResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.close_position = async_to_raw_response_wrapper(
            positions.close_position,
        )
        self.close_positions = async_to_raw_response_wrapper(
            positions.close_positions,
        )
        self.get_positions = async_to_raw_response_wrapper(
            positions.get_positions,
        )


class PositionsResourceWithStreamingResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.close_position = to_streamed_response_wrapper(
            positions.close_position,
        )
        self.close_positions = to_streamed_response_wrapper(
            positions.close_positions,
        )
        self.get_positions = to_streamed_response_wrapper(
            positions.get_positions,
        )


class AsyncPositionsResourceWithStreamingResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.close_position = async_to_streamed_response_wrapper(
            positions.close_position,
        )
        self.close_positions = async_to_streamed_response_wrapper(
            positions.close_positions,
        )
        self.get_positions = async_to_streamed_response_wrapper(
            positions.get_positions,
        )
