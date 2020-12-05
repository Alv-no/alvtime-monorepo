# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeniedUserAccessLog(object):
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
        'message': 'str',
        'deleted': 'bool',
        'company_name': 'str',
        'username': 'str',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'company_id': 'int',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'email': 'Email',
        'message': 'Message',
        'deleted': 'Deleted',
        'company_name': 'CompanyName',
        'username': 'Username',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'company_id': 'CompanyID',
        'custom_values': 'CustomValues'
    }

    def __init__(self, email=None, message=None, deleted=None, company_name=None, username=None, id=None, updated_by=None, created_by=None, company_id=None, custom_values=None):  # noqa: E501
        """DeniedUserAccessLog - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._message = None
        self._deleted = None
        self._company_name = None
        self._username = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._company_id = None
        self._custom_values = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if message is not None:
            self.message = message
        if deleted is not None:
            self.deleted = deleted
        if company_name is not None:
            self.company_name = company_name
        if username is not None:
            self.username = username
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if company_id is not None:
            self.company_id = company_id
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def email(self):
        """Gets the email of this DeniedUserAccessLog.  # noqa: E501


        :return: The email of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DeniedUserAccessLog.


        :param email: The email of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def message(self):
        """Gets the message of this DeniedUserAccessLog.  # noqa: E501


        :return: The message of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeniedUserAccessLog.


        :param message: The message of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def deleted(self):
        """Gets the deleted of this DeniedUserAccessLog.  # noqa: E501


        :return: The deleted of this DeniedUserAccessLog.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeniedUserAccessLog.


        :param deleted: The deleted of this DeniedUserAccessLog.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def company_name(self):
        """Gets the company_name of this DeniedUserAccessLog.  # noqa: E501


        :return: The company_name of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this DeniedUserAccessLog.


        :param company_name: The company_name of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def username(self):
        """Gets the username of this DeniedUserAccessLog.  # noqa: E501


        :return: The username of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DeniedUserAccessLog.


        :param username: The username of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def id(self):
        """Gets the id of this DeniedUserAccessLog.  # noqa: E501


        :return: The id of this DeniedUserAccessLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeniedUserAccessLog.


        :param id: The id of this DeniedUserAccessLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this DeniedUserAccessLog.  # noqa: E501


        :return: The updated_by of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this DeniedUserAccessLog.


        :param updated_by: The updated_by of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this DeniedUserAccessLog.  # noqa: E501


        :return: The created_by of this DeniedUserAccessLog.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DeniedUserAccessLog.


        :param created_by: The created_by of this DeniedUserAccessLog.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def company_id(self):
        """Gets the company_id of this DeniedUserAccessLog.  # noqa: E501


        :return: The company_id of this DeniedUserAccessLog.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this DeniedUserAccessLog.


        :param company_id: The company_id of this DeniedUserAccessLog.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def custom_values(self):
        """Gets the custom_values of this DeniedUserAccessLog.  # noqa: E501


        :return: The custom_values of this DeniedUserAccessLog.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this DeniedUserAccessLog.


        :param custom_values: The custom_values of this DeniedUserAccessLog.  # noqa: E501
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
        if issubclass(DeniedUserAccessLog, dict):
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
        if not isinstance(other, DeniedUserAccessLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
