# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountVisibilityGroup(object):
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
        'name': 'str',
        'deleted': 'bool',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'accounts': 'list[AccountVisibilityGroupAccount]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'name': 'Name',
        'deleted': 'Deleted',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'accounts': 'Accounts',
        'custom_values': 'CustomValues'
    }

    def __init__(self, name=None, deleted=None, id=None, updated_by=None, created_by=None, accounts=None, custom_values=None):  # noqa: E501
        """AccountVisibilityGroup - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._deleted = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._accounts = None
        self._custom_values = None
        self.discriminator = None
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
        if accounts is not None:
            self.accounts = accounts
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def name(self):
        """Gets the name of this AccountVisibilityGroup.  # noqa: E501


        :return: The name of this AccountVisibilityGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountVisibilityGroup.


        :param name: The name of this AccountVisibilityGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deleted(self):
        """Gets the deleted of this AccountVisibilityGroup.  # noqa: E501


        :return: The deleted of this AccountVisibilityGroup.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AccountVisibilityGroup.


        :param deleted: The deleted of this AccountVisibilityGroup.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this AccountVisibilityGroup.  # noqa: E501


        :return: The id of this AccountVisibilityGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountVisibilityGroup.


        :param id: The id of this AccountVisibilityGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this AccountVisibilityGroup.  # noqa: E501


        :return: The updated_by of this AccountVisibilityGroup.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AccountVisibilityGroup.


        :param updated_by: The updated_by of this AccountVisibilityGroup.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this AccountVisibilityGroup.  # noqa: E501


        :return: The created_by of this AccountVisibilityGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AccountVisibilityGroup.


        :param created_by: The created_by of this AccountVisibilityGroup.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def accounts(self):
        """Gets the accounts of this AccountVisibilityGroup.  # noqa: E501


        :return: The accounts of this AccountVisibilityGroup.  # noqa: E501
        :rtype: list[AccountVisibilityGroupAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this AccountVisibilityGroup.


        :param accounts: The accounts of this AccountVisibilityGroup.  # noqa: E501
        :type: list[AccountVisibilityGroupAccount]
        """

        self._accounts = accounts

    @property
    def custom_values(self):
        """Gets the custom_values of this AccountVisibilityGroup.  # noqa: E501


        :return: The custom_values of this AccountVisibilityGroup.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this AccountVisibilityGroup.


        :param custom_values: The custom_values of this AccountVisibilityGroup.  # noqa: E501
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
        if issubclass(AccountVisibilityGroup, dict):
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
        if not isinstance(other, AccountVisibilityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
