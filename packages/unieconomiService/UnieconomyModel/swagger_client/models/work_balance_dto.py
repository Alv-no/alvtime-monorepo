# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkBalanceDto(object):
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
        'sum_overtime': 'int',
        'minutes': 'int',
        'description': 'str',
        'balancetype': 'str',
        'is_start_balance': 'bool',
        'last_day_expected': 'int',
        'work_relation_id': 'int',
        'valid_time_off': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'last_day_actual': 'int',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'actual_minutes': 'int',
        'expected_minutes': 'int',
        'previous': 'BalanceInfo',
        'details': 'list[FlexDetail]',
        'work_relation': 'WorkRelation',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'sum_overtime': 'SumOvertime',
        'minutes': 'Minutes',
        'description': 'Description',
        'balancetype': 'Balancetype',
        'is_start_balance': 'IsStartBalance',
        'last_day_expected': 'LastDayExpected',
        'work_relation_id': 'WorkRelationID',
        'valid_time_off': 'ValidTimeOff',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'last_day_actual': 'LastDayActual',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'actual_minutes': 'ActualMinutes',
        'expected_minutes': 'ExpectedMinutes',
        'previous': 'Previous',
        'details': 'Details',
        'work_relation': 'WorkRelation',
        'custom_values': 'CustomValues'
    }

    def __init__(self, sum_overtime=None, minutes=None, description=None, balancetype=None, is_start_balance=None, last_day_expected=None, work_relation_id=None, valid_time_off=None, status_code=None, deleted=None, last_day_actual=None, id=None, updated_by=None, created_by=None, actual_minutes=None, expected_minutes=None, previous=None, details=None, work_relation=None, custom_values=None):  # noqa: E501
        """WorkBalanceDto - a model defined in Swagger"""  # noqa: E501
        self._sum_overtime = None
        self._minutes = None
        self._description = None
        self._balancetype = None
        self._is_start_balance = None
        self._last_day_expected = None
        self._work_relation_id = None
        self._valid_time_off = None
        self._status_code = None
        self._deleted = None
        self._last_day_actual = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._actual_minutes = None
        self._expected_minutes = None
        self._previous = None
        self._details = None
        self._work_relation = None
        self._custom_values = None
        self.discriminator = None
        if sum_overtime is not None:
            self.sum_overtime = sum_overtime
        if minutes is not None:
            self.minutes = minutes
        if description is not None:
            self.description = description
        if balancetype is not None:
            self.balancetype = balancetype
        if is_start_balance is not None:
            self.is_start_balance = is_start_balance
        if last_day_expected is not None:
            self.last_day_expected = last_day_expected
        if work_relation_id is not None:
            self.work_relation_id = work_relation_id
        if valid_time_off is not None:
            self.valid_time_off = valid_time_off
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if last_day_actual is not None:
            self.last_day_actual = last_day_actual
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if actual_minutes is not None:
            self.actual_minutes = actual_minutes
        if expected_minutes is not None:
            self.expected_minutes = expected_minutes
        if previous is not None:
            self.previous = previous
        if details is not None:
            self.details = details
        if work_relation is not None:
            self.work_relation = work_relation
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def sum_overtime(self):
        """Gets the sum_overtime of this WorkBalanceDto.  # noqa: E501


        :return: The sum_overtime of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._sum_overtime

    @sum_overtime.setter
    def sum_overtime(self, sum_overtime):
        """Sets the sum_overtime of this WorkBalanceDto.


        :param sum_overtime: The sum_overtime of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._sum_overtime = sum_overtime

    @property
    def minutes(self):
        """Gets the minutes of this WorkBalanceDto.  # noqa: E501


        :return: The minutes of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this WorkBalanceDto.


        :param minutes: The minutes of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def description(self):
        """Gets the description of this WorkBalanceDto.  # noqa: E501


        :return: The description of this WorkBalanceDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkBalanceDto.


        :param description: The description of this WorkBalanceDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def balancetype(self):
        """Gets the balancetype of this WorkBalanceDto.  # noqa: E501


        :return: The balancetype of this WorkBalanceDto.  # noqa: E501
        :rtype: str
        """
        return self._balancetype

    @balancetype.setter
    def balancetype(self, balancetype):
        """Sets the balancetype of this WorkBalanceDto.


        :param balancetype: The balancetype of this WorkBalanceDto.  # noqa: E501
        :type: str
        """

        self._balancetype = balancetype

    @property
    def is_start_balance(self):
        """Gets the is_start_balance of this WorkBalanceDto.  # noqa: E501


        :return: The is_start_balance of this WorkBalanceDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_start_balance

    @is_start_balance.setter
    def is_start_balance(self, is_start_balance):
        """Sets the is_start_balance of this WorkBalanceDto.


        :param is_start_balance: The is_start_balance of this WorkBalanceDto.  # noqa: E501
        :type: bool
        """

        self._is_start_balance = is_start_balance

    @property
    def last_day_expected(self):
        """Gets the last_day_expected of this WorkBalanceDto.  # noqa: E501


        :return: The last_day_expected of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._last_day_expected

    @last_day_expected.setter
    def last_day_expected(self, last_day_expected):
        """Sets the last_day_expected of this WorkBalanceDto.


        :param last_day_expected: The last_day_expected of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._last_day_expected = last_day_expected

    @property
    def work_relation_id(self):
        """Gets the work_relation_id of this WorkBalanceDto.  # noqa: E501


        :return: The work_relation_id of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._work_relation_id

    @work_relation_id.setter
    def work_relation_id(self, work_relation_id):
        """Sets the work_relation_id of this WorkBalanceDto.


        :param work_relation_id: The work_relation_id of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._work_relation_id = work_relation_id

    @property
    def valid_time_off(self):
        """Gets the valid_time_off of this WorkBalanceDto.  # noqa: E501


        :return: The valid_time_off of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._valid_time_off

    @valid_time_off.setter
    def valid_time_off(self, valid_time_off):
        """Sets the valid_time_off of this WorkBalanceDto.


        :param valid_time_off: The valid_time_off of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._valid_time_off = valid_time_off

    @property
    def status_code(self):
        """Gets the status_code of this WorkBalanceDto.  # noqa: E501


        :return: The status_code of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this WorkBalanceDto.


        :param status_code: The status_code of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this WorkBalanceDto.  # noqa: E501


        :return: The deleted of this WorkBalanceDto.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this WorkBalanceDto.


        :param deleted: The deleted of this WorkBalanceDto.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def last_day_actual(self):
        """Gets the last_day_actual of this WorkBalanceDto.  # noqa: E501


        :return: The last_day_actual of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._last_day_actual

    @last_day_actual.setter
    def last_day_actual(self, last_day_actual):
        """Sets the last_day_actual of this WorkBalanceDto.


        :param last_day_actual: The last_day_actual of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._last_day_actual = last_day_actual

    @property
    def id(self):
        """Gets the id of this WorkBalanceDto.  # noqa: E501


        :return: The id of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkBalanceDto.


        :param id: The id of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this WorkBalanceDto.  # noqa: E501


        :return: The updated_by of this WorkBalanceDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this WorkBalanceDto.


        :param updated_by: The updated_by of this WorkBalanceDto.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this WorkBalanceDto.  # noqa: E501


        :return: The created_by of this WorkBalanceDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkBalanceDto.


        :param created_by: The created_by of this WorkBalanceDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def actual_minutes(self):
        """Gets the actual_minutes of this WorkBalanceDto.  # noqa: E501


        :return: The actual_minutes of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._actual_minutes

    @actual_minutes.setter
    def actual_minutes(self, actual_minutes):
        """Sets the actual_minutes of this WorkBalanceDto.


        :param actual_minutes: The actual_minutes of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._actual_minutes = actual_minutes

    @property
    def expected_minutes(self):
        """Gets the expected_minutes of this WorkBalanceDto.  # noqa: E501


        :return: The expected_minutes of this WorkBalanceDto.  # noqa: E501
        :rtype: int
        """
        return self._expected_minutes

    @expected_minutes.setter
    def expected_minutes(self, expected_minutes):
        """Sets the expected_minutes of this WorkBalanceDto.


        :param expected_minutes: The expected_minutes of this WorkBalanceDto.  # noqa: E501
        :type: int
        """

        self._expected_minutes = expected_minutes

    @property
    def previous(self):
        """Gets the previous of this WorkBalanceDto.  # noqa: E501


        :return: The previous of this WorkBalanceDto.  # noqa: E501
        :rtype: BalanceInfo
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this WorkBalanceDto.


        :param previous: The previous of this WorkBalanceDto.  # noqa: E501
        :type: BalanceInfo
        """

        self._previous = previous

    @property
    def details(self):
        """Gets the details of this WorkBalanceDto.  # noqa: E501


        :return: The details of this WorkBalanceDto.  # noqa: E501
        :rtype: list[FlexDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this WorkBalanceDto.


        :param details: The details of this WorkBalanceDto.  # noqa: E501
        :type: list[FlexDetail]
        """

        self._details = details

    @property
    def work_relation(self):
        """Gets the work_relation of this WorkBalanceDto.  # noqa: E501


        :return: The work_relation of this WorkBalanceDto.  # noqa: E501
        :rtype: WorkRelation
        """
        return self._work_relation

    @work_relation.setter
    def work_relation(self, work_relation):
        """Sets the work_relation of this WorkBalanceDto.


        :param work_relation: The work_relation of this WorkBalanceDto.  # noqa: E501
        :type: WorkRelation
        """

        self._work_relation = work_relation

    @property
    def custom_values(self):
        """Gets the custom_values of this WorkBalanceDto.  # noqa: E501


        :return: The custom_values of this WorkBalanceDto.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this WorkBalanceDto.


        :param custom_values: The custom_values of this WorkBalanceDto.  # noqa: E501
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
        if issubclass(WorkBalanceDto, dict):
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
        if not isinstance(other, WorkBalanceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
