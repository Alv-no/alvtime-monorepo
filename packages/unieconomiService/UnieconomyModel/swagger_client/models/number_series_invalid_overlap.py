# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NumberSeriesInvalidOverlap(object):
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
        'number_serie_type_aid': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'number_serie_type_bid': 'int',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'number_serie_type_a': 'NumberSeriesType',
        'number_serie_type_b': 'NumberSeriesType',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'number_serie_type_aid': 'NumberSerieTypeAID',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'number_serie_type_bid': 'NumberSerieTypeBID',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'number_serie_type_a': 'NumberSerieTypeA',
        'number_serie_type_b': 'NumberSerieTypeB',
        'custom_values': 'CustomValues'
    }

    def __init__(self, number_serie_type_aid=None, status_code=None, deleted=None, number_serie_type_bid=None, id=None, updated_by=None, created_by=None, number_serie_type_a=None, number_serie_type_b=None, custom_values=None):  # noqa: E501
        """NumberSeriesInvalidOverlap - a model defined in Swagger"""  # noqa: E501
        self._number_serie_type_aid = None
        self._status_code = None
        self._deleted = None
        self._number_serie_type_bid = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._number_serie_type_a = None
        self._number_serie_type_b = None
        self._custom_values = None
        self.discriminator = None
        if number_serie_type_aid is not None:
            self.number_serie_type_aid = number_serie_type_aid
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if number_serie_type_bid is not None:
            self.number_serie_type_bid = number_serie_type_bid
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if number_serie_type_a is not None:
            self.number_serie_type_a = number_serie_type_a
        if number_serie_type_b is not None:
            self.number_serie_type_b = number_serie_type_b
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def number_serie_type_aid(self):
        """Gets the number_serie_type_aid of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The number_serie_type_aid of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: int
        """
        return self._number_serie_type_aid

    @number_serie_type_aid.setter
    def number_serie_type_aid(self, number_serie_type_aid):
        """Sets the number_serie_type_aid of this NumberSeriesInvalidOverlap.


        :param number_serie_type_aid: The number_serie_type_aid of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: int
        """

        self._number_serie_type_aid = number_serie_type_aid

    @property
    def status_code(self):
        """Gets the status_code of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The status_code of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this NumberSeriesInvalidOverlap.


        :param status_code: The status_code of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The deleted of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this NumberSeriesInvalidOverlap.


        :param deleted: The deleted of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def number_serie_type_bid(self):
        """Gets the number_serie_type_bid of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The number_serie_type_bid of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: int
        """
        return self._number_serie_type_bid

    @number_serie_type_bid.setter
    def number_serie_type_bid(self, number_serie_type_bid):
        """Sets the number_serie_type_bid of this NumberSeriesInvalidOverlap.


        :param number_serie_type_bid: The number_serie_type_bid of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: int
        """

        self._number_serie_type_bid = number_serie_type_bid

    @property
    def id(self):
        """Gets the id of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The id of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NumberSeriesInvalidOverlap.


        :param id: The id of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The updated_by of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this NumberSeriesInvalidOverlap.


        :param updated_by: The updated_by of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The created_by of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NumberSeriesInvalidOverlap.


        :param created_by: The created_by of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def number_serie_type_a(self):
        """Gets the number_serie_type_a of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The number_serie_type_a of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: NumberSeriesType
        """
        return self._number_serie_type_a

    @number_serie_type_a.setter
    def number_serie_type_a(self, number_serie_type_a):
        """Sets the number_serie_type_a of this NumberSeriesInvalidOverlap.


        :param number_serie_type_a: The number_serie_type_a of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: NumberSeriesType
        """

        self._number_serie_type_a = number_serie_type_a

    @property
    def number_serie_type_b(self):
        """Gets the number_serie_type_b of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The number_serie_type_b of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: NumberSeriesType
        """
        return self._number_serie_type_b

    @number_serie_type_b.setter
    def number_serie_type_b(self, number_serie_type_b):
        """Sets the number_serie_type_b of this NumberSeriesInvalidOverlap.


        :param number_serie_type_b: The number_serie_type_b of this NumberSeriesInvalidOverlap.  # noqa: E501
        :type: NumberSeriesType
        """

        self._number_serie_type_b = number_serie_type_b

    @property
    def custom_values(self):
        """Gets the custom_values of this NumberSeriesInvalidOverlap.  # noqa: E501


        :return: The custom_values of this NumberSeriesInvalidOverlap.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this NumberSeriesInvalidOverlap.


        :param custom_values: The custom_values of this NumberSeriesInvalidOverlap.  # noqa: E501
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
        if issubclass(NumberSeriesInvalidOverlap, dict):
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
        if not isinstance(other, NumberSeriesInvalidOverlap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
