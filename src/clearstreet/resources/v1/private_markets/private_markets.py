# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from .offerings import (
    OfferingsResource,
    AsyncOfferingsResource,
    OfferingsResourceWithRawResponse,
    AsyncOfferingsResourceWithRawResponse,
    OfferingsResourceWithStreamingResponse,
    AsyncOfferingsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.v1 import (
    private_market_get_iois_params,
    private_market_create_ioi_params,
    private_market_delete_ioi_params,
    private_market_update_ioi_params,
    private_market_get_spv_by_id_params,
    private_market_get_company_by_id_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.private_market_get_iois_response import PrivateMarketGetIoisResponse
from ....types.v1.private_market_create_ioi_response import PrivateMarketCreateIoiResponse
from ....types.v1.private_market_update_ioi_response import PrivateMarketUpdateIoiResponse
from ....types.v1.private_market_get_spv_by_id_response import PrivateMarketGetSpvByIDResponse
from ....types.v1.private_market_get_company_by_id_response import PrivateMarketGetCompanyByIDResponse

__all__ = ["PrivateMarketsResource", "AsyncPrivateMarketsResource"]


class PrivateMarketsResource(SyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def offerings(self) -> OfferingsResource:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrivateMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return PrivateMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return PrivateMarketsResourceWithStreamingResponse(self)

    def create_ioi(
        self,
        *,
        account_id: int,
        notional_amount: str,
        offering_id: str,
        nda_acceptance: Optional[private_market_create_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketCreateIoiResponse:
        """
        Create an IOI for a visible upcoming offering.

        Args:
          nda_acceptance: Required only when the offering's attached SPV has an NDA agreement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/private-markets/iois",
            body=maybe_transform(
                {
                    "notional_amount": notional_amount,
                    "offering_id": offering_id,
                    "nda_acceptance": nda_acceptance,
                },
                private_market_create_ioi_params.PrivateMarketCreateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, private_market_create_ioi_params.PrivateMarketCreateIoiParams
                ),
            ),
            cast_to=PrivateMarketCreateIoiResponse,
        )

    def delete_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Withdraw a live IOI.

        Repeating a withdrawal returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ioi_id:
            raise ValueError(f"Expected a non-empty value for `ioi_id` but received {ioi_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/private-markets/iois/{ioi_id}", ioi_id=ioi_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, private_market_delete_ioi_params.PrivateMarketDeleteIoiParams
                ),
            ),
            cast_to=NoneType,
        )

    def get_company_by_id(
        self,
        company_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetCompanyByIDResponse:
        """
        Fetch one published private-market company with its complete versioned profile.
        Requires the account holder to have attested. Returns `404` when the company
        does not exist or is not yet published.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            path_template("/v1/private-markets/companies/{company_id}", company_id=company_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id},
                    private_market_get_company_by_id_params.PrivateMarketGetCompanyByIDParams,
                ),
            ),
            cast_to=PrivateMarketGetCompanyByIDResponse,
        )

    def get_iois(
        self,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetIoisResponse:
        """
        List every live IOI for the caller's account-holder entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/private-markets/iois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, private_market_get_iois_params.PrivateMarketGetIoisParams
                ),
            ),
            cast_to=PrivateMarketGetIoisResponse,
        )

    def get_spv_by_id(
        self,
        spv_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetSpvByIDResponse:
        """Fetch one private-market SPV's complete economics and fee schedule.

        Requires the
        account holder to have attested. Returns `404` unless the SPV is `OPEN` and
        attached to a currently visible `ACTIVE` offering.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spv_id:
            raise ValueError(f"Expected a non-empty value for `spv_id` but received {spv_id!r}")
        return self._get(
            path_template("/v1/private-markets/spvs/{spv_id}", spv_id=spv_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, private_market_get_spv_by_id_params.PrivateMarketGetSpvByIDParams
                ),
            ),
            cast_to=PrivateMarketGetSpvByIDResponse,
        )

    def update_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        notional_amount: str,
        nda_acceptance: Optional[private_market_update_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketUpdateIoiResponse:
        """
        Update an IOI's notional, accepting the current NDA revision when required.

        Args:
          nda_acceptance: Required when the SPV's current NDA version is newer than the IOI's latest
              acceptance. Irrelevant acceptances are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ioi_id:
            raise ValueError(f"Expected a non-empty value for `ioi_id` but received {ioi_id!r}")
        return self._patch(
            path_template("/v1/private-markets/iois/{ioi_id}", ioi_id=ioi_id),
            body=maybe_transform(
                {
                    "notional_amount": notional_amount,
                    "nda_acceptance": nda_acceptance,
                },
                private_market_update_ioi_params.PrivateMarketUpdateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, private_market_update_ioi_params.PrivateMarketUpdateIoiParams
                ),
            ),
            cast_to=PrivateMarketUpdateIoiResponse,
        )


class AsyncPrivateMarketsResource(AsyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def offerings(self) -> AsyncOfferingsResource:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrivateMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncPrivateMarketsResourceWithStreamingResponse(self)

    async def create_ioi(
        self,
        *,
        account_id: int,
        notional_amount: str,
        offering_id: str,
        nda_acceptance: Optional[private_market_create_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketCreateIoiResponse:
        """
        Create an IOI for a visible upcoming offering.

        Args:
          nda_acceptance: Required only when the offering's attached SPV has an NDA agreement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/private-markets/iois",
            body=await async_maybe_transform(
                {
                    "notional_amount": notional_amount,
                    "offering_id": offering_id,
                    "nda_acceptance": nda_acceptance,
                },
                private_market_create_ioi_params.PrivateMarketCreateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, private_market_create_ioi_params.PrivateMarketCreateIoiParams
                ),
            ),
            cast_to=PrivateMarketCreateIoiResponse,
        )

    async def delete_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Withdraw a live IOI.

        Repeating a withdrawal returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ioi_id:
            raise ValueError(f"Expected a non-empty value for `ioi_id` but received {ioi_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/private-markets/iois/{ioi_id}", ioi_id=ioi_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, private_market_delete_ioi_params.PrivateMarketDeleteIoiParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_company_by_id(
        self,
        company_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetCompanyByIDResponse:
        """
        Fetch one published private-market company with its complete versioned profile.
        Requires the account holder to have attested. Returns `404` when the company
        does not exist or is not yet published.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            path_template("/v1/private-markets/companies/{company_id}", company_id=company_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id},
                    private_market_get_company_by_id_params.PrivateMarketGetCompanyByIDParams,
                ),
            ),
            cast_to=PrivateMarketGetCompanyByIDResponse,
        )

    async def get_iois(
        self,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetIoisResponse:
        """
        List every live IOI for the caller's account-holder entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/private-markets/iois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, private_market_get_iois_params.PrivateMarketGetIoisParams
                ),
            ),
            cast_to=PrivateMarketGetIoisResponse,
        )

    async def get_spv_by_id(
        self,
        spv_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketGetSpvByIDResponse:
        """Fetch one private-market SPV's complete economics and fee schedule.

        Requires the
        account holder to have attested. Returns `404` unless the SPV is `OPEN` and
        attached to a currently visible `ACTIVE` offering.

        Args:
          account_id: Account whose account-holder entity must hold an accreditation attestation to
              browse private-market offerings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spv_id:
            raise ValueError(f"Expected a non-empty value for `spv_id` but received {spv_id!r}")
        return await self._get(
            path_template("/v1/private-markets/spvs/{spv_id}", spv_id=spv_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, private_market_get_spv_by_id_params.PrivateMarketGetSpvByIDParams
                ),
            ),
            cast_to=PrivateMarketGetSpvByIDResponse,
        )

    async def update_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        notional_amount: str,
        nda_acceptance: Optional[private_market_update_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateMarketUpdateIoiResponse:
        """
        Update an IOI's notional, accepting the current NDA revision when required.

        Args:
          nda_acceptance: Required when the SPV's current NDA version is newer than the IOI's latest
              acceptance. Irrelevant acceptances are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ioi_id:
            raise ValueError(f"Expected a non-empty value for `ioi_id` but received {ioi_id!r}")
        return await self._patch(
            path_template("/v1/private-markets/iois/{ioi_id}", ioi_id=ioi_id),
            body=await async_maybe_transform(
                {
                    "notional_amount": notional_amount,
                    "nda_acceptance": nda_acceptance,
                },
                private_market_update_ioi_params.PrivateMarketUpdateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, private_market_update_ioi_params.PrivateMarketUpdateIoiParams
                ),
            ),
            cast_to=PrivateMarketUpdateIoiResponse,
        )


