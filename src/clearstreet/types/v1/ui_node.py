# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UiNode"]


class UiNode(BaseModel):
    """One node of a composed UI tree."""

    type: str
    """Catalog component name."""

    children: Optional[List[object]] = None
    """
    Nested nodes (each shaped like this one), only where the component's `children`
    allows them. Typed as generic objects so the schema is not self-referential,
    which SDK generators handle poorly.
    """

    props: Optional[object] = None
    """Props that satisfy the component's `props_schema`.

    Omitted when the component has none.
    """
