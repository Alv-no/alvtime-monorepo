# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TransitionThresholdApproval(object):
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
        'approval_id': 'int',
        'value': 'str',
        'shared_role_id': 'int',
        'deleted': 'bool',
        'shared_reject_transition_id': 'int',
        'property_name': 'str',
        'reject_status_code': 'int',
        'operator': 'str',
        'id': 'int',
        'updated_by': 'str',
        'shared_approve_transition_id': 'int',
        'operation': 'str',
        'created_by': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'approval_id': 'ApprovalID',
        'value': 'Value',
        'shared_role_id': 'SharedRoleId',
        'deleted': 'Deleted',
        'shared_reject_transition_id': 'SharedRejectTransitionId',
        'property_name': 'PropertyName',
        'reject_status_code': 'RejectStatusCode',
        'operator': 'Operator',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'shared_approve_transition_id': 'SharedApproveTransitionId',
        'operation': 'Operation',
        'created_by': 'CreatedBy',
        'custom_values': 'CustomValues'
    }

    def __init__(self, approval_id=None, value=None, shared_role_id=None, deleted=None, shared_reject_transition_id=None, property_name=None, reject_status_code=None, operator=None, id=None, updated_by=None, shared_approve_transition_id=None, operation=None, created_by=None, custom_values=None):  # noqa: E501
        """TransitionThresholdApproval - a model defined in Swagger"""  # noqa: E501
        self._approval_id = None
        self._value = None
        self._shared_role_id = None
        self._deleted = None
        self._shared_reject_transition_id = None
        self._property_name = None
        self._reject_status_code = None
        self._operator = None
        self._id = None
        self._updated_by = None
        self._shared_approve_transition_id = None
        self._operation = None
        self._created_by = None
        self._custom_values = None
        self.discriminator = None
        if approval_id is not None:
            self.approval_id = approval_id
        if value is not None:
            self.value = value
        if shared_role_id is not None:
            self.shared_role_id = shared_role_id
        if deleted is not None:
            self.deleted = deleted
        if shared_reject_transition_id is not None:
            self.shared_reject_transition_id = shared_reject_transition_id
        if property_name is not None:
            self.property_name = property_name
        if reject_status_code is not None:
            self.reject_status_code = reject_status_code
        if operator is not None:
            self.operator = operator
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if shared_approve_transition_id is not None:
            self.shared_approve_transition_id = shared_approve_transition_id
        if operation is not None:
            self.operation = operation
        if created_by is not None:
            self.created_by = created_by
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def approval_id(self):
        """Gets the approval_id of this TransitionThresholdApproval.  # noqa: E501


        :return: The approval_id of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._approval_id

    @approval_id.setter
    def approval_id(self, approval_id):
        """Sets the approval_id of this TransitionThresholdApproval.


        :param approval_id: The approval_id of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._approval_id = approval_id

    @property
    def value(self):
        """Gets the value of this TransitionThresholdApproval.  # noqa: E501


        :return: The value of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransitionThresholdApproval.


        :param value: The value of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def shared_role_id(self):
        """Gets the shared_role_id of this TransitionThresholdApproval.  # noqa: E501


        :return: The shared_role_id of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._shared_role_id

    @shared_role_id.setter
    def shared_role_id(self, shared_role_id):
        """Sets the shared_role_id of this TransitionThresholdApproval.


        :param shared_role_id: The shared_role_id of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._shared_role_id = shared_role_id

    @property
    def deleted(self):
        """Gets the deleted of this TransitionThresholdApproval.  # noqa: E501


        :return: The deleted of this TransitionThresholdApproval.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TransitionThresholdApproval.


        :param deleted: The deleted of this TransitionThresholdApproval.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def shared_reject_transition_id(self):
        """Gets the shared_reject_transition_id of this TransitionThresholdApproval.  # noqa: E501


        :return: The shared_reject_transition_id of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._shared_reject_transition_id

    @shared_reject_transition_id.setter
    def shared_reject_transition_id(self, shared_reject_transition_id):
        """Sets the shared_reject_transition_id of this TransitionThresholdApproval.


        :param shared_reject_transition_id: The shared_reject_transition_id of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._shared_reject_transition_id = shared_reject_transition_id

    @property
    def property_name(self):
        """Gets the property_name of this TransitionThresholdApproval.  # noqa: E501


        :return: The property_name of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this TransitionThresholdApproval.


        :param property_name: The property_name of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def reject_status_code(self):
        """Gets the reject_status_code of this TransitionThresholdApproval.  # noqa: E501


        :return: The reject_status_code of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._reject_status_code

    @reject_status_code.setter
    def reject_status_code(self, reject_status_code):
        """Sets the reject_status_code of this TransitionThresholdApproval.


        :param reject_status_code: The reject_status_code of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._reject_status_code = reject_status_code

    @property
    def operator(self):
        """Gets the operator of this TransitionThresholdApproval.  # noqa: E501


        :return: The operator of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TransitionThresholdApproval.


        :param operator: The operator of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def id(self):
        """Gets the id of this TransitionThresholdApproval.  # noqa: E501


        :return: The id of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransitionThresholdApproval.


        :param id: The id of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this TransitionThresholdApproval.  # noqa: E501


        :return: The updated_by of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this TransitionThresholdApproval.


        :param updated_by: The updated_by of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def shared_approve_transition_id(self):
        """Gets the shared_approve_transition_id of this TransitionThresholdApproval.  # noqa: E501


        :return: The shared_approve_transition_id of this TransitionThresholdApproval.  # noqa: E501
        :rtype: int
        """
        return self._shared_approve_transition_id

    @shared_approve_transition_id.setter
    def shared_approve_transition_id(self, shared_approve_transition_id):
        """Sets the shared_approve_transition_id of this TransitionThresholdApproval.


        :param shared_approve_transition_id: The shared_approve_transition_id of this TransitionThresholdApproval.  # noqa: E501
        :type: int
        """

        self._shared_approve_transition_id = shared_approve_transition_id

    @property
    def operation(self):
        """Gets the operation of this TransitionThresholdApproval.  # noqa: E501


        :return: The operation of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this TransitionThresholdApproval.


        :param operation: The operation of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def created_by(self):
        """Gets the created_by of this TransitionThresholdApproval.  # noqa: E501


        :return: The created_by of this TransitionThresholdApproval.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransitionThresholdApproval.


        :param created_by: The created_by of this TransitionThresholdApproval.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def custom_values(self):
        """Gets the custom_values of this TransitionThresholdApproval.  # noqa: E501


        :return: The custom_values of this TransitionThresholdApproval.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this TransitionThresholdApproval.


        :param custom_values: The custom_values of this TransitionThresholdApproval.  # noqa: E501
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
        if issubclass(TransitionThresholdApproval, dict):
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
        if not isinstance(other, TransitionThresholdApproval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