class PrivateMarketsResourceWithRawResponse:
    def __init__(self, private_markets: PrivateMarketsResource) -> None:
        self._private_markets = private_markets

        self.create_ioi = to_raw_response_wrapper(
            private_markets.create_ioi,
        )
        self.delete_ioi = to_raw_response_wrapper(
            private_markets.delete_ioi,
        )
        self.get_company_by_id = to_raw_response_wrapper(
            private_markets.get_company_by_id,
        )
        self.get_iois = to_raw_response_wrapper(
            private_markets.get_iois,
        )
        self.get_spv_by_id = to_raw_response_wrapper(
            private_markets.get_spv_by_id,
        )
        self.update_ioi = to_raw_response_wrapper(
            private_markets.update_ioi,
        )

    @cached_property
    def offerings(self) -> OfferingsResourceWithRawResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResourceWithRawResponse(self._private_markets.offerings)


class AsyncPrivateMarketsResourceWithRawResponse:
    def __init__(self, private_markets: AsyncPrivateMarketsResource) -> None:
        self._private_markets = private_markets

        self.create_ioi = async_to_raw_response_wrapper(
            private_markets.create_ioi,
        )
        self.delete_ioi = async_to_raw_response_wrapper(
            private_markets.delete_ioi,
        )
        self.get_company_by_id = async_to_raw_response_wrapper(
            private_markets.get_company_by_id,
        )
        self.get_iois = async_to_raw_response_wrapper(
            private_markets.get_iois,
        )
        self.get_spv_by_id = async_to_raw_response_wrapper(
            private_markets.get_spv_by_id,
        )
        self.update_ioi = async_to_raw_response_wrapper(
            private_markets.update_ioi,
        )

    @cached_property
    def offerings(self) -> AsyncOfferingsResourceWithRawResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResourceWithRawResponse(self._private_markets.offerings)


