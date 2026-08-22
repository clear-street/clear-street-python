# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .company_document_type import CompanyDocumentType
from .company_document_preview import CompanyDocumentPreview
from .company_document_relation import CompanyDocumentRelation

__all__ = ["CompanyDocumentResource"]


class CompanyDocumentResource(BaseModel):
    """A company-level research or source document."""

    document_type: CompanyDocumentType
    """Typed document kind."""

    relation: CompanyDocumentRelation
    """Relationship to this company."""

    title: str
    """Display title."""

    url: str
    """Document URL."""

    external_id: Optional[str] = None
    """Optional source identifier retained for reconciliation."""

    preview: Optional[CompanyDocumentPreview] = None
    """Optional card preview."""

    published_at: Optional[datetime] = None
    """Publication time, when known."""
