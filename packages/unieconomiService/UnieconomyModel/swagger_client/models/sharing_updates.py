# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SharingUpdates(object):
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
        'sharing_status_updates': 'list[SharingStatusUpdate]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'sharing_status_updates': 'SharingStatusUpdates',
        'custom_values': 'CustomValues'
    }

    def __init__(self, sharing_status_updates=None, custom_values=None):  # noqa: E501
        """SharingUpdates - a model defined in Swagger"""  # noqa: E501
        self._sharing_status_updates = None
        self._custom_values = None
        self.discriminator = None
        if sharing_status_updates is not None:
            self.sharing_status_updates = sharing_status_updates
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def sharing_status_updates(self):
        """Gets the sharing_status_updates of this SharingUpdates.  # noqa: E501


        :return: The sharing_status_updates of this SharingUpdates.  # noqa: E501
        :rtype: list[SharingStatusUpdate]
        """
        return self._sharing_status_updates

    @sharing_status_updates.setter
    def sharing_status_updates(self, sharing_status_updates):
        """Sets the sharing_status_updates of this SharingUpdates.


        :param sharing_status_updates: The sharing_status_updates of this SharingUpdates.  # noqa: E501
        :type: list[SharingStatusUpdate]
        """

        self._sharing_status_updates = sharing_status_updates

    @property
    def custom_values(self):
        """Gets the custom_values of this SharingUpdates.  # noqa: E501


        :return: The custom_values of this SharingUpdates.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this SharingUpdates.


        :param custom_values: The custom_values of this SharingUpdates.  # noqa: E501
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
        if issubclass(SharingUpdates, dict):
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
        if not isinstance(other, SharingUpdates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
