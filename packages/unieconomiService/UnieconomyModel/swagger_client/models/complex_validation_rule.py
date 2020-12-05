# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ComplexValidationRule(object):
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
        'message': 'str',
        'sync_key': 'str',
        'deleted': 'bool',
        'changed_by_company': 'bool',
        'level': 'str',
        'entity_type': 'str',
        'id': 'int',
        'validation_code': 'int',
        'updated_by': 'str',
        'operation': 'str',
        'created_by': 'str',
        'system': 'bool',
        'on_conflict': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'message': 'Message',
        'sync_key': 'SyncKey',
        'deleted': 'Deleted',
        'changed_by_company': 'ChangedByCompany',
        'level': 'Level',
        'entity_type': 'EntityType',
        'id': 'ID',
        'validation_code': 'ValidationCode',
        'updated_by': 'UpdatedBy',
        'operation': 'Operation',
        'created_by': 'CreatedBy',
        'system': 'System',
        'on_conflict': 'OnConflict',
        'custom_values': 'CustomValues'
    }

    def __init__(self, message=None, sync_key=None, deleted=None, changed_by_company=None, level=None, entity_type=None, id=None, validation_code=None, updated_by=None, operation=None, created_by=None, system=None, on_conflict=None, custom_values=None):  # noqa: E501
        """ComplexValidationRule - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._sync_key = None
        self._deleted = None
        self._changed_by_company = None
        self._level = None
        self._entity_type = None
        self._id = None
        self._validation_code = None
        self._updated_by = None
        self._operation = None
        self._created_by = None
        self._system = None
        self._on_conflict = None
        self._custom_values = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if sync_key is not None:
            self.sync_key = sync_key
        if deleted is not None:
            self.deleted = deleted
        if changed_by_company is not None:
            self.changed_by_company = changed_by_company
        if level is not None:
            self.level = level
        if entity_type is not None:
            self.entity_type = entity_type
        if id is not None:
            self.id = id
        if validation_code is not None:
            self.validation_code = validation_code
        if updated_by is not None:
            self.updated_by = updated_by
        if operation is not None:
            self.operation = operation
        if created_by is not None:
            self.created_by = created_by
        if system is not None:
            self.system = system
        if on_conflict is not None:
            self.on_conflict = on_conflict
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def message(self):
        """Gets the message of this ComplexValidationRule.  # noqa: E501


        :return: The message of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ComplexValidationRule.


        :param message: The message of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def sync_key(self):
        """Gets the sync_key of this ComplexValidationRule.  # noqa: E501


        :return: The sync_key of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._sync_key

    @sync_key.setter
    def sync_key(self, sync_key):
        """Sets the sync_key of this ComplexValidationRule.


        :param sync_key: The sync_key of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._sync_key = sync_key

    @property
    def deleted(self):
        """Gets the deleted of this ComplexValidationRule.  # noqa: E501


        :return: The deleted of this ComplexValidationRule.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ComplexValidationRule.


        :param deleted: The deleted of this ComplexValidationRule.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def changed_by_company(self):
        """Gets the changed_by_company of this ComplexValidationRule.  # noqa: E501


        :return: The changed_by_company of this ComplexValidationRule.  # noqa: E501
        :rtype: bool
        """
        return self._changed_by_company

    @changed_by_company.setter
    def changed_by_company(self, changed_by_company):
        """Sets the changed_by_company of this ComplexValidationRule.


        :param changed_by_company: The changed_by_company of this ComplexValidationRule.  # noqa: E501
        :type: bool
        """

        self._changed_by_company = changed_by_company

    @property
    def level(self):
        """Gets the level of this ComplexValidationRule.  # noqa: E501


        :return: The level of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ComplexValidationRule.


        :param level: The level of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def entity_type(self):
        """Gets the entity_type of this ComplexValidationRule.  # noqa: E501


        :return: The entity_type of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ComplexValidationRule.


        :param entity_type: The entity_type of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def id(self):
        """Gets the id of this ComplexValidationRule.  # noqa: E501


        :return: The id of this ComplexValidationRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComplexValidationRule.


        :param id: The id of this ComplexValidationRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def validation_code(self):
        """Gets the validation_code of this ComplexValidationRule.  # noqa: E501


        :return: The validation_code of this ComplexValidationRule.  # noqa: E501
        :rtype: int
        """
        return self._validation_code

    @validation_code.setter
    def validation_code(self, validation_code):
        """Sets the validation_code of this ComplexValidationRule.


        :param validation_code: The validation_code of this ComplexValidationRule.  # noqa: E501
        :type: int
        """

        self._validation_code = validation_code

    @property
    def updated_by(self):
        """Gets the updated_by of this ComplexValidationRule.  # noqa: E501


        :return: The updated_by of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ComplexValidationRule.


        :param updated_by: The updated_by of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def operation(self):
        """Gets the operation of this ComplexValidationRule.  # noqa: E501


        :return: The operation of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ComplexValidationRule.


        :param operation: The operation of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def created_by(self):
        """Gets the created_by of this ComplexValidationRule.  # noqa: E501


        :return: The created_by of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ComplexValidationRule.


        :param created_by: The created_by of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def system(self):
        """Gets the system of this ComplexValidationRule.  # noqa: E501


        :return: The system of this ComplexValidationRule.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this ComplexValidationRule.


        :param system: The system of this ComplexValidationRule.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def on_conflict(self):
        """Gets the on_conflict of this ComplexValidationRule.  # noqa: E501


        :return: The on_conflict of this ComplexValidationRule.  # noqa: E501
        :rtype: str
        """
        return self._on_conflict

    @on_conflict.setter
    def on_conflict(self, on_conflict):
        """Sets the on_conflict of this ComplexValidationRule.


        :param on_conflict: The on_conflict of this ComplexValidationRule.  # noqa: E501
        :type: str
        """

        self._on_conflict = on_conflict

    @property
    def custom_values(self):
        """Gets the custom_values of this ComplexValidationRule.  # noqa: E501


        :return: The custom_values of this ComplexValidationRule.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ComplexValidationRule.


        :param custom_values: The custom_values of this ComplexValidationRule.  # noqa: E501
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
        if issubclass(ComplexValidationRule, dict):
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
        if not isinstance(other, ComplexValidationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
