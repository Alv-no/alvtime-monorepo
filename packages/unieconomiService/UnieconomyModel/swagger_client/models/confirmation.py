# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Confirmation(object):
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
        'email': 'str',
        'phone': 'str',
        'code': 'str',
        'status_code': 'int',
        'deleted': 'bool',
        'company_name': 'str',
        'contract_type': 'str',
        'id': 'int',
        'display_name': 'str',
        'postal_code': 'str',
        'updated_by': 'str',
        'created_by': 'str',
        'sign_up_referrer': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'email': 'Email',
        'phone': 'Phone',
        'code': 'Code',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'company_name': 'CompanyName',
        'contract_type': 'ContractType',
        'id': 'ID',
        'display_name': 'DisplayName',
        'postal_code': 'PostalCode',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'sign_up_referrer': 'SignUpReferrer',
        'custom_values': 'CustomValues'
    }

    def __init__(self, email=None, phone=None, code=None, status_code=None, deleted=None, company_name=None, contract_type=None, id=None, display_name=None, postal_code=None, updated_by=None, created_by=None, sign_up_referrer=None, custom_values=None):  # noqa: E501
        """Confirmation - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._phone = None
        self._code = None
        self._status_code = None
        self._deleted = None
        self._company_name = None
        self._contract_type = None
        self._id = None
        self._display_name = None
        self._postal_code = None
        self._updated_by = None
        self._created_by = None
        self._sign_up_referrer = None
        self._custom_values = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if code is not None:
            self.code = code
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if company_name is not None:
            self.company_name = company_name
        if contract_type is not None:
            self.contract_type = contract_type
        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if postal_code is not None:
            self.postal_code = postal_code
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if sign_up_referrer is not None:
            self.sign_up_referrer = sign_up_referrer
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def email(self):
        """Gets the email of this Confirmation.  # noqa: E501


        :return: The email of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Confirmation.


        :param email: The email of this Confirmation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Confirmation.  # noqa: E501


        :return: The phone of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Confirmation.


        :param phone: The phone of this Confirmation.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def code(self):
        """Gets the code of this Confirmation.  # noqa: E501


        :return: The code of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Confirmation.


        :param code: The code of this Confirmation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def status_code(self):
        """Gets the status_code of this Confirmation.  # noqa: E501


        :return: The status_code of this Confirmation.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Confirmation.


        :param status_code: The status_code of this Confirmation.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this Confirmation.  # noqa: E501


        :return: The deleted of this Confirmation.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Confirmation.


        :param deleted: The deleted of this Confirmation.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def company_name(self):
        """Gets the company_name of this Confirmation.  # noqa: E501


        :return: The company_name of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Confirmation.


        :param company_name: The company_name of this Confirmation.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contract_type(self):
        """Gets the contract_type of this Confirmation.  # noqa: E501


        :return: The contract_type of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this Confirmation.


        :param contract_type: The contract_type of this Confirmation.  # noqa: E501
        :type: str
        """

        self._contract_type = contract_type

    @property
    def id(self):
        """Gets the id of this Confirmation.  # noqa: E501


        :return: The id of this Confirmation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Confirmation.


        :param id: The id of this Confirmation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Confirmation.  # noqa: E501


        :return: The display_name of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Confirmation.


        :param display_name: The display_name of this Confirmation.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def postal_code(self):
        """Gets the postal_code of this Confirmation.  # noqa: E501


        :return: The postal_code of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Confirmation.


        :param postal_code: The postal_code of this Confirmation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def updated_by(self):
        """Gets the updated_by of this Confirmation.  # noqa: E501


        :return: The updated_by of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Confirmation.


        :param updated_by: The updated_by of this Confirmation.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this Confirmation.  # noqa: E501


        :return: The created_by of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Confirmation.


        :param created_by: The created_by of this Confirmation.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def sign_up_referrer(self):
        """Gets the sign_up_referrer of this Confirmation.  # noqa: E501


        :return: The sign_up_referrer of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._sign_up_referrer

    @sign_up_referrer.setter
    def sign_up_referrer(self, sign_up_referrer):
        """Sets the sign_up_referrer of this Confirmation.


        :param sign_up_referrer: The sign_up_referrer of this Confirmation.  # noqa: E501
        :type: str
        """

        self._sign_up_referrer = sign_up_referrer

    @property
    def custom_values(self):
        """Gets the custom_values of this Confirmation.  # noqa: E501


        :return: The custom_values of this Confirmation.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Confirmation.


        :param custom_values: The custom_values of this Confirmation.  # noqa: E501
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
        if issubclass(Confirmation, dict):
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
        if not isinstance(other, Confirmation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
