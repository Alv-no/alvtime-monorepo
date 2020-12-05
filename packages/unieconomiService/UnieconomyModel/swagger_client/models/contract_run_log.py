# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ContractRunLog(object):
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
        'status_code': 'int',
        'deleted': 'bool',
        'contract_id': 'int',
        'type': 'str',
        'contract_trigger_id': 'int',
        'run_time': 'str',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'contract': 'Contract',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'message': 'Message',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'contract_id': 'ContractID',
        'type': 'Type',
        'contract_trigger_id': 'ContractTriggerID',
        'run_time': 'RunTime',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'contract': 'Contract',
        'custom_values': 'CustomValues'
    }

    def __init__(self, message=None, status_code=None, deleted=None, contract_id=None, type=None, contract_trigger_id=None, run_time=None, id=None, updated_by=None, created_by=None, contract=None, custom_values=None):  # noqa: E501
        """ContractRunLog - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._status_code = None
        self._deleted = None
        self._contract_id = None
        self._type = None
        self._contract_trigger_id = None
        self._run_time = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._contract = None
        self._custom_values = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if contract_id is not None:
            self.contract_id = contract_id
        if type is not None:
            self.type = type
        if contract_trigger_id is not None:
            self.contract_trigger_id = contract_trigger_id
        if run_time is not None:
            self.run_time = run_time
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if contract is not None:
            self.contract = contract
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def message(self):
        """Gets the message of this ContractRunLog.  # noqa: E501


        :return: The message of this ContractRunLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ContractRunLog.


        :param message: The message of this ContractRunLog.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status_code(self):
        """Gets the status_code of this ContractRunLog.  # noqa: E501


        :return: The status_code of this ContractRunLog.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ContractRunLog.


        :param status_code: The status_code of this ContractRunLog.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this ContractRunLog.  # noqa: E501


        :return: The deleted of this ContractRunLog.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ContractRunLog.


        :param deleted: The deleted of this ContractRunLog.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractRunLog.  # noqa: E501


        :return: The contract_id of this ContractRunLog.  # noqa: E501
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractRunLog.


        :param contract_id: The contract_id of this ContractRunLog.  # noqa: E501
        :type: int
        """

        self._contract_id = contract_id

    @property
    def type(self):
        """Gets the type of this ContractRunLog.  # noqa: E501


        :return: The type of this ContractRunLog.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContractRunLog.


        :param type: The type of this ContractRunLog.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def contract_trigger_id(self):
        """Gets the contract_trigger_id of this ContractRunLog.  # noqa: E501


        :return: The contract_trigger_id of this ContractRunLog.  # noqa: E501
        :rtype: int
        """
        return self._contract_trigger_id

    @contract_trigger_id.setter
    def contract_trigger_id(self, contract_trigger_id):
        """Sets the contract_trigger_id of this ContractRunLog.


        :param contract_trigger_id: The contract_trigger_id of this ContractRunLog.  # noqa: E501
        :type: int
        """

        self._contract_trigger_id = contract_trigger_id

    @property
    def run_time(self):
        """Gets the run_time of this ContractRunLog.  # noqa: E501


        :return: The run_time of this ContractRunLog.  # noqa: E501
        :rtype: str
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        """Sets the run_time of this ContractRunLog.


        :param run_time: The run_time of this ContractRunLog.  # noqa: E501
        :type: str
        """

        self._run_time = run_time

    @property
    def id(self):
        """Gets the id of this ContractRunLog.  # noqa: E501


        :return: The id of this ContractRunLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContractRunLog.


        :param id: The id of this ContractRunLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this ContractRunLog.  # noqa: E501


        :return: The updated_by of this ContractRunLog.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ContractRunLog.


        :param updated_by: The updated_by of this ContractRunLog.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this ContractRunLog.  # noqa: E501


        :return: The created_by of this ContractRunLog.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ContractRunLog.


        :param created_by: The created_by of this ContractRunLog.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def contract(self):
        """Gets the contract of this ContractRunLog.  # noqa: E501


        :return: The contract of this ContractRunLog.  # noqa: E501
        :rtype: Contract
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this ContractRunLog.


        :param contract: The contract of this ContractRunLog.  # noqa: E501
        :type: Contract
        """

        self._contract = contract

    @property
    def custom_values(self):
        """Gets the custom_values of this ContractRunLog.  # noqa: E501


        :return: The custom_values of this ContractRunLog.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ContractRunLog.


        :param custom_values: The custom_values of this ContractRunLog.  # noqa: E501
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
        if issubclass(ContractRunLog, dict):
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
        if not isinstance(other, ContractRunLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
