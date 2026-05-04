# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ...._models import BaseModel
from ..fiscal_period_type import FiscalPeriodType

__all__ = ["InstrumentIncomeStatement"]


class InstrumentIncomeStatement(BaseModel):
    """A quarterly income statement for an instrument."""

    accepted_date: datetime
    """The date and time when the filing was accepted by the SEC"""

    filing_date: date
    """The date the financial statement was filed"""

    period: str
    """The fiscal period identifier (e.g., "Q1", "Q2", "Q3", "Q4")"""

    period_type: FiscalPeriodType
    """The type of fiscal period"""

    reported_currency: str
    """The currency in which the statement is reported (ISO 4217)"""

    year: int
    """The fiscal year of the statement"""

    bottom_line_net_income: Optional[str] = None
    """Bottom line net income after all adjustments"""

    cost_and_expenses: Optional[str] = None
    """Total costs and expenses"""

    cost_of_revenue: Optional[str] = None
    """Direct costs attributable to producing goods sold"""

    depreciation_and_amortization: Optional[str] = None
    """Depreciation and amortization expenses"""

    ebit: Optional[str] = None
    """Earnings before interest and taxes"""

    ebitda: Optional[str] = None
    """Earnings before interest, taxes, depreciation, and amortization"""

    eps: Optional[str] = None
    """Basic earnings per share"""

    eps_diluted: Optional[str] = None
    """Diluted earnings per share"""

    general_and_administrative_expenses: Optional[str] = None
    """General administrative overhead expenses"""

    gross_profit: Optional[str] = None
    """Revenue minus cost of revenue"""

    income_before_tax: Optional[str] = None
    """Income before income tax expense"""

    income_tax_expense: Optional[str] = None
    """Income tax expense for the period"""

    interest_expense: Optional[str] = None
    """Interest paid on debt"""

    interest_income: Optional[str] = None
    """Interest earned on investments and cash"""

    net_income: Optional[str] = None
    """Total net income for the period"""

    net_income_deductions: Optional[str] = None
    """Deductions from net income"""

    net_income_from_continuing_operations: Optional[str] = None
    """Net income from continuing operations"""

    net_income_from_discontinued_operations: Optional[str] = None
    """Net income from discontinued operations"""

    net_interest_income: Optional[str] = None
    """Net interest income (interest income minus interest expense)"""

    non_operating_income_excluding_interest: Optional[str] = None
    """Non-operating income excluding interest"""

    operating_expenses: Optional[str] = None
    """Total operating expenses"""

    operating_income: Optional[str] = None
    """Income from core business operations"""

    other_adjustments_to_net_income: Optional[str] = None
    """Other adjustments to net income"""

    other_expenses: Optional[str] = None
    """Other miscellaneous expenses"""

    research_and_development_expenses: Optional[str] = None
    """Expenditure on research and development activities"""

    revenue: Optional[str] = None
    """Total revenue from sales of goods and services"""

    selling_and_marketing_expenses: Optional[str] = None
    """Expenditure on marketing and sales activities"""

    selling_general_and_administrative_expenses: Optional[str] = None
    """Combined selling, general, and administrative expenses"""

    total_other_income_expenses_net: Optional[str] = None
    """Net of other income and expenses"""

    weighted_average_shs_out: Optional[str] = None
    """Weighted average shares outstanding (basic)"""

    weighted_average_shs_out_dil: Optional[str] = None
    """Weighted average shares outstanding (diluted)"""
