# coding: utf-8

# flake8: noqa
"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.a06_options import A06Options
from swagger_client.models.a07_response import A07Response
from swagger_client.models.aga_calculation import AGACalculation
from swagger_client.models.aga_details import AGADetails
from swagger_client.models.aga_draw import AGADraw
from swagger_client.models.aga_pension import AGAPension
from swagger_client.models.aga_rate import AGARate
from swagger_client.models.aga_sector import AGASector
from swagger_client.models.aga_sums import AGASums
from swagger_client.models.aga_tax import AGATax
from swagger_client.models.aga_zone import AGAZone
from swagger_client.models.access_point_format import AccessPointFormat
from swagger_client.models.account import Account
from swagger_client.models.account_alias import AccountAlias
from swagger_client.models.account_asset_group import AccountAssetGroup
from swagger_client.models.account_dimension import AccountDimension
from swagger_client.models.account_group import AccountGroup
from swagger_client.models.account_group_set import AccountGroupSet
from swagger_client.models.account_group_setup import AccountGroupSetup
from swagger_client.models.account_mandatory_dimension import AccountMandatoryDimension
from swagger_client.models.account_setup import AccountSetup
from swagger_client.models.account_usage import AccountUsage
from swagger_client.models.account_usage_reference import AccountUsageReference
from swagger_client.models.account_visibility_group import AccountVisibilityGroup
from swagger_client.models.account_visibility_group_account import AccountVisibilityGroupAccount
from swagger_client.models.accrual import Accrual
from swagger_client.models.accrual_period import AccrualPeriod
from swagger_client.models.active_number_series_task import ActiveNumberSeriesTask
from swagger_client.models.address import Address
from swagger_client.models.agency import Agency
from swagger_client.models.agreement import Agreement
from swagger_client.models.altinn import Altinn
from swagger_client.models.altinn_auth_request import AltinnAuthRequest
from swagger_client.models.altinn_get_vat_report_data_from_altinn_result import AltinnGetVatReportDataFromAltinnResult
from swagger_client.models.altinn_receipt import AltinnReceipt
from swagger_client.models.altinn_signing import AltinnSigning
from swagger_client.models.altinn_signing_text_response import AltinnSigningTextResponse
from swagger_client.models.amelding_aga_and_tax_sums import AmeldingAgaAndTaxSums
from swagger_client.models.amelding_data import AmeldingData
from swagger_client.models.amelding_entity import AmeldingEntity
from swagger_client.models.amelding_log import AmeldingLog
from swagger_client.models.amelding_sum_up import AmeldingSumUp
from swagger_client.models.amount_detail import AmountDetail
from swagger_client.models.annual_statement import AnnualStatement
from swagger_client.models.annual_statement_email_info import AnnualStatementEmailInfo
from swagger_client.models.annual_statement_line import AnnualStatementLine
from swagger_client.models.annual_statement_report_setup import AnnualStatementReportSetup
from swagger_client.models.api_key import ApiKey
from swagger_client.models.api_message import ApiMessage
from swagger_client.models.approval import Approval
from swagger_client.models.approval_data import ApprovalData
from swagger_client.models.approval_rule import ApprovalRule
from swagger_client.models.approval_rule_step import ApprovalRuleStep
from swagger_client.models.approval_substitute import ApprovalSubstitute
from swagger_client.models.asset import Asset
from swagger_client.models.asset_group import AssetGroup
from swagger_client.models.asset_report_dto import AssetReportDTO
from swagger_client.models.asset_report_line_dto import AssetReportLineDTO
from swagger_client.models.assignment_details import AssignmentDetails
from swagger_client.models.audit_log import AuditLog
from swagger_client.models.authentication_challenge_be import AuthenticationChallengeBE
from swagger_client.models.autobank_user_dto import AutobankUserDTO
from swagger_client.models.avtale_giro_agreement import AvtaleGiroAgreement
from swagger_client.models.avtale_giro_bank_account import AvtaleGiroBankAccount
from swagger_client.models.avtale_giro_file import AvtaleGiroFile
from swagger_client.models.avtale_giro_merged_file import AvtaleGiroMergedFile
from swagger_client.models.balance_dto import BalanceDto
from swagger_client.models.balance_info import BalanceInfo
from swagger_client.models.bank import Bank
from swagger_client.models.bank_account import BankAccount
from swagger_client.models.bank_account_dto import BankAccountDTO
from swagger_client.models.bank_agreement import BankAgreement
from swagger_client.models.bank_balance_dto import BankBalanceDto
from swagger_client.models.bank_data import BankData
from swagger_client.models.bank_file import BankFile
from swagger_client.models.bank_identifier_code import BankIdentifierCode
from swagger_client.models.bank_integration_agreement import BankIntegrationAgreement
from swagger_client.models.bank_match_suggestion import BankMatchSuggestion
from swagger_client.models.bank_rule import BankRule
from swagger_client.models.bank_service import BankService
from swagger_client.models.bank_service_bank_account import BankServiceBankAccount
from swagger_client.models.bank_statement import BankStatement
from swagger_client.models.bank_statement_entry import BankStatementEntry
from swagger_client.models.bank_statement_match import BankStatementMatch
from swagger_client.models.bank_statement_rule import BankStatementRule
from swagger_client.models.bankfile_column import BankfileColumn
from swagger_client.models.bankfile_format import BankfileFormat
from swagger_client.models.barnepass import Barnepass
from swagger_client.models.barnepass_oppgave import BarnepassOppgave
from swagger_client.models.barnepass_product import BarnepassProduct
from swagger_client.models.basic_amount import BasicAmount
from swagger_client.models.batch_invoice import BatchInvoice
from swagger_client.models.batch_invoice_item import BatchInvoiceItem
from swagger_client.models.budget import Budget
from swagger_client.models.budget_entry import BudgetEntry
from swagger_client.models.budget_import import BudgetImport
from swagger_client.models.business_relation import BusinessRelation
from swagger_client.models.campaign_template import CampaignTemplate
from swagger_client.models.change_autobank_password_dto import ChangeAutobankPasswordDTO
from swagger_client.models.code import Code
from swagger_client.models.comment import Comment
from swagger_client.models.company import Company
from swagger_client.models.company_access import CompanyAccess
from swagger_client.models.company_accounting_settings import CompanyAccountingSettings
from swagger_client.models.company_backup import CompanyBackup
from swagger_client.models.company_bank_account import CompanyBankAccount
from swagger_client.models.company_license_infomation import CompanyLicenseInfomation
from swagger_client.models.company_report import CompanyReport
from swagger_client.models.company_salary import CompanySalary
from swagger_client.models.company_settings import CompanySettings
from swagger_client.models.company_type import CompanyType
from swagger_client.models.company_vacation_rate import CompanyVacationRate
from swagger_client.models.complex_validation_rule import ComplexValidationRule
from swagger_client.models.complex_validation_rule_template import ComplexValidationRuleTemplate
from swagger_client.models.component_layout import ComponentLayout
from swagger_client.models.component_layout_dto import ComponentLayoutDto
from swagger_client.models.confirmation import Confirmation
from swagger_client.models.contact import Contact
from swagger_client.models.contact_search_service_response import ContactSearchServiceResponse
from swagger_client.models.contract import Contract
from swagger_client.models.contract_address import ContractAddress
from swagger_client.models.contract_asset import ContractAsset
from swagger_client.models.contract_cron import ContractCron
from swagger_client.models.contract_debug_log import ContractDebugLog
from swagger_client.models.contract_license_type import ContractLicenseType
from swagger_client.models.contract_obyte import ContractObyte
from swagger_client.models.contract_parameter import ContractParameter
from swagger_client.models.contract_run_log import ContractRunLog
from swagger_client.models.contract_transaction import ContractTransaction
from swagger_client.models.contract_trigger import ContractTrigger
from swagger_client.models.cost_allocation import CostAllocation
from swagger_client.models.cost_allocation_item import CostAllocationItem
from swagger_client.models.country import Country
from swagger_client.models.create_avtale_giro_payment_batch_dto import CreateAvtaleGiroPaymentBatchDTO
from swagger_client.models.create_bank_integration_dto import CreateBankIntegrationDTO
from swagger_client.models.create_bank_user_dto import CreateBankUserDTO
from swagger_client.models.create_company_details import CreateCompanyDetails
from swagger_client.models.create_payment_batch_dto import CreatePaymentBatchDTO
from swagger_client.models.currency import Currency
from swagger_client.models.currency_code import CurrencyCode
from swagger_client.models.currency_override import CurrencyOverride
from swagger_client.models.currency_rate_data import CurrencyRateData
from swagger_client.models.custom_field import CustomField
from swagger_client.models.custom_liquidity_payment import CustomLiquidityPayment
from swagger_client.models.custom_values import CustomValues
from swagger_client.models.customer import Customer
from swagger_client.models.customer_invoice import CustomerInvoice
from swagger_client.models.customer_invoice_item import CustomerInvoiceItem
from swagger_client.models.customer_invoice_reminder import CustomerInvoiceReminder
from swagger_client.models.customer_invoice_reminder_rule import CustomerInvoiceReminderRule
from swagger_client.models.customer_invoice_reminder_settings import CustomerInvoiceReminderSettings
from swagger_client.models.customer_license_agreement_info import CustomerLicenseAgreementInfo
from swagger_client.models.customer_no_and_name import CustomerNoAndName
from swagger_client.models.customer_order import CustomerOrder
from swagger_client.models.customer_order_item import CustomerOrderItem
from swagger_client.models.customer_quote import CustomerQuote
from swagger_client.models.customer_quote_item import CustomerQuoteItem
from swagger_client.models.debt_collection_automation import DebtCollectionAutomation
from swagger_client.models.debt_collection_settings import DebtCollectionSettings
from swagger_client.models.denied_user_access_log import DeniedUserAccessLog
from swagger_client.models.department import Department
from swagger_client.models.depreciation_line import DepreciationLine
from swagger_client.models.details_dto import DetailsDTO
from swagger_client.models.dimension10 import Dimension10
from swagger_client.models.dimension5 import Dimension5
from swagger_client.models.dimension6 import Dimension6
from swagger_client.models.dimension7 import Dimension7
from swagger_client.models.dimension8 import Dimension8
from swagger_client.models.dimension9 import Dimension9
from swagger_client.models.dimension_settings import DimensionSettings
from swagger_client.models.dimensions import Dimensions
from swagger_client.models.dimensions_info import DimensionsInfo
from swagger_client.models.distribution_plan import DistributionPlan
from swagger_client.models.distribution_plan_element import DistributionPlanElement
from swagger_client.models.distribution_plan_element_type import DistributionPlanElementType
from swagger_client.models.distribution_plan_element_type_legal_entity import DistributionPlanElementTypeLegalEntity
from swagger_client.models.distribution_plan_element_validation import DistributionPlanElementValidation
from swagger_client.models.distribution_type import DistributionType
from swagger_client.models.distributions import Distributions
from swagger_client.models.draw_foreigner_with_percent import DrawForeignerWithPercent
from swagger_client.models.ehf_customer import EHFCustomer
from swagger_client.models.ehf_log import EHFLog
from swagger_client.models.elsa_usage_log import ElsaUsageLog
from swagger_client.models.email import Email
from swagger_client.models.email_dto import EmailDTO
from swagger_client.models.email_log import EmailLog
from swagger_client.models.employee import Employee
from swagger_client.models.employee_category import EmployeeCategory
from swagger_client.models.employee_category_link import EmployeeCategoryLink
from swagger_client.models.employee_language import EmployeeLanguage
from swagger_client.models.employee_leave import EmployeeLeave
from swagger_client.models.employee_status import EmployeeStatus
from swagger_client.models.employee_tax_card import EmployeeTaxCard
from swagger_client.models.employees import Employees
from swagger_client.models.employment import Employment
from swagger_client.models.employment_history_record import EmploymentHistoryRecord
from swagger_client.models.employment_leaves import EmploymentLeaves
from swagger_client.models.employment_valid_values import EmploymentValidValues
from swagger_client.models.employments import Employments
from swagger_client.models.enclosure import Enclosure
from swagger_client.models.encryption_info import EncryptionInfo
from swagger_client.models.entity_validation_rule import EntityValidationRule
from swagger_client.models.entity_validation_rule_template import EntityValidationRuleTemplate
from swagger_client.models.event_subscriber import EventSubscriber
from swagger_client.models.eventplan import Eventplan
from swagger_client.models.expression_filter import ExpressionFilter
from swagger_client.models.extension_data_object import ExtensionDataObject
from swagger_client.models.failed_bank_file import FailedBankFile
from swagger_client.models.field import Field
from swagger_client.models.field_layout import FieldLayout
from swagger_client.models.field_layout_dto import FieldLayoutDto
from swagger_client.models.fields_changed import FieldsChanged
from swagger_client.models.file import File
from swagger_client.models.file_entity_link import FileEntityLink
from swagger_client.models.file_tag import FileTag
from swagger_client.models.financial_deadline import FinancialDeadline
from swagger_client.models.financial_year import FinancialYear
from swagger_client.models.flex_detail import FlexDetail
from swagger_client.models.foreigner_with_amount import ForeignerWithAmount
from swagger_client.models.foreigner_with_percent import ForeignerWithPercent
from swagger_client.models.forskuddstrekk import Forskuddstrekk
from swagger_client.models.fradrag import Fradrag
from swagger_client.models.free_amount_summary import FreeAmountSummary
from swagger_client.models.free_amount_used import FreeAmountUsed
from swagger_client.models.grant import Grant
from swagger_client.models.handle_state import HandleState
from swagger_client.models.hangfire_job import HangfireJob
from swagger_client.models.hangfire_job_context import HangfireJobContext
from swagger_client.models.hangfire_response import HangfireResponse
from swagger_client.models.i_action_result import IActionResult
from swagger_client.models.invoice_payment import InvoicePayment
from swagger_client.models.invoice_payment_data import InvoicePaymentData
from swagger_client.models.invoice_summary import InvoiceSummary
from swagger_client.models.invoices_and_reminders_ready_to_remind import InvoicesAndRemindersReadyToRemind
from swagger_client.models.item_source import ItemSource
from swagger_client.models.item_source_detail import ItemSourceDetail
from swagger_client.models.journal_entry import JournalEntry
from swagger_client.models.journal_entry_data import JournalEntryData
from swagger_client.models.journal_entry_line import JournalEntryLine
from swagger_client.models.journal_entry_line_couple import JournalEntryLineCouple
from swagger_client.models.journal_entry_line_draft import JournalEntryLineDraft
from swagger_client.models.journal_entry_line_post_post_data import JournalEntryLinePostPostData
from swagger_client.models.journal_entry_line_request_summary import JournalEntryLineRequestSummary
from swagger_client.models.journal_entry_mode import JournalEntryMode
from swagger_client.models.journal_entry_payment_data import JournalEntryPaymentData
from swagger_client.models.journal_entry_period_data import JournalEntryPeriodData
from swagger_client.models.journal_entry_source_serie import JournalEntrySourceSerie
from swagger_client.models.journal_entry_type import JournalEntryType
from swagger_client.models.journal_suggestion import JournalSuggestion
from swagger_client.models.kpi_definition import KpiDefinition
from swagger_client.models.kpi_value import KpiValue
from swagger_client.models.language import Language
from swagger_client.models.language_code import LanguageCode
from swagger_client.models.ledger_suggestion import LedgerSuggestion
from swagger_client.models.license_agreement_info import LicenseAgreementInfo
from swagger_client.models.limits import Limits
from swagger_client.models.liquidity_table_dto import LiquidityTableDTO
from swagger_client.models.loennsinntekt import Loennsinntekt
from swagger_client.models.mandatory_dimension_account_report import MandatoryDimensionAccountReport
from swagger_client.models.marking_entry import MarkingEntry
from swagger_client.models.marking_reference import MarkingReference
from swagger_client.models.marking_result import MarkingResult
from swagger_client.models.match_candidate import MatchCandidate
from swagger_client.models.match_request import MatchRequest
from swagger_client.models.match_settings import MatchSettings
from swagger_client.models.member_details import MemberDetails
from swagger_client.models.mentioned import Mentioned
from swagger_client.models.model import Model
from swagger_client.models.municipal import Municipal
from swagger_client.models.municipal_aga_zone import MunicipalAGAZone
from swagger_client.models.naeringsinntekt import Naeringsinntekt
from swagger_client.models.notification import Notification
from swagger_client.models.number_series import NumberSeries
from swagger_client.models.number_series_invalid_overlap import NumberSeriesInvalidOverlap
from swagger_client.models.number_series_task import NumberSeriesTask
from swagger_client.models.number_series_type import NumberSeriesType
from swagger_client.models.order_offer import OrderOffer
from swagger_client.models.otp_export_wagetype import OtpExportWagetype
from swagger_client.models.outgoing_invoice import OutgoingInvoice
from swagger_client.models.pay_aga_tax_dto import PayAgaTaxDTO
from swagger_client.models.paycheck import Paycheck
from swagger_client.models.paycheck_email_info import PaycheckEmailInfo
from swagger_client.models.paycheck_report_setup import PaycheckReportSetup
from swagger_client.models.payment import Payment
from swagger_client.models.payment_batch import PaymentBatch
from swagger_client.models.payment_batch_type import PaymentBatchType
from swagger_client.models.payment_code import PaymentCode
from swagger_client.models.payment_info_type import PaymentInfoType
from swagger_client.models.payment_info_type_part import PaymentInfoTypePart
from swagger_client.models.payroll_run import PayrollRun
from swagger_client.models.payroll_run_category_link import PayrollRunCategoryLink
from swagger_client.models.payroll_run_in_amelding_period import PayrollRunInAmeldingPeriod
from swagger_client.models.pension_scheme import PensionScheme
from swagger_client.models.pension_scheme_supplier import PensionSchemeSupplier
from swagger_client.models.pensjon_eller_trygd import PensjonEllerTrygd
from swagger_client.models.period import Period
from swagger_client.models.period_series import PeriodSeries
from swagger_client.models.period_template import PeriodTemplate
from swagger_client.models.permission import Permission
from swagger_client.models.phone import Phone
from swagger_client.models.post_post import PostPost
from swagger_client.models.postal_code import PostalCode
from swagger_client.models.posting_summary import PostingSummary
from swagger_client.models.posting_summary_draft import PostingSummaryDraft
from swagger_client.models.predefined_description import PredefinedDescription
from swagger_client.models.process_file_log import ProcessFileLog
from swagger_client.models.product import Product
from swagger_client.models.product_category import ProductCategory
from swagger_client.models.product_category_link import ProductCategoryLink
from swagger_client.models.project import Project
from swagger_client.models.project_resource import ProjectResource
from swagger_client.models.project_resource_schedule import ProjectResourceSchedule
from swagger_client.models.project_task import ProjectTask
from swagger_client.models.project_task_schedule import ProjectTaskSchedule
from swagger_client.models.re_invoice import ReInvoice
from swagger_client.models.re_invoice_item import ReInvoiceItem
from swagger_client.models.reason import Reason
from swagger_client.models.reconciliation import Reconciliation
from swagger_client.models.reconciliation_group import ReconciliationGroup
from swagger_client.models.reconciliation_line import ReconciliationLine
from swagger_client.models.reconciliation_status import ReconciliationStatus
from swagger_client.models.recurring_invoice import RecurringInvoice
from swagger_client.models.recurring_invoice_item import RecurringInvoiceItem
from swagger_client.models.recurring_invoice_log import RecurringInvoiceLog
from swagger_client.models.region import Region
from swagger_client.models.regulative import Regulative
from swagger_client.models.regulative_group import RegulativeGroup
from swagger_client.models.regulative_step import RegulativeStep
from swagger_client.models.report_definition import ReportDefinition
from swagger_client.models.report_definition_data_source import ReportDefinitionDataSource
from swagger_client.models.report_definition_parameter import ReportDefinitionParameter
from swagger_client.models.report_parameter import ReportParameter
from swagger_client.models.report_row import ReportRow
from swagger_client.models.responsible import Responsible
from swagger_client.models.role import Role
from swagger_client.models.role_permission import RolePermission
from swagger_client.models.rss_item import RssItem
from swagger_client.models.rss_list import RssList
from swagger_client.models.styrk_code import STYRKCode
from swagger_client.models.saft_mapping_account import SaftMappingAccount
from swagger_client.models.salary_balance import SalaryBalance
from swagger_client.models.salary_balance_line import SalaryBalanceLine
from swagger_client.models.salary_balance_pay_line import SalaryBalancePayLine
from swagger_client.models.salary_balance_template import SalaryBalanceTemplate
from swagger_client.models.salary_transaction import SalaryTransaction
from swagger_client.models.salary_transaction_pay import SalaryTransactionPay
from swagger_client.models.salary_transaction_pay_line import SalaryTransactionPayLine
from swagger_client.models.salary_transaction_period_sums import SalaryTransactionPeriodSums
from swagger_client.models.salary_transaction_sums import SalaryTransactionSums
from swagger_client.models.salary_transaction_supplement import SalaryTransactionSupplement
from swagger_client.models.salary_year import SalaryYear
from swagger_client.models.self_employed import SelfEmployed
from swagger_client.models.self_employed_item import SelfEmployedItem
from swagger_client.models.seller import Seller
from swagger_client.models.seller_link import SellerLink
from swagger_client.models.send_email import SendEmail
from swagger_client.models.send_email_attachment import SendEmailAttachment
from swagger_client.models.service_account import ServiceAccount
from swagger_client.models.service_metadata_dto import ServiceMetadataDto
from swagger_client.models.set_integration_data_dto import SetIntegrationDataDto
from swagger_client.models.sharing import Sharing
from swagger_client.models.sharing_status_update import SharingStatusUpdate
from swagger_client.models.sharing_updates import SharingUpdates
from swagger_client.models.split_file_multipe_result import SplitFileMultipeResult
from swagger_client.models.split_file_result import SplitFileResult
from swagger_client.models.standard_pension_scheme_supplier import StandardPensionSchemeSupplier
from swagger_client.models.static_register import StaticRegister
from swagger_client.models.status import Status
from swagger_client.models.status_category import StatusCategory
from swagger_client.models.status_log import StatusLog
from swagger_client.models.status_remark import StatusRemark
from swagger_client.models.sub_company import SubCompany
from swagger_client.models.sub_entity import SubEntity
from swagger_client.models.sub_entity_aga_sums import SubEntityAgaSums
from swagger_client.models.sum_on_run import SumOnRun
from swagger_client.models.sum_on_year import SumOnYear
from swagger_client.models.sums import Sums
from swagger_client.models.supplement_info import SupplementInfo
from swagger_client.models.supplier import Supplier
from swagger_client.models.supplier_invoice import SupplierInvoice
from swagger_client.models.supplier_invoice_detail import SupplierInvoiceDetail
from swagger_client.models.supplier_invoice_item import SupplierInvoiceItem
from swagger_client.models.tof_currency_settings import TOFCurrencySettings
from swagger_client.models.task import Task
from swagger_client.models.task_approval_plan import TaskApprovalPlan
from swagger_client.models.tax_and_aga_sums import TaxAndAgaSums
from swagger_client.models.tax_basis import TaxBasis
from swagger_client.models.tax_card import TaxCard
from swagger_client.models.tax_card_read_status import TaxCardReadStatus
from swagger_client.models.team import Team
from swagger_client.models.team_position import TeamPosition
from swagger_client.models.team_position_dto import TeamPositionDto
from swagger_client.models.team_report import TeamReport
from swagger_client.models.terms import Terms
from swagger_client.models.time_sheet import TimeSheet
from swagger_client.models.time_sheet_item import TimeSheetItem
from swagger_client.models.totals import Totals
from swagger_client.models.tracelink import Tracelink
from swagger_client.models.trade_header_calculation_summary import TradeHeaderCalculationSummary
from swagger_client.models.transaction_types import TransactionTypes
from swagger_client.models.transition import Transition
from swagger_client.models.transition_flow import TransitionFlow
from swagger_client.models.transition_threshold import TransitionThreshold
from swagger_client.models.transition_threshold_approval import TransitionThresholdApproval
from swagger_client.models.translatable import Translatable
from swagger_client.models.translation import Translation
from swagger_client.models.travel import Travel
from swagger_client.models.travel_line import TravelLine
from swagger_client.models.travel_type import TravelType
from swagger_client.models.uni_query_definition import UniQueryDefinition
from swagger_client.models.uni_query_field import UniQueryField
from swagger_client.models.uni_query_filter import UniQueryFilter
from swagger_client.models.union_member import UnionMember
from swagger_client.models.union_report import UnionReport
from swagger_client.models.union_summary import UnionSummary
from swagger_client.models.update_service_iddto import UpdateServiceIDDTO
from swagger_client.models.update_service_status_dto import UpdateServiceStatusDTO
from swagger_client.models.user import User
from swagger_client.models.user_dto import UserDto
from swagger_client.models.user_license_information import UserLicenseInformation
from swagger_client.models.user_license_type import UserLicenseType
from swagger_client.models.user_role import UserRole
from swagger_client.models.user_verification import UserVerification
from swagger_client.models.utleggstrekk import Utleggstrekk
from swagger_client.models.vacation_pay_last_year import VacationPayLastYear
from swagger_client.models.vacation_pay_line import VacationPayLine
from swagger_client.models.vacation_rate_employee import VacationRateEmployee
from swagger_client.models.value_item import ValueItem
from swagger_client.models.value_list import ValueList
from swagger_client.models.vat_calculation_summary import VatCalculationSummary
from swagger_client.models.vat_code_group import VatCodeGroup
from swagger_client.models.vat_code_group_setup import VatCodeGroupSetup
from swagger_client.models.vat_deduction import VatDeduction
from swagger_client.models.vat_deduction_group import VatDeductionGroup
from swagger_client.models.vat_post import VatPost
from swagger_client.models.vat_post_setup import VatPostSetup
from swagger_client.models.vat_report import VatReport
from swagger_client.models.vat_report_archived_summary import VatReportArchivedSummary
from swagger_client.models.vat_report_form import VatReportForm
from swagger_client.models.vat_report_message import VatReportMessage
from swagger_client.models.vat_report_not_reported_journal_entry_data import VatReportNotReportedJournalEntryData
from swagger_client.models.vat_report_reference import VatReportReference
from swagger_client.models.vat_report_reference_setup import VatReportReferenceSetup
from swagger_client.models.vat_report_summary import VatReportSummary
from swagger_client.models.vat_report_summary_per_post import VatReportSummaryPerPost
from swagger_client.models.vat_report_summary_per_post_per_account import VatReportSummaryPerPostPerAccount
from swagger_client.models.vat_report_type import VatReportType
from swagger_client.models.vat_type import VatType
from swagger_client.models.vat_type_percentage import VatTypePercentage
from swagger_client.models.vat_type_setup import VatTypeSetup
from swagger_client.models.vat_type_setup_percentage import VatTypeSetupPercentage
from swagger_client.models.wage_type import WageType
from swagger_client.models.wage_type_supplement import WageTypeSupplement
from swagger_client.models.wage_type_translation import WageTypeTranslation
from swagger_client.models.work_balance import WorkBalance
from swagger_client.models.work_balance_dto import WorkBalanceDto
from swagger_client.models.work_item import WorkItem
from swagger_client.models.work_item_group import WorkItemGroup
from swagger_client.models.work_item_to_salary import WorkItemToSalary
from swagger_client.models.work_profile import WorkProfile
from swagger_client.models.work_relation import WorkRelation
from swagger_client.models.work_time_off import WorkTimeOff
from swagger_client.models.work_type import WorkType
from swagger_client.models.worker import Worker
from swagger_client.models.ytelse_fra_offentlige import YtelseFraOffentlige
from swagger_client.models.zdata_update_bank_properties import ZdataUpdateBankProperties
