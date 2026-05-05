# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import ContractType
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.instruments import option_get_option_contracts_params
from ....types.v1.contract_type import ContractType
from ....types.v1.instruments.option_get_option_contracts_response import OptionGetOptionContractsResponse

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)

    def get_option_contracts(
        self,
        *,
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlying_instrument_id: OEMS instrument UUID or symbol of the underlying equity/index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instruments/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "page_size": page_size,
                        "page_token": page_token,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    option_get_option_contracts_params.OptionGetOptionContractsParams,
                ),
            ),
            cast_to=OptionGetOptionContractsResponse,
        )


class AsyncOptionsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)

    async def get_option_contracts(
        self,
        *,
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlying_instrument_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionGetOptionContractsResponse:
        """
        List options contracts.

        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlying_instrument_id: OEMS instrument UUID or symbol of the underlying equity/index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instruments/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contract_type": contract_type,
                        "expiry": expiry,
                        "page_size": page_size,
                        "page_token": page_token,
                        "underlier": underlier,
                        "underlying_instrument_id": underlying_instrument_id,
                    },
                    option_get_option_contracts_params.OptionGetOptionContractsParams,
                ),
            ),
            cast_to=OptionGetOptionContractsResponse,
        )


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.get_option_contracts = to_raw_response_wrapper(
            options.get_option_contracts,
        )


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.get_option_contracts = async_to_raw_response_wrapper(
            options.get_option_contracts,
        )


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.get_option_contracts = to_streamed_response_wrapper(
            options.get_option_contracts,
        )


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.get_option_contracts = async_to_streamed_response_wrapper(
            options.get_option_contracts,
        )
