# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["APIError"]


class APIError(BaseModel):
    """A direct mapping of tonic::Status, for use in HTTP responses."""

    code: int
    """The error code is used to identify the nature of the error.

    It corresponds to an HTTP status code.
    """

    message: str
    """A human-readable message providing more details about the error."""

    details: Optional[List[Dict[str, object]]] = None
    """Additional error details, if any.

    This can include structured information such as field violations or error
    metadata.
    """
