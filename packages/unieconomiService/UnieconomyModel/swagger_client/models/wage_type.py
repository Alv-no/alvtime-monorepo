# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WageType(object):
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
        'account_number': 'int',
        'postnr': 'str',
        'base_div3': 'bool',
        'base_vacation': 'bool',
        'description': 'str',
        'valid_year': 'int',
        'fixed_salary_holiday_deduction': 'bool',
        'get_rate_from': 'str',
        'standard_wage_type_for': 'str',
        'ratetype_column': 'str',
        'limit_type': 'str',
        'base_payment': 'bool',
        'status_code': 'int',
        'deleted': 'bool',
        'income_type': 'str',
        'limit_wage_type_number': 'int',
        'days_on_board': 'bool',
        'system_required_wage_type': 'int',
        'base_div2': 'bool',
        'account_number_balance': 'int',
        'no_number_of_hours': 'bool',
        'hide_from_paycheck': 'bool',
        'benefit': 'str',
        'special_tax_and_contributions_rule': 'str',
        'id': 'int',
        'base_employment_tax': 'bool',
        'updated_by': 'str',
        'special_tax_handling': 'str',
        'supplement_package': 'str',
        'created_by': 'str',
        'wage_type_number': 'int',
        'special_aga_rule': 'str',
        'systemtype': 'str',
        'wage_type_name': 'str',
        'taxtype': 'str',
        'supplementary_informations': 'list[WageTypeSupplement]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'account_number': 'AccountNumber',
        'postnr': 'Postnr',
        'base_div3': 'Base_div3',
        'base_vacation': 'Base_Vacation',
        'description': 'Description',
        'valid_year': 'ValidYear',
        'fixed_salary_holiday_deduction': 'FixedSalaryHolidayDeduction',
        'get_rate_from': 'GetRateFrom',
        'standard_wage_type_for': 'StandardWageTypeFor',
        'ratetype_column': 'RatetypeColumn',
        'limit_type': 'Limit_type',
        'base_payment': 'Base_Payment',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'income_type': 'IncomeType',
        'limit_wage_type_number': 'Limit_WageTypeNumber',
        'days_on_board': 'DaysOnBoard',
        'system_required_wage_type': 'SystemRequiredWageType',
        'base_div2': 'Base_div2',
        'account_number_balance': 'AccountNumber_balance',
        'no_number_of_hours': 'NoNumberOfHours',
        'hide_from_paycheck': 'HideFromPaycheck',
        'benefit': 'Benefit',
        'special_tax_and_contributions_rule': 'SpecialTaxAndContributionsRule',
        'id': 'ID',
        'base_employment_tax': 'Base_EmploymentTax',
        'updated_by': 'UpdatedBy',
        'special_tax_handling': 'SpecialTaxHandling',
        'supplement_package': 'SupplementPackage',
        'created_by': 'CreatedBy',
        'wage_type_number': 'WageTypeNumber',
        'special_aga_rule': 'SpecialAgaRule',
        'systemtype': 'Systemtype',
        'wage_type_name': 'WageTypeName',
        'taxtype': 'taxtype',
        'supplementary_informations': 'SupplementaryInformations',
        'custom_values': 'CustomValues'
    }

    def __init__(self, account_number=None, postnr=None, base_div3=None, base_vacation=None, description=None, valid_year=None, fixed_salary_holiday_deduction=None, get_rate_from=None, standard_wage_type_for=None, ratetype_column=None, limit_type=None, base_payment=None, status_code=None, deleted=None, income_type=None, limit_wage_type_number=None, days_on_board=None, system_required_wage_type=None, base_div2=None, account_number_balance=None, no_number_of_hours=None, hide_from_paycheck=None, benefit=None, special_tax_and_contributions_rule=None, id=None, base_employment_tax=None, updated_by=None, special_tax_handling=None, supplement_package=None, created_by=None, wage_type_number=None, special_aga_rule=None, systemtype=None, wage_type_name=None, taxtype=None, supplementary_informations=None, custom_values=None):  # noqa: E501
        """WageType - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._postnr = None
        self._base_div3 = None
        self._base_vacation = None
        self._description = None
        self._valid_year = None
        self._fixed_salary_holiday_deduction = None
        self._get_rate_from = None
        self._standard_wage_type_for = None
        self._ratetype_column = None
        self._limit_type = None
        self._base_payment = None
        self._status_code = None
        self._deleted = None
        self._income_type = None
        self._limit_wage_type_number = None
        self._days_on_board = None
        self._system_required_wage_type = None
        self._base_div2 = None
        self._account_number_balance = None
        self._no_number_of_hours = None
        self._hide_from_paycheck = None
        self._benefit = None
        self._special_tax_and_contributions_rule = None
        self._id = None
        self._base_employment_tax = None
        self._updated_by = None
        self._special_tax_handling = None
        self._supplement_package = None
        self._created_by = None
        self._wage_type_number = None
        self._special_aga_rule = None
        self._systemtype = None
        self._wage_type_name = None
        self._taxtype = None
        self._supplementary_informations = None
        self._custom_values = None
        self.discriminator = None
        if account_number is not None:
            self.account_number = account_number
        if postnr is not None:
            self.postnr = postnr
        if base_div3 is not None:
            self.base_div3 = base_div3
        if base_vacation is not None:
            self.base_vacation = base_vacation
        if description is not None:
            self.description = description
        if valid_year is not None:
            self.valid_year = valid_year
        if fixed_salary_holiday_deduction is not None:
            self.fixed_salary_holiday_deduction = fixed_salary_holiday_deduction
        if get_rate_from is not None:
            self.get_rate_from = get_rate_from
        if standard_wage_type_for is not None:
            self.standard_wage_type_for = standard_wage_type_for
        if ratetype_column is not None:
            self.ratetype_column = ratetype_column
        if limit_type is not None:
            self.limit_type = limit_type
        if base_payment is not None:
            self.base_payment = base_payment
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if income_type is not None:
            self.income_type = income_type
        if limit_wage_type_number is not None:
            self.limit_wage_type_number = limit_wage_type_number
        if days_on_board is not None:
            self.days_on_board = days_on_board
        if system_required_wage_type is not None:
            self.system_required_wage_type = system_required_wage_type
        if base_div2 is not None:
            self.base_div2 = base_div2
        if account_number_balance is not None:
            self.account_number_balance = account_number_balance
        if no_number_of_hours is not None:
            self.no_number_of_hours = no_number_of_hours
        if hide_from_paycheck is not None:
            self.hide_from_paycheck = hide_from_paycheck
        if benefit is not None:
            self.benefit = benefit
        if special_tax_and_contributions_rule is not None:
            self.special_tax_and_contributions_rule = special_tax_and_contributions_rule
        if id is not None:
            self.id = id
        if base_employment_tax is not None:
            self.base_employment_tax = base_employment_tax
        if updated_by is not None:
            self.updated_by = updated_by
        if special_tax_handling is not None:
            self.special_tax_handling = special_tax_handling
        if supplement_package is not None:
            self.supplement_package = supplement_package
        if created_by is not None:
            self.created_by = created_by
        if wage_type_number is not None:
            self.wage_type_number = wage_type_number
        if special_aga_rule is not None:
            self.special_aga_rule = special_aga_rule
        if systemtype is not None:
            self.systemtype = systemtype
        if wage_type_name is not None:
            self.wage_type_name = wage_type_name
        if taxtype is not None:
            self.taxtype = taxtype
        if supplementary_informations is not None:
            self.supplementary_informations = supplementary_informations
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def account_number(self):
        """Gets the account_number of this WageType.  # noqa: E501


        :return: The account_number of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this WageType.


        :param account_number: The account_number of this WageType.  # noqa: E501
        :type: int
        """

        self._account_number = account_number

    @property
    def postnr(self):
        """Gets the postnr of this WageType.  # noqa: E501


        :return: The postnr of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._postnr

    @postnr.setter
    def postnr(self, postnr):
        """Sets the postnr of this WageType.


        :param postnr: The postnr of this WageType.  # noqa: E501
        :type: str
        """

        self._postnr = postnr

    @property
    def base_div3(self):
        """Gets the base_div3 of this WageType.  # noqa: E501


        :return: The base_div3 of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._base_div3

    @base_div3.setter
    def base_div3(self, base_div3):
        """Sets the base_div3 of this WageType.


        :param base_div3: The base_div3 of this WageType.  # noqa: E501
        :type: bool
        """

        self._base_div3 = base_div3

    @property
    def base_vacation(self):
        """Gets the base_vacation of this WageType.  # noqa: E501


        :return: The base_vacation of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._base_vacation

    @base_vacation.setter
    def base_vacation(self, base_vacation):
        """Sets the base_vacation of this WageType.


        :param base_vacation: The base_vacation of this WageType.  # noqa: E501
        :type: bool
        """

        self._base_vacation = base_vacation

    @property
    def description(self):
        """Gets the description of this WageType.  # noqa: E501


        :return: The description of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WageType.


        :param description: The description of this WageType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def valid_year(self):
        """Gets the valid_year of this WageType.  # noqa: E501


        :return: The valid_year of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._valid_year

    @valid_year.setter
    def valid_year(self, valid_year):
        """Sets the valid_year of this WageType.


        :param valid_year: The valid_year of this WageType.  # noqa: E501
        :type: int
        """

        self._valid_year = valid_year

    @property
    def fixed_salary_holiday_deduction(self):
        """Gets the fixed_salary_holiday_deduction of this WageType.  # noqa: E501


        :return: The fixed_salary_holiday_deduction of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_salary_holiday_deduction

    @fixed_salary_holiday_deduction.setter
    def fixed_salary_holiday_deduction(self, fixed_salary_holiday_deduction):
        """Sets the fixed_salary_holiday_deduction of this WageType.


        :param fixed_salary_holiday_deduction: The fixed_salary_holiday_deduction of this WageType.  # noqa: E501
        :type: bool
        """

        self._fixed_salary_holiday_deduction = fixed_salary_holiday_deduction

    @property
    def get_rate_from(self):
        """Gets the get_rate_from of this WageType.  # noqa: E501


        :return: The get_rate_from of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._get_rate_from

    @get_rate_from.setter
    def get_rate_from(self, get_rate_from):
        """Sets the get_rate_from of this WageType.


        :param get_rate_from: The get_rate_from of this WageType.  # noqa: E501
        :type: str
        """

        self._get_rate_from = get_rate_from

    @property
    def standard_wage_type_for(self):
        """Gets the standard_wage_type_for of this WageType.  # noqa: E501


        :return: The standard_wage_type_for of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._standard_wage_type_for

    @standard_wage_type_for.setter
    def standard_wage_type_for(self, standard_wage_type_for):
        """Sets the standard_wage_type_for of this WageType.


        :param standard_wage_type_for: The standard_wage_type_for of this WageType.  # noqa: E501
        :type: str
        """

        self._standard_wage_type_for = standard_wage_type_for

    @property
    def ratetype_column(self):
        """Gets the ratetype_column of this WageType.  # noqa: E501


        :return: The ratetype_column of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._ratetype_column

    @ratetype_column.setter
    def ratetype_column(self, ratetype_column):
        """Sets the ratetype_column of this WageType.


        :param ratetype_column: The ratetype_column of this WageType.  # noqa: E501
        :type: str
        """

        self._ratetype_column = ratetype_column

    @property
    def limit_type(self):
        """Gets the limit_type of this WageType.  # noqa: E501


        :return: The limit_type of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        """Sets the limit_type of this WageType.


        :param limit_type: The limit_type of this WageType.  # noqa: E501
        :type: str
        """

        self._limit_type = limit_type

    @property
    def base_payment(self):
        """Gets the base_payment of this WageType.  # noqa: E501


        :return: The base_payment of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._base_payment

    @base_payment.setter
    def base_payment(self, base_payment):
        """Sets the base_payment of this WageType.


        :param base_payment: The base_payment of this WageType.  # noqa: E501
        :type: bool
        """

        self._base_payment = base_payment

    @property
    def status_code(self):
        """Gets the status_code of this WageType.  # noqa: E501


        :return: The status_code of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this WageType.


        :param status_code: The status_code of this WageType.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this WageType.  # noqa: E501


        :return: The deleted of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this WageType.


        :param deleted: The deleted of this WageType.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def income_type(self):
        """Gets the income_type of this WageType.  # noqa: E501


        :return: The income_type of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._income_type

    @income_type.setter
    def income_type(self, income_type):
        """Sets the income_type of this WageType.


        :param income_type: The income_type of this WageType.  # noqa: E501
        :type: str
        """

        self._income_type = income_type

    @property
    def limit_wage_type_number(self):
        """Gets the limit_wage_type_number of this WageType.  # noqa: E501


        :return: The limit_wage_type_number of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._limit_wage_type_number

    @limit_wage_type_number.setter
    def limit_wage_type_number(self, limit_wage_type_number):
        """Sets the limit_wage_type_number of this WageType.


        :param limit_wage_type_number: The limit_wage_type_number of this WageType.  # noqa: E501
        :type: int
        """

        self._limit_wage_type_number = limit_wage_type_number

    @property
    def days_on_board(self):
        """Gets the days_on_board of this WageType.  # noqa: E501


        :return: The days_on_board of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._days_on_board

    @days_on_board.setter
    def days_on_board(self, days_on_board):
        """Sets the days_on_board of this WageType.


        :param days_on_board: The days_on_board of this WageType.  # noqa: E501
        :type: bool
        """

        self._days_on_board = days_on_board

    @property
    def system_required_wage_type(self):
        """Gets the system_required_wage_type of this WageType.  # noqa: E501


        :return: The system_required_wage_type of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._system_required_wage_type

    @system_required_wage_type.setter
    def system_required_wage_type(self, system_required_wage_type):
        """Sets the system_required_wage_type of this WageType.


        :param system_required_wage_type: The system_required_wage_type of this WageType.  # noqa: E501
        :type: int
        """

        self._system_required_wage_type = system_required_wage_type

    @property
    def base_div2(self):
        """Gets the base_div2 of this WageType.  # noqa: E501


        :return: The base_div2 of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._base_div2

    @base_div2.setter
    def base_div2(self, base_div2):
        """Sets the base_div2 of this WageType.


        :param base_div2: The base_div2 of this WageType.  # noqa: E501
        :type: bool
        """

        self._base_div2 = base_div2

    @property
    def account_number_balance(self):
        """Gets the account_number_balance of this WageType.  # noqa: E501


        :return: The account_number_balance of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._account_number_balance

    @account_number_balance.setter
    def account_number_balance(self, account_number_balance):
        """Sets the account_number_balance of this WageType.


        :param account_number_balance: The account_number_balance of this WageType.  # noqa: E501
        :type: int
        """

        self._account_number_balance = account_number_balance

    @property
    def no_number_of_hours(self):
        """Gets the no_number_of_hours of this WageType.  # noqa: E501


        :return: The no_number_of_hours of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._no_number_of_hours

    @no_number_of_hours.setter
    def no_number_of_hours(self, no_number_of_hours):
        """Sets the no_number_of_hours of this WageType.


        :param no_number_of_hours: The no_number_of_hours of this WageType.  # noqa: E501
        :type: bool
        """

        self._no_number_of_hours = no_number_of_hours

    @property
    def hide_from_paycheck(self):
        """Gets the hide_from_paycheck of this WageType.  # noqa: E501


        :return: The hide_from_paycheck of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_paycheck

    @hide_from_paycheck.setter
    def hide_from_paycheck(self, hide_from_paycheck):
        """Sets the hide_from_paycheck of this WageType.


        :param hide_from_paycheck: The hide_from_paycheck of this WageType.  # noqa: E501
        :type: bool
        """

        self._hide_from_paycheck = hide_from_paycheck

    @property
    def benefit(self):
        """Gets the benefit of this WageType.  # noqa: E501


        :return: The benefit of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._benefit

    @benefit.setter
    def benefit(self, benefit):
        """Sets the benefit of this WageType.


        :param benefit: The benefit of this WageType.  # noqa: E501
        :type: str
        """

        self._benefit = benefit

    @property
    def special_tax_and_contributions_rule(self):
        """Gets the special_tax_and_contributions_rule of this WageType.  # noqa: E501


        :return: The special_tax_and_contributions_rule of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._special_tax_and_contributions_rule

    @special_tax_and_contributions_rule.setter
    def special_tax_and_contributions_rule(self, special_tax_and_contributions_rule):
        """Sets the special_tax_and_contributions_rule of this WageType.


        :param special_tax_and_contributions_rule: The special_tax_and_contributions_rule of this WageType.  # noqa: E501
        :type: str
        """

        self._special_tax_and_contributions_rule = special_tax_and_contributions_rule

    @property
    def id(self):
        """Gets the id of this WageType.  # noqa: E501


        :return: The id of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WageType.


        :param id: The id of this WageType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def base_employment_tax(self):
        """Gets the base_employment_tax of this WageType.  # noqa: E501


        :return: The base_employment_tax of this WageType.  # noqa: E501
        :rtype: bool
        """
        return self._base_employment_tax

    @base_employment_tax.setter
    def base_employment_tax(self, base_employment_tax):
        """Sets the base_employment_tax of this WageType.


        :param base_employment_tax: The base_employment_tax of this WageType.  # noqa: E501
        :type: bool
        """

        self._base_employment_tax = base_employment_tax

    @property
    def updated_by(self):
        """Gets the updated_by of this WageType.  # noqa: E501


        :return: The updated_by of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this WageType.


        :param updated_by: The updated_by of this WageType.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def special_tax_handling(self):
        """Gets the special_tax_handling of this WageType.  # noqa: E501


        :return: The special_tax_handling of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._special_tax_handling

    @special_tax_handling.setter
    def special_tax_handling(self, special_tax_handling):
        """Sets the special_tax_handling of this WageType.


        :param special_tax_handling: The special_tax_handling of this WageType.  # noqa: E501
        :type: str
        """

        self._special_tax_handling = special_tax_handling

    @property
    def supplement_package(self):
        """Gets the supplement_package of this WageType.  # noqa: E501


        :return: The supplement_package of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._supplement_package

    @supplement_package.setter
    def supplement_package(self, supplement_package):
        """Sets the supplement_package of this WageType.


        :param supplement_package: The supplement_package of this WageType.  # noqa: E501
        :type: str
        """

        self._supplement_package = supplement_package

    @property
    def created_by(self):
        """Gets the created_by of this WageType.  # noqa: E501


        :return: The created_by of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WageType.


        :param created_by: The created_by of this WageType.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def wage_type_number(self):
        """Gets the wage_type_number of this WageType.  # noqa: E501


        :return: The wage_type_number of this WageType.  # noqa: E501
        :rtype: int
        """
        return self._wage_type_number

    @wage_type_number.setter
    def wage_type_number(self, wage_type_number):
        """Sets the wage_type_number of this WageType.


        :param wage_type_number: The wage_type_number of this WageType.  # noqa: E501
        :type: int
        """

        self._wage_type_number = wage_type_number

    @property
    def special_aga_rule(self):
        """Gets the special_aga_rule of this WageType.  # noqa: E501


        :return: The special_aga_rule of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._special_aga_rule

    @special_aga_rule.setter
    def special_aga_rule(self, special_aga_rule):
        """Sets the special_aga_rule of this WageType.


        :param special_aga_rule: The special_aga_rule of this WageType.  # noqa: E501
        :type: str
        """

        self._special_aga_rule = special_aga_rule

    @property
    def systemtype(self):
        """Gets the systemtype of this WageType.  # noqa: E501


        :return: The systemtype of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._systemtype

    @systemtype.setter
    def systemtype(self, systemtype):
        """Sets the systemtype of this WageType.


        :param systemtype: The systemtype of this WageType.  # noqa: E501
        :type: str
        """

        self._systemtype = systemtype

    @property
    def wage_type_name(self):
        """Gets the wage_type_name of this WageType.  # noqa: E501


        :return: The wage_type_name of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._wage_type_name

    @wage_type_name.setter
    def wage_type_name(self, wage_type_name):
        """Sets the wage_type_name of this WageType.


        :param wage_type_name: The wage_type_name of this WageType.  # noqa: E501
        :type: str
        """

        self._wage_type_name = wage_type_name

    @property
    def taxtype(self):
        """Gets the taxtype of this WageType.  # noqa: E501


        :return: The taxtype of this WageType.  # noqa: E501
        :rtype: str
        """
        return self._taxtype

    @taxtype.setter
    def taxtype(self, taxtype):
        """Sets the taxtype of this WageType.


        :param taxtype: The taxtype of this WageType.  # noqa: E501
        :type: str
        """

        self._taxtype = taxtype

    @property
    def supplementary_informations(self):
        """Gets the supplementary_informations of this WageType.  # noqa: E501


        :return: The supplementary_informations of this WageType.  # noqa: E501
        :rtype: list[WageTypeSupplement]
        """
        return self._supplementary_informations

    @supplementary_informations.setter
    def supplementary_informations(self, supplementary_informations):
        """Sets the supplementary_informations of this WageType.


        :param supplementary_informations: The supplementary_informations of this WageType.  # noqa: E501
        :type: list[WageTypeSupplement]
        """

        self._supplementary_informations = supplementary_informations

    @property
    def custom_values(self):
        """Gets the custom_values of this WageType.  # noqa: E501


        :return: The custom_values of this WageType.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this WageType.


        :param custom_values: The custom_values of this WageType.  # noqa: E501
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
        if issubclass(WageType, dict):
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
        if not isinstance(other, WageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
