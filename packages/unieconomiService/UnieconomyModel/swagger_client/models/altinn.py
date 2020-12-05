# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Altinn(object):
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
        'status_code': 'int',
        'deleted': 'bool',
        'language': 'str',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'preferred_login': 'str',
        'system_pw': 'str',
        'system_id': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'language': 'Language',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'preferred_login': 'PreferredLogin',
        'system_pw': 'SystemPw',
        'system_id': 'SystemID',
        'custom_values': 'CustomValues'
    }

    def __init__(self, status_code=None, deleted=None, language=None, id=None, updated_by=None, created_by=None, preferred_login=None, system_pw=None, system_id=None, custom_values=None):  # noqa: E501
        """Altinn - a model defined in Swagger"""  # noqa: E501
        self._status_code = None
        self._deleted = None
        self._language = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._preferred_login = None
        self._system_pw = None
        self._system_id = None
        self._custom_values = None
        self.discriminator = None
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if language is not None:
            self.language = language
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if preferred_login is not None:
            self.preferred_login = preferred_login
        if system_pw is not None:
            self.system_pw = system_pw
        if system_id is not None:
            self.system_id = system_id
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def status_code(self):
        """Gets the status_code of this Altinn.  # noqa: E501


        :return: The status_code of this Altinn.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Altinn.


        :param status_code: The status_code of this Altinn.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this Altinn.  # noqa: E501


        :return: The deleted of this Altinn.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Altinn.


        :param deleted: The deleted of this Altinn.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def language(self):
        """Gets the language of this Altinn.  # noqa: E501


        :return: The language of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Altinn.


        :param language: The language of this Altinn.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def id(self):
        """Gets the id of this Altinn.  # noqa: E501


        :return: The id of this Altinn.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Altinn.


        :param id: The id of this Altinn.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this Altinn.  # noqa: E501


        :return: The updated_by of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Altinn.


        :param updated_by: The updated_by of this Altinn.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this Altinn.  # noqa: E501


        :return: The created_by of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Altinn.


        :param created_by: The created_by of this Altinn.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def preferred_login(self):
        """Gets the preferred_login of this Altinn.  # noqa: E501


        :return: The preferred_login of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._preferred_login

    @preferred_login.setter
    def preferred_login(self, preferred_login):
        """Sets the preferred_login of this Altinn.


        :param preferred_login: The preferred_login of this Altinn.  # noqa: E501
        :type: str
        """

        self._preferred_login = preferred_login

    @property
    def system_pw(self):
        """Gets the system_pw of this Altinn.  # noqa: E501


        :return: The system_pw of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._system_pw

    @system_pw.setter
    def system_pw(self, system_pw):
        """Sets the system_pw of this Altinn.


        :param system_pw: The system_pw of this Altinn.  # noqa: E501
        :type: str
        """

        self._system_pw = system_pw

    @property
    def system_id(self):
        """Gets the system_id of this Altinn.  # noqa: E501


        :return: The system_id of this Altinn.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this Altinn.


        :param system_id: The system_id of this Altinn.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def custom_values(self):
        """Gets the custom_values of this Altinn.  # noqa: E501


        :return: The custom_values of this Altinn.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Altinn.


        :param custom_values: The custom_values of this Altinn.  # noqa: E501
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
        if issubclass(Altinn, dict):
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
        if not isinstance(other, Altinn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
