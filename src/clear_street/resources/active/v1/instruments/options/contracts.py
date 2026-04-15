# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.active import SecurityIDSource
from ......types.active.v1 import ContractType
from ......types.active.v1.contract_type import ContractType
from ......types.active.security_id_source import SecurityIDSource
from ......types.active.v1.instruments.options import contract_get_option_contracts_params
from ......types.active.v1.instruments.options.contract_get_option_contracts_response import (
    ContractGetOptionContractsResponse,
)

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def get_option_contracts(
        self,
        *,
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlier_instrument_id: str | Omit = omit,
        underlier_security_id: str | Omit = omit,
        underlier_security_id_source: SecurityIDSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetOptionContractsResponse:
        """
        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlier_instrument_id: OEMS instrument UUID of the underlying equity/index

          underlier_security_id: Security identifier of the underlying (e.g., CUSIP, ISIN). Must be paired with
              underlier_security_id_source.

          underlier_security_id_source: Security ID source for the underlier (e.g., CMS, CUSIP). Must be paired with
              underlier_security_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/instruments/options/contracts",
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
                        "underlier_instrument_id": underlier_instrument_id,
                        "underlier_security_id": underlier_security_id,
                        "underlier_security_id_source": underlier_security_id_source,
                    },
                    contract_get_option_contracts_params.ContractGetOptionContractsParams,
                ),
            ),
            cast_to=ContractGetOptionContractsResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def get_option_contracts(
        self,
        *,
        contract_type: ContractType | Omit = omit,
        expiry: Union[str, date] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        underlier: str | Omit = omit,
        underlier_instrument_id: str | Omit = omit,
        underlier_security_id: str | Omit = omit,
        underlier_security_id_source: SecurityIDSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetOptionContractsResponse:
        """
        Returns options contracts for a given underlier with options-specific metadata.
        Exactly one underlier identifier must be provided.

        Args:
          contract_type: Filter by contract type: CALL or PUT

          expiry: Filter to contracts expiring on this date (YYYY-MM-DD)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          underlier: Underlier symbol (e.g., AAPL, SPX)

          underlier_instrument_id: OEMS instrument UUID of the underlying equity/index

          underlier_security_id: Security identifier of the underlying (e.g., CUSIP, ISIN). Must be paired with
              underlier_security_id_source.

          underlier_security_id_source: Security ID source for the underlier (e.g., CMS, CUSIP). Must be paired with
              underlier_security_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/instruments/options/contracts",
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
                        "underlier_instrument_id": underlier_instrument_id,
                        "underlier_security_id": underlier_security_id,
                        "underlier_security_id_source": underlier_security_id_source,
                    },
                    contract_get_option_contracts_params.ContractGetOptionContractsParams,
                ),
            ),
            cast_to=ContractGetOptionContractsResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.get_option_contracts = to_raw_response_wrapper(
            contracts.get_option_contracts,
        )


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.get_option_contracts = async_to_raw_response_wrapper(
            contracts.get_option_contracts,
        )


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.get_option_contracts = to_streamed_response_wrapper(
            contracts.get_option_contracts,
        )


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.get_option_contracts = async_to_streamed_response_wrapper(
            contracts.get_option_contracts,
        )
