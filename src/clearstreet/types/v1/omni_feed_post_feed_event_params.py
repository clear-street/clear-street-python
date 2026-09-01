# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OmniFeedPostFeedEventParams", "Event"]


class OmniFeedPostFeedEventParams(TypedDict, total=False):
    event: Required[Event]
    """The event to record."""


class Event(TypedDict, total=False):
    """The event to record."""

    item_id: Required[str]
    """The feed item the event concerns."""

    type: Required[Literal["seen", "click", "upvote", "downvote"]]
    """What happened."""