class PrivateMarketsResourceWithStreamingResponse:
    def __init__(self, private_markets: PrivateMarketsResource) -> None:
        self._private_markets = private_markets

        self.create_ioi = to_streamed_response_wrapper(
            private_markets.create_ioi,
        )
        self.delete_ioi = to_streamed_response_wrapper(
            private_markets.delete_ioi,
        )
        self.get_company_by_id = to_streamed_response_wrapper(
            private_markets.get_company_by_id,
        )
        self.get_iois = to_streamed_response_wrapper(
            private_markets.get_iois,
        )
        self.get_spv_by_id = to_streamed_response_wrapper(
            private_markets.get_spv_by_id,
        )
        self.update_ioi = to_streamed_response_wrapper(
            private_markets.update_ioi,
        )

    @cached_property
    def offerings(self) -> OfferingsResourceWithStreamingResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return OfferingsResourceWithStreamingResponse(self._private_markets.offerings)


class AsyncPrivateMarketsResourceWithStreamingResponse:
    def __init__(self, private_markets: AsyncPrivateMarketsResource) -> None:
        self._private_markets = private_markets

        self.create_ioi = async_to_streamed_response_wrapper(
            private_markets.create_ioi,
        )
        self.delete_ioi = async_to_streamed_response_wrapper(
            private_markets.delete_ioi,
        )
        self.get_company_by_id = async_to_streamed_response_wrapper(
            private_markets.get_company_by_id,
        )
        self.get_iois = async_to_streamed_response_wrapper(
            private_markets.get_iois,
        )
        self.get_spv_by_id = async_to_streamed_response_wrapper(
            private_markets.get_spv_by_id,
        )
        self.update_ioi = async_to_streamed_response_wrapper(
            private_markets.update_ioi,
        )

    @cached_property
    def offerings(self) -> AsyncOfferingsResourceWithStreamingResponse:
        """Browse private-market offerings and their indicative terms.

        Access requires the account holder to hold an accreditation attestation.
        """
        return AsyncOfferingsResourceWithStreamingResponse(self._private_markets.offerings)
