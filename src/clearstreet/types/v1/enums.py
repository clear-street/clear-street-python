# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["Enums"]


class Enums(BaseModel):
    """The enum universes every other section's values are drawn from."""

    builtin_variable: List[str]
    """The built-in variable names, e.g. `"today"`, `"start_of_year"`."""

    category: List[str]
    """`FieldCategory` variants, e.g. `"PROFILE"`, `"VALUATION"`."""

    date_unit: List[str]
    """The modifier date units, e.g. `"DAY"`, `"YEAR"`."""

    format: List[str]
    """`FieldFormat` variants, e.g. `"CURRENCY"`, `"PERCENT"`."""

    lookback: List[str]
    """`FieldLookback` variants, e.g. `"ONE_WEEK"`, `"YEAR_TO_DATE"`."""

    modifier_op: List[str]
    """The modifier operation names, `"ADD"` and `"SUBTRACT"`."""

    operator: List[str]
    """`FilterOperator` variants, e.g. `"BETWEEN"`, `"ONE_OF"`."""

    operator_arg: List[str]
    """The modifier arg forms, e.g. `"LEFT_INCLUSIVE"`."""

    period: List[str]
    """`FieldPeriod` variants, e.g. `"QUARTER"`, `"ANNUAL"`."""

    value_type: List[str]
    """`FieldValueType` variants, e.g. `"DECIMAL"`, `"DATE"`."""
