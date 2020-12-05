# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PeriodSeries(object):
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
        'active': 'bool',
        'name': 'str',
        'deleted': 'bool',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'series_type': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'active': 'Active',
        'name': 'Name',
        'deleted': 'Deleted',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'series_type': 'SeriesType',
        'custom_values': 'CustomValues'
    }

    def __init__(self, active=None, name=None, deleted=None, id=None, updated_by=None, created_by=None, series_type=None, custom_values=None):  # noqa: E501
        """PeriodSeries - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._name = None
        self._deleted = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._series_type = None
        self._custom_values = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if name is not None:
            self.name = name
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if series_type is not None:
            self.series_type = series_type
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def active(self):
        """Gets the active of this PeriodSeries.  # noqa: E501


        :return: The active of this PeriodSeries.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PeriodSeries.


        :param active: The active of this PeriodSeries.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """Gets the name of this PeriodSeries.  # noqa: E501


        :return: The name of this PeriodSeries.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PeriodSeries.


        :param name: The name of this PeriodSeries.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deleted(self):
        """Gets the deleted of this PeriodSeries.  # noqa: E501


        :return: The deleted of this PeriodSeries.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this PeriodSeries.


        :param deleted: The deleted of this PeriodSeries.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this PeriodSeries.  # noqa: E501


        :return: The id of this PeriodSeries.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PeriodSeries.


        :param id: The id of this PeriodSeries.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this PeriodSeries.  # noqa: E501


        :return: The updated_by of this PeriodSeries.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this PeriodSeries.


        :param updated_by: The updated_by of this PeriodSeries.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this PeriodSeries.  # noqa: E501


        :return: The created_by of this PeriodSeries.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PeriodSeries.


        :param created_by: The created_by of this PeriodSeries.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def series_type(self):
        """Gets the series_type of this PeriodSeries.  # noqa: E501


        :return: The series_type of this PeriodSeries.  # noqa: E501
        :rtype: str
        """
        return self._series_type

    @series_type.setter
    def series_type(self, series_type):
        """Sets the series_type of this PeriodSeries.


        :param series_type: The series_type of this PeriodSeries.  # noqa: E501
        :type: str
        """

        self._series_type = series_type

    @property
    def custom_values(self):
        """Gets the custom_values of this PeriodSeries.  # noqa: E501


        :return: The custom_values of this PeriodSeries.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this PeriodSeries.


        :param custom_values: The custom_values of this PeriodSeries.  # noqa: E501
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
        if issubclass(PeriodSeries, dict):
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
        if not isinstance(other, PeriodSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
