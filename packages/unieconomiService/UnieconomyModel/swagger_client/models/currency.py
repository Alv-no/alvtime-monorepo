# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Currency(object):
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
        'factor': 'int',
        'from_currency_code_id': 'int',
        'deleted': 'bool',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'to_currency_code_id': 'int',
        'source': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'factor': 'Factor',
        'from_currency_code_id': 'FromCurrencyCodeID',
        'deleted': 'Deleted',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'to_currency_code_id': 'ToCurrencyCodeID',
        'source': 'Source',
        'custom_values': 'CustomValues'
    }

    def __init__(self, factor=None, from_currency_code_id=None, deleted=None, id=None, updated_by=None, created_by=None, to_currency_code_id=None, source=None, custom_values=None):  # noqa: E501
        """Currency - a model defined in Swagger"""  # noqa: E501
        self._factor = None
        self._from_currency_code_id = None
        self._deleted = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._to_currency_code_id = None
        self._source = None
        self._custom_values = None
        self.discriminator = None
        if factor is not None:
            self.factor = factor
        if from_currency_code_id is not None:
            self.from_currency_code_id = from_currency_code_id
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if to_currency_code_id is not None:
            self.to_currency_code_id = to_currency_code_id
        if source is not None:
            self.source = source
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def factor(self):
        """Gets the factor of this Currency.  # noqa: E501


        :return: The factor of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this Currency.


        :param factor: The factor of this Currency.  # noqa: E501
        :type: int
        """

        self._factor = factor

    @property
    def from_currency_code_id(self):
        """Gets the from_currency_code_id of this Currency.  # noqa: E501


        :return: The from_currency_code_id of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._from_currency_code_id

    @from_currency_code_id.setter
    def from_currency_code_id(self, from_currency_code_id):
        """Sets the from_currency_code_id of this Currency.


        :param from_currency_code_id: The from_currency_code_id of this Currency.  # noqa: E501
        :type: int
        """

        self._from_currency_code_id = from_currency_code_id

    @property
    def deleted(self):
        """Gets the deleted of this Currency.  # noqa: E501


        :return: The deleted of this Currency.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Currency.


        :param deleted: The deleted of this Currency.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this Currency.  # noqa: E501


        :return: The id of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Currency.


        :param id: The id of this Currency.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this Currency.  # noqa: E501


        :return: The updated_by of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Currency.


        :param updated_by: The updated_by of this Currency.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this Currency.  # noqa: E501


        :return: The created_by of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Currency.


        :param created_by: The created_by of this Currency.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def to_currency_code_id(self):
        """Gets the to_currency_code_id of this Currency.  # noqa: E501


        :return: The to_currency_code_id of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._to_currency_code_id

    @to_currency_code_id.setter
    def to_currency_code_id(self, to_currency_code_id):
        """Sets the to_currency_code_id of this Currency.


        :param to_currency_code_id: The to_currency_code_id of this Currency.  # noqa: E501
        :type: int
        """

        self._to_currency_code_id = to_currency_code_id

    @property
    def source(self):
        """Gets the source of this Currency.  # noqa: E501


        :return: The source of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Currency.


        :param source: The source of this Currency.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def custom_values(self):
        """Gets the custom_values of this Currency.  # noqa: E501


        :return: The custom_values of this Currency.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Currency.


        :param custom_values: The custom_values of this Currency.  # noqa: E501
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
        if issubclass(Currency, dict):
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
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
