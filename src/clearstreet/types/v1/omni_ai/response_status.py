# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResponseStatus"]

ResponseStatus: TypeAlias = Literal["queued", "running", "succeeded", "failed", "canceled"]
