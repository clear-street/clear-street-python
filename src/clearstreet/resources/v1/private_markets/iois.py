# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.v1.private_markets import (
    iois_get_iois_params,
    iois_create_ioi_params,
    iois_delete_ioi_params,
    iois_update_ioi_params,
)
from ....types.v1.private_markets.iois_get_iois_response import IoisGetIoisResponse
from ....types.v1.private_markets.iois_create_ioi_response import IoisCreateIoiResponse
from ....types.v1.private_markets.iois_update_ioi_response import IoisUpdateIoiResponse

__all__ = ["IoisResource", "AsyncIoisResource"]


class IoisResource(SyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def with_raw_response(self) -> IoisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return IoisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IoisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return IoisResourceWithStreamingResponse(self)

    def create_ioi(
        self,
        *,
        account_id: int,
        notional_amount: str,
        offering_id: str,
        nda_acceptance: Optional[iois_create_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IoisCreateIoiResponse:
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
                iois_create_ioi_params.IoisCreateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, iois_create_ioi_params.IoisCreateIoiParams),
            ),
            cast_to=IoisCreateIoiResponse,
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
                query=maybe_transform({"account_id": account_id}, iois_delete_ioi_params.IoisDeleteIoiParams),
            ),
            cast_to=NoneType,
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
    ) -> IoisGetIoisResponse:
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
                query=maybe_transform({"account_id": account_id}, iois_get_iois_params.IoisGetIoisParams),
            ),
            cast_to=IoisGetIoisResponse,
        )

    def update_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        notional_amount: str,
        nda_acceptance: Optional[iois_update_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IoisUpdateIoiResponse:
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
                iois_update_ioi_params.IoisUpdateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, iois_update_ioi_params.IoisUpdateIoiParams),
            ),
            cast_to=IoisUpdateIoiResponse,
        )


class AsyncIoisResource(AsyncAPIResource):
    """Browse private-market offerings and their indicative terms.

    Access requires the account holder to hold an accreditation attestation.
    """

    @cached_property
    def with_raw_response(self) -> AsyncIoisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIoisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIoisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncIoisResourceWithStreamingResponse(self)

    async def create_ioi(
        self,
        *,
        account_id: int,
        notional_amount: str,
        offering_id: str,
        nda_acceptance: Optional[iois_create_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IoisCreateIoiResponse:
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
                iois_create_ioi_params.IoisCreateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, iois_create_ioi_params.IoisCreateIoiParams
                ),
            ),
            cast_to=IoisCreateIoiResponse,
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
                    {"account_id": account_id}, iois_delete_ioi_params.IoisDeleteIoiParams
                ),
            ),
            cast_to=NoneType,
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
    ) -> IoisGetIoisResponse:
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
                query=await async_maybe_transform({"account_id": account_id}, iois_get_iois_params.IoisGetIoisParams),
            ),
            cast_to=IoisGetIoisResponse,
        )

    async def update_ioi(
        self,
        ioi_id: str,
        *,
        account_id: int,
        notional_amount: str,
        nda_acceptance: Optional[iois_update_ioi_params.NdaAcceptance] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IoisUpdateIoiResponse:
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
                iois_update_ioi_params.IoisUpdateIoiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, iois_update_ioi_params.IoisUpdateIoiParams
                ),
            ),
            cast_to=IoisUpdateIoiResponse,
        )


class IoisResourceWithRawResponse:
    def __init__(self, iois: IoisResource) -> None:
        self._iois = iois

        self.create_ioi = to_raw_response_wrapper(
            iois.create_ioi,
        )
        self.delete_ioi = to_raw_response_wrapper(
            iois.delete_ioi,
        )
        self.get_iois = to_raw_response_wrapper(
            iois.get_iois,
        )
        self.update_ioi = to_raw_response_wrapper(
            iois.update_ioi,
        )


class AsyncIoisResourceWithRawResponse:
    def __init__(self, iois: AsyncIoisResource) -> None:
        self._iois = iois

        self.create_ioi = async_to_raw_response_wrapper(
            iois.create_ioi,
        )
        self.delete_ioi = async_to_raw_response_wrapper(
            iois.delete_ioi,
        )
        self.get_iois = async_to_raw_response_wrapper(
            iois.get_iois,
        )
        self.update_ioi = async_to_raw_response_wrapper(
            iois.update_ioi,
        )


class IoisResourceWithStreamingResponse:
    def __init__(self, iois: IoisResource) -> None:
        self._iois = iois

        self.create_ioi = to_streamed_response_wrapper(
            iois.create_ioi,
        )
        self.delete_ioi = to_streamed_response_wrapper(
            iois.delete_ioi,
        )
        self.get_iois = to_streamed_response_wrapper(
            iois.get_iois,
        )
        self.update_ioi = to_streamed_response_wrapper(
            iois.update_ioi,
        )


class AsyncIoisResourceWithStreamingResponse:
    def __init__(self, iois: AsyncIoisResource) -> None:
        self._iois = iois

        self.create_ioi = async_to_streamed_response_wrapper(
            iois.create_ioi,
        )
        self.delete_ioi = async_to_streamed_response_wrapper(
            iois.delete_ioi,
        )
        self.get_iois = async_to_streamed_response_wrapper(
            iois.get_iois,
        )
        self.update_ioi = async_to_streamed_response_wrapper(
            iois.update_ioi,
        )
