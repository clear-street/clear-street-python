# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Rules"]


class Rules(BaseModel):
    """
    Request-side semantics: how to turn the catalog data into a valid
    `POST /screener` call.
    """

    api_name_composition: str
    """
    Requests and response `field` objects use the same reference shape: base name
    plus at most one of `period` / `lookback`; `default_response_fields` (the POST
    default column set when `columns` is omitted) carries api_names, each decoding
    via `suffixes`.
    """

    axes: str
    """
    At most one of `period` / `lookback`; the empty combination selects the field's
    current or most recent value.
    """

    defaults: str
    """
    Omitting both is always valid; it resolves to the field's current or most recent
    value when the kind offers it, otherwise to `default_combination`.
    """

    modifiers: str
    """Where `modifier` is legal, its `args` forms, and unit semantics."""

    operators: str
    """Filter operator value counts for the `right` array."""

    variables: str
    """Built-in variables and field references in `right[].variable`."""
