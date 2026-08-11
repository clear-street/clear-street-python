# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, Base64FileInput, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import Schedule, TriggerMode, alert_get_alerts_params, alert_create_alert_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.schedule import Schedule
from ...types.v1.trigger_mode import TriggerMode
from ...types.v1.alert_get_alerts_response import AlertGetAlertsResponse
from ...types.v1.alert_create_alert_response import AlertCreateAlertResponse
from ...types.v1.alert_get_alert_by_id_response import AlertGetAlertByIDResponse

__all__ = ["AlertsResource", "AsyncAlertsResource"]


class AlertsResource(SyncAPIResource):
    """
    Create and manage alerts that watch market and portfolio conditions on an account and notify when they trigger.
    """

    @cached_property
    def with_raw_response(self) -> AlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AlertsResourceWithStreamingResponse(self)

    def create_alert(
        self,
        *,
        condition: object,
        schedule: Schedule,
        trigger: TriggerMode,
        account_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertCreateAlertResponse:
        """
        Create an alert that watches a market or portfolio condition on the account and
        notifies when it triggers.

        The alert starts evaluating immediately. A `once` alert triggers a single time
        and then completes. Instrument references in the condition accept a ticker
        symbol or an OEMS instrument id; they are stored and returned as instrument ids.

        `account_id` is optional: an alert without one may only watch market conditions,
        so a condition that reads account data (an `account.*` signal or a holdings
        scope) is rejected without it.

        Args:
          condition: The boolean condition tree, in the condition grammar. `"instrument_id"`
              references accept a ticker or an OEMS instrument id.

          schedule: How often an alert's condition is evaluated.

          trigger: How an alert triggers. `once` alerts complete after their first trigger.

          account_id: The account whose `account.*` signals and holdings scopes the condition reads.
              Optional: a market-only alert needs no account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alerts",
            body=maybe_transform(
                {
                    "condition": condition,
                    "schedule": schedule,
                    "trigger": trigger,
                    "account_id": account_id,
                },
                alert_create_alert_params.AlertCreateAlertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertCreateAlertResponse,
        )

    def delete_alert(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an alert.

        It stops evaluating and disappears from this API; its trigger
        history is retained server-side.

        Only `active` and `paused` alerts can be deleted; `completed` and `expired`
        alerts are immutable history. Repeating a delete reports 404, matching what GET
        shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/alerts/{alert_id}", alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_alert_by_id(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertGetAlertByIDResponse:
        """
        Get one alert by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return self._get(
            path_template("/v1/alerts/{alert_id}", alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertGetAlertByIDResponse,
        )

    def get_alerts(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertGetAlertsResponse:
        """
        List the caller's alerts, newest first.

        `status` narrows the result to a comma-separated set of statuses; when absent,
        alerts of every status are returned. Deleted alerts are never returned.

        Args:
          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          status: Comma-separated status filter (`active`, `paused`, `completed`, `expired`).
              Unknown values are rejected. Absent = every status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                    },
                    alert_get_alerts_params.AlertGetAlertsParams,
                ),
            ),
            cast_to=AlertGetAlertsResponse,
        )


class AsyncAlertsResource(AsyncAPIResource):
    """
    Create and manage alerts that watch market and portfolio conditions on an account and notify when they trigger.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncAlertsResourceWithStreamingResponse(self)

    async def create_alert(
        self,
        *,
        condition: object,
        schedule: Schedule,
        trigger: TriggerMode,
        account_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertCreateAlertResponse:
        """
        Create an alert that watches a market or portfolio condition on the account and
        notifies when it triggers.

        The alert starts evaluating immediately. A `once` alert triggers a single time
        and then completes. Instrument references in the condition accept a ticker
        symbol or an OEMS instrument id; they are stored and returned as instrument ids.

        `account_id` is optional: an alert without one may only watch market conditions,
        so a condition that reads account data (an `account.*` signal or a holdings
        scope) is rejected without it.

        Args:
          condition: The boolean condition tree, in the condition grammar. `"instrument_id"`
              references accept a ticker or an OEMS instrument id.

          schedule: How often an alert's condition is evaluated.

          trigger: How an alert triggers. `once` alerts complete after their first trigger.

          account_id: The account whose `account.*` signals and holdings scopes the condition reads.
              Optional: a market-only alert needs no account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alerts",
            body=await async_maybe_transform(
                {
                    "condition": condition,
                    "schedule": schedule,
                    "trigger": trigger,
                    "account_id": account_id,
                },
                alert_create_alert_params.AlertCreateAlertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertCreateAlertResponse,
        )

    async def delete_alert(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an alert.

        It stops evaluating and disappears from this API; its trigger
        history is retained server-side.

        Only `active` and `paused` alerts can be deleted; `completed` and `expired`
        alerts are immutable history. Repeating a delete reports 404, matching what GET
        shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/alerts/{alert_id}", alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_alert_by_id(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertGetAlertByIDResponse:
        """
        Get one alert by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return await self._get(
            path_template("/v1/alerts/{alert_id}", alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertGetAlertByIDResponse,
        )

    async def get_alerts(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertGetAlertsResponse:
        """
        List the caller's alerts, newest first.

        `status` narrows the result to a comma-separated set of statuses; when absent,
        alerts of every status are returned. Deleted alerts are never returned.

        Args:
          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          status: Comma-separated status filter (`active`, `paused`, `completed`, `expired`).
              Unknown values are rejected. Absent = every status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                    },
                    alert_get_alerts_params.AlertGetAlertsParams,
                ),
            ),
            cast_to=AlertGetAlertsResponse,
        )


class AlertsResourceWithRawResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.create_alert = to_raw_response_wrapper(
            alerts.create_alert,
        )
        self.delete_alert = to_raw_response_wrapper(
            alerts.delete_alert,
        )
        self.get_alert_by_id = to_raw_response_wrapper(
            alerts.get_alert_by_id,
        )
        self.get_alerts = to_raw_response_wrapper(
            alerts.get_alerts,
        )


class AsyncAlertsResourceWithRawResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.create_alert = async_to_raw_response_wrapper(
            alerts.create_alert,
        )
        self.delete_alert = async_to_raw_response_wrapper(
            alerts.delete_alert,
        )
        self.get_alert_by_id = async_to_raw_response_wrapper(
            alerts.get_alert_by_id,
        )
        self.get_alerts = async_to_raw_response_wrapper(
            alerts.get_alerts,
        )


class AlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.create_alert = to_streamed_response_wrapper(
            alerts.create_alert,
        )
        self.delete_alert = to_streamed_response_wrapper(
            alerts.delete_alert,
        )
        self.get_alert_by_id = to_streamed_response_wrapper(
            alerts.get_alert_by_id,
        )
        self.get_alerts = to_streamed_response_wrapper(
            alerts.get_alerts,
        )


class AsyncAlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.create_alert = async_to_streamed_response_wrapper(
            alerts.create_alert,
        )
        self.delete_alert = async_to_streamed_response_wrapper(
            alerts.delete_alert,
        )
        self.get_alert_by_id = async_to_streamed_response_wrapper(
            alerts.get_alert_by_id,
        )
        self.get_alerts = async_to_streamed_response_wrapper(
            alerts.get_alerts,
        )
