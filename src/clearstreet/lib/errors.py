from typing import Dict, List, Optional

from .._utils import is_mapping
from .._models import BaseModel, construct_type_unchecked

__all__ = ["ErrorObject", "ErrorDetail"]


class ErrorDetail(BaseModel):
    """One entry in `ErrorObject.details`.

    Entries come in different shapes, and each one sets only some of these fields:

    - A check that failed, such as a risk check, sets `type`, `subject` and `description`.
    - Context for a failure sets `reason`, `domain` and `metadata`.
    - An instrument that wasn't found sets `instrument_id`.

    Fields that an entry doesn't set are `None`.
    """

    type: Optional[str] = None
    """The check that failed, e.g. `BUYING_POWER`."""

    subject: Optional[str] = None
    """What the check was applied to, e.g. `order:<id>`."""

    description: Optional[str] = None
    """A human-readable description of the failure."""

    reason: Optional[str] = None
    """The reason for the failure, e.g. `BUYING_POWER`."""

    domain: Optional[str] = None
    """The service that reported the failure, e.g. `com.clearstreet.oems.risk`."""

    metadata: Optional[Dict[str, str]] = None
    """Values that describe the failure, as strings, e.g. `required_total` and `available`."""

    instrument_id: Optional[str] = None
    """An instrument id that wasn't found."""


class ErrorObject(BaseModel):
    """The `error` object of an error response.

    It has the same fields as `clearstreet.types.APIError`, except that each entry in `details` is an `ErrorDetail`
    instead of a dict.
    """

    code: int
    """The error code is used to identify the nature of the error.

    It corresponds to an HTTP status code.
    """

    message: str
    """A human-readable message providing more details about the error."""

    details: Optional[List[ErrorDetail]] = None
    """Structured details about the error, if any, such as each check that failed."""


def _parse_error(body: object) -> Optional[ErrorObject]:  # pyright: ignore[reportUnusedFunction]
    """Returns `body["error"]` as an `ErrorObject`, without validating it.

    Returns `None` if it is missing or isn't an object, and never raises.
    """
    if not is_mapping(body):
        return None
    error = body.get("error")
    if not is_mapping(error):
        return None
    try:
        return construct_type_unchecked(type_=ErrorObject, value=error)
    except Exception:
        return None
