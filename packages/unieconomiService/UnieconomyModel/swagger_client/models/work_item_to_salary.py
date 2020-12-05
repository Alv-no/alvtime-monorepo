# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkItemToSalary(object):
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
        'payroll_run_id': 'int',
        'wage_type': 'WageType',
        'employment': 'Employment',
        'work_items': 'list[WorkItem]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'payroll_run_id': 'PayrollRunID',
        'wage_type': 'WageType',
        'employment': 'Employment',
        'work_items': 'WorkItems',
        'custom_values': 'CustomValues'
    }

    def __init__(self, payroll_run_id=None, wage_type=None, employment=None, work_items=None, custom_values=None):  # noqa: E501
        """WorkItemToSalary - a model defined in Swagger"""  # noqa: E501
        self._payroll_run_id = None
        self._wage_type = None
        self._employment = None
        self._work_items = None
        self._custom_values = None
        self.discriminator = None
        if payroll_run_id is not None:
            self.payroll_run_id = payroll_run_id
        if wage_type is not None:
            self.wage_type = wage_type
        if employment is not None:
            self.employment = employment
        if work_items is not None:
            self.work_items = work_items
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def payroll_run_id(self):
        """Gets the payroll_run_id of this WorkItemToSalary.  # noqa: E501


        :return: The payroll_run_id of this WorkItemToSalary.  # noqa: E501
        :rtype: int
        """
        return self._payroll_run_id

    @payroll_run_id.setter
    def payroll_run_id(self, payroll_run_id):
        """Sets the payroll_run_id of this WorkItemToSalary.


        :param payroll_run_id: The payroll_run_id of this WorkItemToSalary.  # noqa: E501
        :type: int
        """

        self._payroll_run_id = payroll_run_id

    @property
    def wage_type(self):
        """Gets the wage_type of this WorkItemToSalary.  # noqa: E501


        :return: The wage_type of this WorkItemToSalary.  # noqa: E501
        :rtype: WageType
        """
        return self._wage_type

    @wage_type.setter
    def wage_type(self, wage_type):
        """Sets the wage_type of this WorkItemToSalary.


        :param wage_type: The wage_type of this WorkItemToSalary.  # noqa: E501
        :type: WageType
        """

        self._wage_type = wage_type

    @property
    def employment(self):
        """Gets the employment of this WorkItemToSalary.  # noqa: E501


        :return: The employment of this WorkItemToSalary.  # noqa: E501
        :rtype: Employment
        """
        return self._employment

    @employment.setter
    def employment(self, employment):
        """Sets the employment of this WorkItemToSalary.


        :param employment: The employment of this WorkItemToSalary.  # noqa: E501
        :type: Employment
        """

        self._employment = employment

    @property
    def work_items(self):
        """Gets the work_items of this WorkItemToSalary.  # noqa: E501


        :return: The work_items of this WorkItemToSalary.  # noqa: E501
        :rtype: list[WorkItem]
        """
        return self._work_items

    @work_items.setter
    def work_items(self, work_items):
        """Sets the work_items of this WorkItemToSalary.


        :param work_items: The work_items of this WorkItemToSalary.  # noqa: E501
        :type: list[WorkItem]
        """

        self._work_items = work_items

    @property
    def custom_values(self):
        """Gets the custom_values of this WorkItemToSalary.  # noqa: E501


        :return: The custom_values of this WorkItemToSalary.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this WorkItemToSalary.


        :param custom_values: The custom_values of this WorkItemToSalary.  # noqa: E501
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
        if issubclass(WorkItemToSalary, dict):
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
        if not isinstance(other, WorkItemToSalary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
