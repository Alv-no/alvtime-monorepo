# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ComponentLayoutDto(object):
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
        'url': 'str',
        'name': 'str',
        'base_entity': 'str',
        'fields': 'list[FieldLayoutDto]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'url': 'Url',
        'name': 'Name',
        'base_entity': 'BaseEntity',
        'fields': 'Fields',
        'custom_values': 'CustomValues'
    }

    def __init__(self, url=None, name=None, base_entity=None, fields=None, custom_values=None):  # noqa: E501
        """ComponentLayoutDto - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._name = None
        self._base_entity = None
        self._fields = None
        self._custom_values = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if name is not None:
            self.name = name
        if base_entity is not None:
            self.base_entity = base_entity
        if fields is not None:
            self.fields = fields
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def url(self):
        """Gets the url of this ComponentLayoutDto.  # noqa: E501


        :return: The url of this ComponentLayoutDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ComponentLayoutDto.


        :param url: The url of this ComponentLayoutDto.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this ComponentLayoutDto.  # noqa: E501


        :return: The name of this ComponentLayoutDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentLayoutDto.


        :param name: The name of this ComponentLayoutDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_entity(self):
        """Gets the base_entity of this ComponentLayoutDto.  # noqa: E501


        :return: The base_entity of this ComponentLayoutDto.  # noqa: E501
        :rtype: str
        """
        return self._base_entity

    @base_entity.setter
    def base_entity(self, base_entity):
        """Sets the base_entity of this ComponentLayoutDto.


        :param base_entity: The base_entity of this ComponentLayoutDto.  # noqa: E501
        :type: str
        """

        self._base_entity = base_entity

    @property
    def fields(self):
        """Gets the fields of this ComponentLayoutDto.  # noqa: E501


        :return: The fields of this ComponentLayoutDto.  # noqa: E501
        :rtype: list[FieldLayoutDto]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ComponentLayoutDto.


        :param fields: The fields of this ComponentLayoutDto.  # noqa: E501
        :type: list[FieldLayoutDto]
        """

        self._fields = fields

    @property
    def custom_values(self):
        """Gets the custom_values of this ComponentLayoutDto.  # noqa: E501


        :return: The custom_values of this ComponentLayoutDto.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ComponentLayoutDto.


        :param custom_values: The custom_values of this ComponentLayoutDto.  # noqa: E501
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
        if issubclass(ComponentLayoutDto, dict):
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
        if not isinstance(other, ComponentLayoutDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
