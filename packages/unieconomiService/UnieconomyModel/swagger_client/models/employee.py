# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Employee(object):
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
        'user_id': 'int',
        'business_relation_id': 'int',
        'include_otp_until_year': 'int',
        'include_otp_until_month': 'int',
        'employee_language_id': 'int',
        'active': 'bool',
        'otp_export': 'bool',
        'internasjonal_id_type': 'str',
        'free_text': 'str',
        'municipality_no': 'str',
        'status_code': 'int',
        'deleted': 'bool',
        'photo_id': 'int',
        'internasjonal_id_country': 'str',
        'employee_number': 'int',
        'type_of_payment_otp': 'str',
        'otp_status': 'str',
        'international_id': 'str',
        'id': 'int',
        'social_security_number': 'str',
        'updated_by': 'str',
        'sex': 'str',
        'created_by': 'str',
        'sub_entity_id': 'int',
        'foreign_worker': 'str',
        'payment_interval': 'str',
        'business_relation_info': 'BusinessRelation',
        'employments': 'list[Employment]',
        'vacation_rate_employees': 'list[VacationRateEmployee]',
        'tax_cards': 'list[EmployeeTaxCard]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'user_id': 'UserID',
        'business_relation_id': 'BusinessRelationID',
        'include_otp_until_year': 'IncludeOtpUntilYear',
        'include_otp_until_month': 'IncludeOtpUntilMonth',
        'employee_language_id': 'EmployeeLanguageID',
        'active': 'Active',
        'otp_export': 'OtpExport',
        'internasjonal_id_type': 'InternasjonalIDType',
        'free_text': 'FreeText',
        'municipality_no': 'MunicipalityNo',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'photo_id': 'PhotoID',
        'internasjonal_id_country': 'InternasjonalIDCountry',
        'employee_number': 'EmployeeNumber',
        'type_of_payment_otp': 'TypeOfPaymentOtp',
        'otp_status': 'OtpStatus',
        'international_id': 'InternationalID',
        'id': 'ID',
        'social_security_number': 'SocialSecurityNumber',
        'updated_by': 'UpdatedBy',
        'sex': 'Sex',
        'created_by': 'CreatedBy',
        'sub_entity_id': 'SubEntityID',
        'foreign_worker': 'ForeignWorker',
        'payment_interval': 'PaymentInterval',
        'business_relation_info': 'BusinessRelationInfo',
        'employments': 'Employments',
        'vacation_rate_employees': 'VacationRateEmployees',
        'tax_cards': 'TaxCards',
        'custom_values': 'CustomValues'
    }

    def __init__(self, user_id=None, business_relation_id=None, include_otp_until_year=None, include_otp_until_month=None, employee_language_id=None, active=None, otp_export=None, internasjonal_id_type=None, free_text=None, municipality_no=None, status_code=None, deleted=None, photo_id=None, internasjonal_id_country=None, employee_number=None, type_of_payment_otp=None, otp_status=None, international_id=None, id=None, social_security_number=None, updated_by=None, sex=None, created_by=None, sub_entity_id=None, foreign_worker=None, payment_interval=None, business_relation_info=None, employments=None, vacation_rate_employees=None, tax_cards=None, custom_values=None):  # noqa: E501
        """Employee - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._business_relation_id = None
        self._include_otp_until_year = None
        self._include_otp_until_month = None
        self._employee_language_id = None
        self._active = None
        self._otp_export = None
        self._internasjonal_id_type = None
        self._free_text = None
        self._municipality_no = None
        self._status_code = None
        self._deleted = None
        self._photo_id = None
        self._internasjonal_id_country = None
        self._employee_number = None
        self._type_of_payment_otp = None
        self._otp_status = None
        self._international_id = None
        self._id = None
        self._social_security_number = None
        self._updated_by = None
        self._sex = None
        self._created_by = None
        self._sub_entity_id = None
        self._foreign_worker = None
        self._payment_interval = None
        self._business_relation_info = None
        self._employments = None
        self._vacation_rate_employees = None
        self._tax_cards = None
        self._custom_values = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if business_relation_id is not None:
            self.business_relation_id = business_relation_id
        if include_otp_until_year is not None:
            self.include_otp_until_year = include_otp_until_year
        if include_otp_until_month is not None:
            self.include_otp_until_month = include_otp_until_month
        if employee_language_id is not None:
            self.employee_language_id = employee_language_id
        if active is not None:
            self.active = active
        if otp_export is not None:
            self.otp_export = otp_export
        if internasjonal_id_type is not None:
            self.internasjonal_id_type = internasjonal_id_type
        if free_text is not None:
            self.free_text = free_text
        if municipality_no is not None:
            self.municipality_no = municipality_no
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if photo_id is not None:
            self.photo_id = photo_id
        if internasjonal_id_country is not None:
            self.internasjonal_id_country = internasjonal_id_country
        if employee_number is not None:
            self.employee_number = employee_number
        if type_of_payment_otp is not None:
            self.type_of_payment_otp = type_of_payment_otp
        if otp_status is not None:
            self.otp_status = otp_status
        if international_id is not None:
            self.international_id = international_id
        if id is not None:
            self.id = id
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if updated_by is not None:
            self.updated_by = updated_by
        if sex is not None:
            self.sex = sex
        if created_by is not None:
            self.created_by = created_by
        if sub_entity_id is not None:
            self.sub_entity_id = sub_entity_id
        if foreign_worker is not None:
            self.foreign_worker = foreign_worker
        if payment_interval is not None:
            self.payment_interval = payment_interval
        if business_relation_info is not None:
            self.business_relation_info = business_relation_info
        if employments is not None:
            self.employments = employments
        if vacation_rate_employees is not None:
            self.vacation_rate_employees = vacation_rate_employees
        if tax_cards is not None:
            self.tax_cards = tax_cards
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def user_id(self):
        """Gets the user_id of this Employee.  # noqa: E501


        :return: The user_id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Employee.


        :param user_id: The user_id of this Employee.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def business_relation_id(self):
        """Gets the business_relation_id of this Employee.  # noqa: E501


        :return: The business_relation_id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._business_relation_id

    @business_relation_id.setter
    def business_relation_id(self, business_relation_id):
        """Sets the business_relation_id of this Employee.


        :param business_relation_id: The business_relation_id of this Employee.  # noqa: E501
        :type: int
        """

        self._business_relation_id = business_relation_id

    @property
    def include_otp_until_year(self):
        """Gets the include_otp_until_year of this Employee.  # noqa: E501


        :return: The include_otp_until_year of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._include_otp_until_year

    @include_otp_until_year.setter
    def include_otp_until_year(self, include_otp_until_year):
        """Sets the include_otp_until_year of this Employee.


        :param include_otp_until_year: The include_otp_until_year of this Employee.  # noqa: E501
        :type: int
        """

        self._include_otp_until_year = include_otp_until_year

    @property
    def include_otp_until_month(self):
        """Gets the include_otp_until_month of this Employee.  # noqa: E501


        :return: The include_otp_until_month of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._include_otp_until_month

    @include_otp_until_month.setter
    def include_otp_until_month(self, include_otp_until_month):
        """Sets the include_otp_until_month of this Employee.


        :param include_otp_until_month: The include_otp_until_month of this Employee.  # noqa: E501
        :type: int
        """

        self._include_otp_until_month = include_otp_until_month

    @property
    def employee_language_id(self):
        """Gets the employee_language_id of this Employee.  # noqa: E501


        :return: The employee_language_id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._employee_language_id

    @employee_language_id.setter
    def employee_language_id(self, employee_language_id):
        """Sets the employee_language_id of this Employee.


        :param employee_language_id: The employee_language_id of this Employee.  # noqa: E501
        :type: int
        """

        self._employee_language_id = employee_language_id

    @property
    def active(self):
        """Gets the active of this Employee.  # noqa: E501


        :return: The active of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Employee.


        :param active: The active of this Employee.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def otp_export(self):
        """Gets the otp_export of this Employee.  # noqa: E501


        :return: The otp_export of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._otp_export

    @otp_export.setter
    def otp_export(self, otp_export):
        """Sets the otp_export of this Employee.


        :param otp_export: The otp_export of this Employee.  # noqa: E501
        :type: bool
        """

        self._otp_export = otp_export

    @property
    def internasjonal_id_type(self):
        """Gets the internasjonal_id_type of this Employee.  # noqa: E501


        :return: The internasjonal_id_type of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._internasjonal_id_type

    @internasjonal_id_type.setter
    def internasjonal_id_type(self, internasjonal_id_type):
        """Sets the internasjonal_id_type of this Employee.


        :param internasjonal_id_type: The internasjonal_id_type of this Employee.  # noqa: E501
        :type: str
        """

        self._internasjonal_id_type = internasjonal_id_type

    @property
    def free_text(self):
        """Gets the free_text of this Employee.  # noqa: E501


        :return: The free_text of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._free_text

    @free_text.setter
    def free_text(self, free_text):
        """Sets the free_text of this Employee.


        :param free_text: The free_text of this Employee.  # noqa: E501
        :type: str
        """

        self._free_text = free_text

    @property
    def municipality_no(self):
        """Gets the municipality_no of this Employee.  # noqa: E501


        :return: The municipality_no of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._municipality_no

    @municipality_no.setter
    def municipality_no(self, municipality_no):
        """Sets the municipality_no of this Employee.


        :param municipality_no: The municipality_no of this Employee.  # noqa: E501
        :type: str
        """

        self._municipality_no = municipality_no

    @property
    def status_code(self):
        """Gets the status_code of this Employee.  # noqa: E501


        :return: The status_code of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Employee.


        :param status_code: The status_code of this Employee.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this Employee.  # noqa: E501


        :return: The deleted of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Employee.


        :param deleted: The deleted of this Employee.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def photo_id(self):
        """Gets the photo_id of this Employee.  # noqa: E501


        :return: The photo_id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._photo_id

    @photo_id.setter
    def photo_id(self, photo_id):
        """Sets the photo_id of this Employee.


        :param photo_id: The photo_id of this Employee.  # noqa: E501
        :type: int
        """

        self._photo_id = photo_id

    @property
    def internasjonal_id_country(self):
        """Gets the internasjonal_id_country of this Employee.  # noqa: E501


        :return: The internasjonal_id_country of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._internasjonal_id_country

    @internasjonal_id_country.setter
    def internasjonal_id_country(self, internasjonal_id_country):
        """Sets the internasjonal_id_country of this Employee.


        :param internasjonal_id_country: The internasjonal_id_country of this Employee.  # noqa: E501
        :type: str
        """

        self._internasjonal_id_country = internasjonal_id_country

    @property
    def employee_number(self):
        """Gets the employee_number of this Employee.  # noqa: E501


        :return: The employee_number of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this Employee.


        :param employee_number: The employee_number of this Employee.  # noqa: E501
        :type: int
        """

        self._employee_number = employee_number

    @property
    def type_of_payment_otp(self):
        """Gets the type_of_payment_otp of this Employee.  # noqa: E501


        :return: The type_of_payment_otp of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._type_of_payment_otp

    @type_of_payment_otp.setter
    def type_of_payment_otp(self, type_of_payment_otp):
        """Sets the type_of_payment_otp of this Employee.


        :param type_of_payment_otp: The type_of_payment_otp of this Employee.  # noqa: E501
        :type: str
        """

        self._type_of_payment_otp = type_of_payment_otp

    @property
    def otp_status(self):
        """Gets the otp_status of this Employee.  # noqa: E501


        :return: The otp_status of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._otp_status

    @otp_status.setter
    def otp_status(self, otp_status):
        """Sets the otp_status of this Employee.


        :param otp_status: The otp_status of this Employee.  # noqa: E501
        :type: str
        """

        self._otp_status = otp_status

    @property
    def international_id(self):
        """Gets the international_id of this Employee.  # noqa: E501


        :return: The international_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._international_id

    @international_id.setter
    def international_id(self, international_id):
        """Sets the international_id of this Employee.


        :param international_id: The international_id of this Employee.  # noqa: E501
        :type: str
        """

        self._international_id = international_id

    @property
    def id(self):
        """Gets the id of this Employee.  # noqa: E501


        :return: The id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Employee.


        :param id: The id of this Employee.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def social_security_number(self):
        """Gets the social_security_number of this Employee.  # noqa: E501


        :return: The social_security_number of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this Employee.


        :param social_security_number: The social_security_number of this Employee.  # noqa: E501
        :type: str
        """

        self._social_security_number = social_security_number

    @property
    def updated_by(self):
        """Gets the updated_by of this Employee.  # noqa: E501


        :return: The updated_by of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Employee.


        :param updated_by: The updated_by of this Employee.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def sex(self):
        """Gets the sex of this Employee.  # noqa: E501


        :return: The sex of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this Employee.


        :param sex: The sex of this Employee.  # noqa: E501
        :type: str
        """

        self._sex = sex

    @property
    def created_by(self):
        """Gets the created_by of this Employee.  # noqa: E501


        :return: The created_by of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Employee.


        :param created_by: The created_by of this Employee.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def sub_entity_id(self):
        """Gets the sub_entity_id of this Employee.  # noqa: E501


        :return: The sub_entity_id of this Employee.  # noqa: E501
        :rtype: int
        """
        return self._sub_entity_id

    @sub_entity_id.setter
    def sub_entity_id(self, sub_entity_id):
        """Sets the sub_entity_id of this Employee.


        :param sub_entity_id: The sub_entity_id of this Employee.  # noqa: E501
        :type: int
        """

        self._sub_entity_id = sub_entity_id

    @property
    def foreign_worker(self):
        """Gets the foreign_worker of this Employee.  # noqa: E501


        :return: The foreign_worker of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._foreign_worker

    @foreign_worker.setter
    def foreign_worker(self, foreign_worker):
        """Sets the foreign_worker of this Employee.


        :param foreign_worker: The foreign_worker of this Employee.  # noqa: E501
        :type: str
        """

        self._foreign_worker = foreign_worker

    @property
    def payment_interval(self):
        """Gets the payment_interval of this Employee.  # noqa: E501


        :return: The payment_interval of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._payment_interval

    @payment_interval.setter
    def payment_interval(self, payment_interval):
        """Sets the payment_interval of this Employee.


        :param payment_interval: The payment_interval of this Employee.  # noqa: E501
        :type: str
        """

        self._payment_interval = payment_interval

    @property
    def business_relation_info(self):
        """Gets the business_relation_info of this Employee.  # noqa: E501


        :return: The business_relation_info of this Employee.  # noqa: E501
        :rtype: BusinessRelation
        """
        return self._business_relation_info

    @business_relation_info.setter
    def business_relation_info(self, business_relation_info):
        """Sets the business_relation_info of this Employee.


        :param business_relation_info: The business_relation_info of this Employee.  # noqa: E501
        :type: BusinessRelation
        """

        self._business_relation_info = business_relation_info

    @property
    def employments(self):
        """Gets the employments of this Employee.  # noqa: E501


        :return: The employments of this Employee.  # noqa: E501
        :rtype: list[Employment]
        """
        return self._employments

    @employments.setter
    def employments(self, employments):
        """Sets the employments of this Employee.


        :param employments: The employments of this Employee.  # noqa: E501
        :type: list[Employment]
        """

        self._employments = employments

    @property
    def vacation_rate_employees(self):
        """Gets the vacation_rate_employees of this Employee.  # noqa: E501


        :return: The vacation_rate_employees of this Employee.  # noqa: E501
        :rtype: list[VacationRateEmployee]
        """
        return self._vacation_rate_employees

    @vacation_rate_employees.setter
    def vacation_rate_employees(self, vacation_rate_employees):
        """Sets the vacation_rate_employees of this Employee.


        :param vacation_rate_employees: The vacation_rate_employees of this Employee.  # noqa: E501
        :type: list[VacationRateEmployee]
        """

        self._vacation_rate_employees = vacation_rate_employees

    @property
    def tax_cards(self):
        """Gets the tax_cards of this Employee.  # noqa: E501


        :return: The tax_cards of this Employee.  # noqa: E501
        :rtype: list[EmployeeTaxCard]
        """
        return self._tax_cards

    @tax_cards.setter
    def tax_cards(self, tax_cards):
        """Sets the tax_cards of this Employee.


        :param tax_cards: The tax_cards of this Employee.  # noqa: E501
        :type: list[EmployeeTaxCard]
        """

        self._tax_cards = tax_cards

    @property
    def custom_values(self):
        """Gets the custom_values of this Employee.  # noqa: E501


        :return: The custom_values of this Employee.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Employee.


        :param custom_values: The custom_values of this Employee.  # noqa: E501
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
        if issubclass(Employee, dict):
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
        if not isinstance(other, Employee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
