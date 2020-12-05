# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CompanySalary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'main_account_cost_vacation': 'int',
        'main_account_allocated_financial_vacation': 'int',
        'base_netto_payment_for_maritim': 'bool',
        'main_account_allocated_vacation': 'int',
        'otp_export_active': 'bool',
        'base_spesial_deduction_for_maritim': 'bool',
        'interrim_remit_account': 'int',
        'base_netto_payment': 'bool',
        'main_account_cost_aga_vacation': 'int',
        'wagetype_advance_payment': 'int',
        'wage_deduction_due_to_holiday': 'str',
        'base_tax_free_organization': 'bool',
        'status_code': 'int',
        'deleted': 'bool',
        'allow_over6_g': 'bool',
        'annual_statement_zip_report_id': 'int',
        'base_pay_as_you_earn_tax_on_pensions': 'bool',
        'post_garnishment_to_tax_account': 'bool',
        'main_account_cost_financial': 'int',
        'wagetype_advance_payment_auto': 'int',
        'post_to_tax_draw': 'bool',
        'base_svalbard': 'bool',
        'main_account_cost_aga': 'int',
        'id': 'int',
        'main_account_allocated_financial': 'int',
        'main_account_allocated_aga': 'int',
        'updated_by': 'str',
        'base_jan_mayen_and_bi_countries': 'bool',
        'paycheck_zip_report_id': 'int',
        'created_by': 'str',
        'main_account_cost_financial_vacation': 'int',
        'calculate_financial_tax': 'bool',
        'main_account_allocated_aga_vacation': 'int',
        'payment_interval': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'main_account_cost_vacation': 'MainAccountCostVacation',
        'main_account_allocated_financial_vacation': 'MainAccountAllocatedFinancialVacation',
        'base_netto_payment_for_maritim': 'Base_NettoPaymentForMaritim',
        'main_account_allocated_vacation': 'MainAccountAllocatedVacation',
        'otp_export_active': 'OtpExportActive',
        'base_spesial_deduction_for_maritim': 'Base_SpesialDeductionForMaritim',
        'interrim_remit_account': 'InterrimRemitAccount',
        'base_netto_payment': 'Base_NettoPayment',
        'main_account_cost_aga_vacation': 'MainAccountCostAGAVacation',
        'wagetype_advance_payment': 'WagetypeAdvancePayment',
        'wage_deduction_due_to_holiday': 'WageDeductionDueToHoliday',
        'base_tax_free_organization': 'Base_TaxFreeOrganization',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'allow_over6_g': 'AllowOver6G',
        'annual_statement_zip_report_id': 'AnnualStatementZipReportID',
        'base_pay_as_you_earn_tax_on_pensions': 'Base_PayAsYouEarnTaxOnPensions',
        'post_garnishment_to_tax_account': 'PostGarnishmentToTaxAccount',
        'main_account_cost_financial': 'MainAccountCostFinancial',
        'wagetype_advance_payment_auto': 'WagetypeAdvancePaymentAuto',
        'post_to_tax_draw': 'PostToTaxDraw',
        'base_svalbard': 'Base_Svalbard',
        'main_account_cost_aga': 'MainAccountCostAGA',
        'id': 'ID',
        'main_account_allocated_financial': 'MainAccountAllocatedFinancial',
        'main_account_allocated_aga': 'MainAccountAllocatedAGA',
        'updated_by': 'UpdatedBy',
        'base_jan_mayen_and_bi_countries': 'Base_JanMayenAndBiCountries',
        'paycheck_zip_report_id': 'PaycheckZipReportID',
        'created_by': 'CreatedBy',
        'main_account_cost_financial_vacation': 'MainAccountCostFinancialVacation',
        'calculate_financial_tax': 'CalculateFinancialTax',
        'main_account_allocated_aga_vacation': 'MainAccountAllocatedAGAVacation',
        'payment_interval': 'PaymentInterval',
        'custom_values': 'CustomValues'
    }

    def __init__(self, main_account_cost_vacation=None, main_account_allocated_financial_vacation=None, base_netto_payment_for_maritim=None, main_account_allocated_vacation=None, otp_export_active=None, base_spesial_deduction_for_maritim=None, interrim_remit_account=None, base_netto_payment=None, main_account_cost_aga_vacation=None, wagetype_advance_payment=None, wage_deduction_due_to_holiday=None, base_tax_free_organization=None, status_code=None, deleted=None, allow_over6_g=None, annual_statement_zip_report_id=None, base_pay_as_you_earn_tax_on_pensions=None, post_garnishment_to_tax_account=None, main_account_cost_financial=None, wagetype_advance_payment_auto=None, post_to_tax_draw=None, base_svalbard=None, main_account_cost_aga=None, id=None, main_account_allocated_financial=None, main_account_allocated_aga=None, updated_by=None, base_jan_mayen_and_bi_countries=None, paycheck_zip_report_id=None, created_by=None, main_account_cost_financial_vacation=None, calculate_financial_tax=None, main_account_allocated_aga_vacation=None, payment_interval=None, custom_values=None):  # noqa: E501
        """CompanySalary - a model defined in Swagger"""  # noqa: E501
        self._main_account_cost_vacation = None
        self._main_account_allocated_financial_vacation = None
        self._base_netto_payment_for_maritim = None
        self._main_account_allocated_vacation = None
        self._otp_export_active = None
        self._base_spesial_deduction_for_maritim = None
        self._interrim_remit_account = None
        self._base_netto_payment = None
        self._main_account_cost_aga_vacation = None
        self._wagetype_advance_payment = None
        self._wage_deduction_due_to_holiday = None
        self._base_tax_free_organization = None
        self._status_code = None
        self._deleted = None
        self._allow_over6_g = None
        self._annual_statement_zip_report_id = None
        self._base_pay_as_you_earn_tax_on_pensions = None
        self._post_garnishment_to_tax_account = None
        self._main_account_cost_financial = None
        self._wagetype_advance_payment_auto = None
        self._post_to_tax_draw = None
        self._base_svalbard = None
        self._main_account_cost_aga = None
        self._id = None
        self._main_account_allocated_financial = None
        self._main_account_allocated_aga = None
        self._updated_by = None
        self._base_jan_mayen_and_bi_countries = None
        self._paycheck_zip_report_id = None
        self._created_by = None
        self._main_account_cost_financial_vacation = None
        self._calculate_financial_tax = None
        self._main_account_allocated_aga_vacation = None
        self._payment_interval = None
        self._custom_values = None
        self.discriminator = None
        if main_account_cost_vacation is not None:
            self.main_account_cost_vacation = main_account_cost_vacation
        if main_account_allocated_financial_vacation is not None:
            self.main_account_allocated_financial_vacation = main_account_allocated_financial_vacation
        if base_netto_payment_for_maritim is not None:
            self.base_netto_payment_for_maritim = base_netto_payment_for_maritim
        if main_account_allocated_vacation is not None:
            self.main_account_allocated_vacation = main_account_allocated_vacation
        if otp_export_active is not None:
            self.otp_export_active = otp_export_active
        if base_spesial_deduction_for_maritim is not None:
            self.base_spesial_deduction_for_maritim = base_spesial_deduction_for_maritim
        if interrim_remit_account is not None:
            self.interrim_remit_account = interrim_remit_account
        if base_netto_payment is not None:
            self.base_netto_payment = base_netto_payment
        if main_account_cost_aga_vacation is not None:
            self.main_account_cost_aga_vacation = main_account_cost_aga_vacation
        if wagetype_advance_payment is not None:
            self.wagetype_advance_payment = wagetype_advance_payment
        if wage_deduction_due_to_holiday is not None:
            self.wage_deduction_due_to_holiday = wage_deduction_due_to_holiday
        if base_tax_free_organization is not None:
            self.base_tax_free_organization = base_tax_free_organization
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if allow_over6_g is not None:
            self.allow_over6_g = allow_over6_g
        if annual_statement_zip_report_id is not None:
            self.annual_statement_zip_report_id = annual_statement_zip_report_id
        if base_pay_as_you_earn_tax_on_pensions is not None:
            self.base_pay_as_you_earn_tax_on_pensions = base_pay_as_you_earn_tax_on_pensions
        if post_garnishment_to_tax_account is not None:
            self.post_garnishment_to_tax_account = post_garnishment_to_tax_account
        if main_account_cost_financial is not None:
            self.main_account_cost_financial = main_account_cost_financial
        if wagetype_advance_payment_auto is not None:
            self.wagetype_advance_payment_auto = wagetype_advance_payment_auto
        if post_to_tax_draw is not None:
            self.post_to_tax_draw = post_to_tax_draw
        if base_svalbard is not None:
            self.base_svalbard = base_svalbard
        if main_account_cost_aga is not None:
            self.main_account_cost_aga = main_account_cost_aga
        if id is not None:
            self.id = id
        if main_account_allocated_financial is not None:
            self.main_account_allocated_financial = main_account_allocated_financial
        if main_account_allocated_aga is not None:
            self.main_account_allocated_aga = main_account_allocated_aga
        if updated_by is not None:
            self.updated_by = updated_by
        if base_jan_mayen_and_bi_countries is not None:
            self.base_jan_mayen_and_bi_countries = base_jan_mayen_and_bi_countries
        if paycheck_zip_report_id is not None:
            self.paycheck_zip_report_id = paycheck_zip_report_id
        if created_by is not None:
            self.created_by = created_by
        if main_account_cost_financial_vacation is not None:
            self.main_account_cost_financial_vacation = main_account_cost_financial_vacation
        if calculate_financial_tax is not None:
            self.calculate_financial_tax = calculate_financial_tax
        if main_account_allocated_aga_vacation is not None:
            self.main_account_allocated_aga_vacation = main_account_allocated_aga_vacation
        if payment_interval is not None:
            self.payment_interval = payment_interval
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def main_account_cost_vacation(self):
        """Gets the main_account_cost_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_cost_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_cost_vacation

    @main_account_cost_vacation.setter
    def main_account_cost_vacation(self, main_account_cost_vacation):
        """Sets the main_account_cost_vacation of this CompanySalary.


        :param main_account_cost_vacation: The main_account_cost_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_cost_vacation = main_account_cost_vacation

    @property
    def main_account_allocated_financial_vacation(self):
        """Gets the main_account_allocated_financial_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_allocated_financial_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_allocated_financial_vacation

    @main_account_allocated_financial_vacation.setter
    def main_account_allocated_financial_vacation(self, main_account_allocated_financial_vacation):
        """Sets the main_account_allocated_financial_vacation of this CompanySalary.


        :param main_account_allocated_financial_vacation: The main_account_allocated_financial_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_allocated_financial_vacation = main_account_allocated_financial_vacation

    @property
    def base_netto_payment_for_maritim(self):
        """Gets the base_netto_payment_for_maritim of this CompanySalary.  # noqa: E501


        :return: The base_netto_payment_for_maritim of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_netto_payment_for_maritim

    @base_netto_payment_for_maritim.setter
    def base_netto_payment_for_maritim(self, base_netto_payment_for_maritim):
        """Sets the base_netto_payment_for_maritim of this CompanySalary.


        :param base_netto_payment_for_maritim: The base_netto_payment_for_maritim of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_netto_payment_for_maritim = base_netto_payment_for_maritim

    @property
    def main_account_allocated_vacation(self):
        """Gets the main_account_allocated_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_allocated_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_allocated_vacation

    @main_account_allocated_vacation.setter
    def main_account_allocated_vacation(self, main_account_allocated_vacation):
        """Sets the main_account_allocated_vacation of this CompanySalary.


        :param main_account_allocated_vacation: The main_account_allocated_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_allocated_vacation = main_account_allocated_vacation

    @property
    def otp_export_active(self):
        """Gets the otp_export_active of this CompanySalary.  # noqa: E501


        :return: The otp_export_active of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._otp_export_active

    @otp_export_active.setter
    def otp_export_active(self, otp_export_active):
        """Sets the otp_export_active of this CompanySalary.


        :param otp_export_active: The otp_export_active of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._otp_export_active = otp_export_active

    @property
    def base_spesial_deduction_for_maritim(self):
        """Gets the base_spesial_deduction_for_maritim of this CompanySalary.  # noqa: E501


        :return: The base_spesial_deduction_for_maritim of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_spesial_deduction_for_maritim

    @base_spesial_deduction_for_maritim.setter
    def base_spesial_deduction_for_maritim(self, base_spesial_deduction_for_maritim):
        """Sets the base_spesial_deduction_for_maritim of this CompanySalary.


        :param base_spesial_deduction_for_maritim: The base_spesial_deduction_for_maritim of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_spesial_deduction_for_maritim = base_spesial_deduction_for_maritim

    @property
    def interrim_remit_account(self):
        """Gets the interrim_remit_account of this CompanySalary.  # noqa: E501


        :return: The interrim_remit_account of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._interrim_remit_account

    @interrim_remit_account.setter
    def interrim_remit_account(self, interrim_remit_account):
        """Sets the interrim_remit_account of this CompanySalary.


        :param interrim_remit_account: The interrim_remit_account of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._interrim_remit_account = interrim_remit_account

    @property
    def base_netto_payment(self):
        """Gets the base_netto_payment of this CompanySalary.  # noqa: E501


        :return: The base_netto_payment of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_netto_payment

    @base_netto_payment.setter
    def base_netto_payment(self, base_netto_payment):
        """Sets the base_netto_payment of this CompanySalary.


        :param base_netto_payment: The base_netto_payment of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_netto_payment = base_netto_payment

    @property
    def main_account_cost_aga_vacation(self):
        """Gets the main_account_cost_aga_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_cost_aga_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_cost_aga_vacation

    @main_account_cost_aga_vacation.setter
    def main_account_cost_aga_vacation(self, main_account_cost_aga_vacation):
        """Sets the main_account_cost_aga_vacation of this CompanySalary.


        :param main_account_cost_aga_vacation: The main_account_cost_aga_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_cost_aga_vacation = main_account_cost_aga_vacation

    @property
    def wagetype_advance_payment(self):
        """Gets the wagetype_advance_payment of this CompanySalary.  # noqa: E501


        :return: The wagetype_advance_payment of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._wagetype_advance_payment

    @wagetype_advance_payment.setter
    def wagetype_advance_payment(self, wagetype_advance_payment):
        """Sets the wagetype_advance_payment of this CompanySalary.


        :param wagetype_advance_payment: The wagetype_advance_payment of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._wagetype_advance_payment = wagetype_advance_payment

    @property
    def wage_deduction_due_to_holiday(self):
        """Gets the wage_deduction_due_to_holiday of this CompanySalary.  # noqa: E501


        :return: The wage_deduction_due_to_holiday of this CompanySalary.  # noqa: E501
        :rtype: str
        """
        return self._wage_deduction_due_to_holiday

    @wage_deduction_due_to_holiday.setter
    def wage_deduction_due_to_holiday(self, wage_deduction_due_to_holiday):
        """Sets the wage_deduction_due_to_holiday of this CompanySalary.


        :param wage_deduction_due_to_holiday: The wage_deduction_due_to_holiday of this CompanySalary.  # noqa: E501
        :type: str
        """

        self._wage_deduction_due_to_holiday = wage_deduction_due_to_holiday

    @property
    def base_tax_free_organization(self):
        """Gets the base_tax_free_organization of this CompanySalary.  # noqa: E501


        :return: The base_tax_free_organization of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_tax_free_organization

    @base_tax_free_organization.setter
    def base_tax_free_organization(self, base_tax_free_organization):
        """Sets the base_tax_free_organization of this CompanySalary.


        :param base_tax_free_organization: The base_tax_free_organization of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_tax_free_organization = base_tax_free_organization

    @property
    def status_code(self):
        """Gets the status_code of this CompanySalary.  # noqa: E501


        :return: The status_code of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CompanySalary.


        :param status_code: The status_code of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this CompanySalary.  # noqa: E501


        :return: The deleted of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CompanySalary.


        :param deleted: The deleted of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def allow_over6_g(self):
        """Gets the allow_over6_g of this CompanySalary.  # noqa: E501


        :return: The allow_over6_g of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._allow_over6_g

    @allow_over6_g.setter
    def allow_over6_g(self, allow_over6_g):
        """Sets the allow_over6_g of this CompanySalary.


        :param allow_over6_g: The allow_over6_g of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._allow_over6_g = allow_over6_g

    @property
    def annual_statement_zip_report_id(self):
        """Gets the annual_statement_zip_report_id of this CompanySalary.  # noqa: E501


        :return: The annual_statement_zip_report_id of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._annual_statement_zip_report_id

    @annual_statement_zip_report_id.setter
    def annual_statement_zip_report_id(self, annual_statement_zip_report_id):
        """Sets the annual_statement_zip_report_id of this CompanySalary.


        :param annual_statement_zip_report_id: The annual_statement_zip_report_id of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._annual_statement_zip_report_id = annual_statement_zip_report_id

    @property
    def base_pay_as_you_earn_tax_on_pensions(self):
        """Gets the base_pay_as_you_earn_tax_on_pensions of this CompanySalary.  # noqa: E501


        :return: The base_pay_as_you_earn_tax_on_pensions of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_pay_as_you_earn_tax_on_pensions

    @base_pay_as_you_earn_tax_on_pensions.setter
    def base_pay_as_you_earn_tax_on_pensions(self, base_pay_as_you_earn_tax_on_pensions):
        """Sets the base_pay_as_you_earn_tax_on_pensions of this CompanySalary.


        :param base_pay_as_you_earn_tax_on_pensions: The base_pay_as_you_earn_tax_on_pensions of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_pay_as_you_earn_tax_on_pensions = base_pay_as_you_earn_tax_on_pensions

    @property
    def post_garnishment_to_tax_account(self):
        """Gets the post_garnishment_to_tax_account of this CompanySalary.  # noqa: E501


        :return: The post_garnishment_to_tax_account of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._post_garnishment_to_tax_account

    @post_garnishment_to_tax_account.setter
    def post_garnishment_to_tax_account(self, post_garnishment_to_tax_account):
        """Sets the post_garnishment_to_tax_account of this CompanySalary.


        :param post_garnishment_to_tax_account: The post_garnishment_to_tax_account of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._post_garnishment_to_tax_account = post_garnishment_to_tax_account

    @property
    def main_account_cost_financial(self):
        """Gets the main_account_cost_financial of this CompanySalary.  # noqa: E501


        :return: The main_account_cost_financial of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_cost_financial

    @main_account_cost_financial.setter
    def main_account_cost_financial(self, main_account_cost_financial):
        """Sets the main_account_cost_financial of this CompanySalary.


        :param main_account_cost_financial: The main_account_cost_financial of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_cost_financial = main_account_cost_financial

    @property
    def wagetype_advance_payment_auto(self):
        """Gets the wagetype_advance_payment_auto of this CompanySalary.  # noqa: E501


        :return: The wagetype_advance_payment_auto of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._wagetype_advance_payment_auto

    @wagetype_advance_payment_auto.setter
    def wagetype_advance_payment_auto(self, wagetype_advance_payment_auto):
        """Sets the wagetype_advance_payment_auto of this CompanySalary.


        :param wagetype_advance_payment_auto: The wagetype_advance_payment_auto of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._wagetype_advance_payment_auto = wagetype_advance_payment_auto

    @property
    def post_to_tax_draw(self):
        """Gets the post_to_tax_draw of this CompanySalary.  # noqa: E501


        :return: The post_to_tax_draw of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._post_to_tax_draw

    @post_to_tax_draw.setter
    def post_to_tax_draw(self, post_to_tax_draw):
        """Sets the post_to_tax_draw of this CompanySalary.


        :param post_to_tax_draw: The post_to_tax_draw of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._post_to_tax_draw = post_to_tax_draw

    @property
    def base_svalbard(self):
        """Gets the base_svalbard of this CompanySalary.  # noqa: E501


        :return: The base_svalbard of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_svalbard

    @base_svalbard.setter
    def base_svalbard(self, base_svalbard):
        """Sets the base_svalbard of this CompanySalary.


        :param base_svalbard: The base_svalbard of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_svalbard = base_svalbard

    @property
    def main_account_cost_aga(self):
        """Gets the main_account_cost_aga of this CompanySalary.  # noqa: E501


        :return: The main_account_cost_aga of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_cost_aga

    @main_account_cost_aga.setter
    def main_account_cost_aga(self, main_account_cost_aga):
        """Sets the main_account_cost_aga of this CompanySalary.


        :param main_account_cost_aga: The main_account_cost_aga of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_cost_aga = main_account_cost_aga

    @property
    def id(self):
        """Gets the id of this CompanySalary.  # noqa: E501


        :return: The id of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanySalary.


        :param id: The id of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def main_account_allocated_financial(self):
        """Gets the main_account_allocated_financial of this CompanySalary.  # noqa: E501


        :return: The main_account_allocated_financial of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_allocated_financial

    @main_account_allocated_financial.setter
    def main_account_allocated_financial(self, main_account_allocated_financial):
        """Sets the main_account_allocated_financial of this CompanySalary.


        :param main_account_allocated_financial: The main_account_allocated_financial of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_allocated_financial = main_account_allocated_financial

    @property
    def main_account_allocated_aga(self):
        """Gets the main_account_allocated_aga of this CompanySalary.  # noqa: E501


        :return: The main_account_allocated_aga of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_allocated_aga

    @main_account_allocated_aga.setter
    def main_account_allocated_aga(self, main_account_allocated_aga):
        """Sets the main_account_allocated_aga of this CompanySalary.


        :param main_account_allocated_aga: The main_account_allocated_aga of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_allocated_aga = main_account_allocated_aga

    @property
    def updated_by(self):
        """Gets the updated_by of this CompanySalary.  # noqa: E501


        :return: The updated_by of this CompanySalary.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this CompanySalary.


        :param updated_by: The updated_by of this CompanySalary.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def base_jan_mayen_and_bi_countries(self):
        """Gets the base_jan_mayen_and_bi_countries of this CompanySalary.  # noqa: E501


        :return: The base_jan_mayen_and_bi_countries of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._base_jan_mayen_and_bi_countries

    @base_jan_mayen_and_bi_countries.setter
    def base_jan_mayen_and_bi_countries(self, base_jan_mayen_and_bi_countries):
        """Sets the base_jan_mayen_and_bi_countries of this CompanySalary.


        :param base_jan_mayen_and_bi_countries: The base_jan_mayen_and_bi_countries of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._base_jan_mayen_and_bi_countries = base_jan_mayen_and_bi_countries

    @property
    def paycheck_zip_report_id(self):
        """Gets the paycheck_zip_report_id of this CompanySalary.  # noqa: E501


        :return: The paycheck_zip_report_id of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._paycheck_zip_report_id

    @paycheck_zip_report_id.setter
    def paycheck_zip_report_id(self, paycheck_zip_report_id):
        """Sets the paycheck_zip_report_id of this CompanySalary.


        :param paycheck_zip_report_id: The paycheck_zip_report_id of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._paycheck_zip_report_id = paycheck_zip_report_id

    @property
    def created_by(self):
        """Gets the created_by of this CompanySalary.  # noqa: E501


        :return: The created_by of this CompanySalary.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CompanySalary.


        :param created_by: The created_by of this CompanySalary.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def main_account_cost_financial_vacation(self):
        """Gets the main_account_cost_financial_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_cost_financial_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_cost_financial_vacation

    @main_account_cost_financial_vacation.setter
    def main_account_cost_financial_vacation(self, main_account_cost_financial_vacation):
        """Sets the main_account_cost_financial_vacation of this CompanySalary.


        :param main_account_cost_financial_vacation: The main_account_cost_financial_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_cost_financial_vacation = main_account_cost_financial_vacation

    @property
    def calculate_financial_tax(self):
        """Gets the calculate_financial_tax of this CompanySalary.  # noqa: E501


        :return: The calculate_financial_tax of this CompanySalary.  # noqa: E501
        :rtype: bool
        """
        return self._calculate_financial_tax

    @calculate_financial_tax.setter
    def calculate_financial_tax(self, calculate_financial_tax):
        """Sets the calculate_financial_tax of this CompanySalary.


        :param calculate_financial_tax: The calculate_financial_tax of this CompanySalary.  # noqa: E501
        :type: bool
        """

        self._calculate_financial_tax = calculate_financial_tax

    @property
    def main_account_allocated_aga_vacation(self):
        """Gets the main_account_allocated_aga_vacation of this CompanySalary.  # noqa: E501


        :return: The main_account_allocated_aga_vacation of this CompanySalary.  # noqa: E501
        :rtype: int
        """
        return self._main_account_allocated_aga_vacation

    @main_account_allocated_aga_vacation.setter
    def main_account_allocated_aga_vacation(self, main_account_allocated_aga_vacation):
        """Sets the main_account_allocated_aga_vacation of this CompanySalary.


        :param main_account_allocated_aga_vacation: The main_account_allocated_aga_vacation of this CompanySalary.  # noqa: E501
        :type: int
        """

        self._main_account_allocated_aga_vacation = main_account_allocated_aga_vacation

    @property
    def payment_interval(self):
        """Gets the payment_interval of this CompanySalary.  # noqa: E501


        :return: The payment_interval of this CompanySalary.  # noqa: E501
        :rtype: str
        """
        return self._payment_interval

    @payment_interval.setter
    def payment_interval(self, payment_interval):
        """Sets the payment_interval of this CompanySalary.


        :param payment_interval: The payment_interval of this CompanySalary.  # noqa: E501
        :type: str
        """

        self._payment_interval = payment_interval

    @property
    def custom_values(self):
        """Gets the custom_values of this CompanySalary.  # noqa: E501


        :return: The custom_values of this CompanySalary.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this CompanySalary.


        :param custom_values: The custom_values of this CompanySalary.  # noqa: E501
        :type: CustomValues
        """

        self._custom_values = custom_values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CompanySalary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompanySalary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
