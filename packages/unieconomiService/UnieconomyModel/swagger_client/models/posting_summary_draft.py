# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PostingSummaryDraft(object):
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
        'draft_with_dims_on_balance': 'str',
        'payroll_id': 'int',
        'job_info_id': 'int',
        'status': 'str',
        'draft_with_dims': 'str',
        'id': 'int',
        'draft_basic': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'draft_with_dims_on_balance': 'draftWithDimsOnBalance',
        'payroll_id': 'PayrollID',
        'job_info_id': 'JobInfoID',
        'status': 'status',
        'draft_with_dims': 'draftWithDims',
        'id': 'ID',
        'draft_basic': 'draftBasic',
        'custom_values': 'CustomValues'
    }

    def __init__(self, draft_with_dims_on_balance=None, payroll_id=None, job_info_id=None, status=None, draft_with_dims=None, id=None, draft_basic=None, custom_values=None):  # noqa: E501
        """PostingSummaryDraft - a model defined in Swagger"""  # noqa: E501
        self._draft_with_dims_on_balance = None
        self._payroll_id = None
        self._job_info_id = None
        self._status = None
        self._draft_with_dims = None
        self._id = None
        self._draft_basic = None
        self._custom_values = None
        self.discriminator = None
        if draft_with_dims_on_balance is not None:
            self.draft_with_dims_on_balance = draft_with_dims_on_balance
        if payroll_id is not None:
            self.payroll_id = payroll_id
        if job_info_id is not None:
            self.job_info_id = job_info_id
        if status is not None:
            self.status = status
        if draft_with_dims is not None:
            self.draft_with_dims = draft_with_dims
        if id is not None:
            self.id = id
        if draft_basic is not None:
            self.draft_basic = draft_basic
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def draft_with_dims_on_balance(self):
        """Gets the draft_with_dims_on_balance of this PostingSummaryDraft.  # noqa: E501


        :return: The draft_with_dims_on_balance of this PostingSummaryDraft.  # noqa: E501
        :rtype: str
        """
        return self._draft_with_dims_on_balance

    @draft_with_dims_on_balance.setter
    def draft_with_dims_on_balance(self, draft_with_dims_on_balance):
        """Sets the draft_with_dims_on_balance of this PostingSummaryDraft.


        :param draft_with_dims_on_balance: The draft_with_dims_on_balance of this PostingSummaryDraft.  # noqa: E501
        :type: str
        """

        self._draft_with_dims_on_balance = draft_with_dims_on_balance

    @property
    def payroll_id(self):
        """Gets the payroll_id of this PostingSummaryDraft.  # noqa: E501


        :return: The payroll_id of this PostingSummaryDraft.  # noqa: E501
        :rtype: int
        """
        return self._payroll_id

    @payroll_id.setter
    def payroll_id(self, payroll_id):
        """Sets the payroll_id of this PostingSummaryDraft.


        :param payroll_id: The payroll_id of this PostingSummaryDraft.  # noqa: E501
        :type: int
        """

        self._payroll_id = payroll_id

    @property
    def job_info_id(self):
        """Gets the job_info_id of this PostingSummaryDraft.  # noqa: E501


        :return: The job_info_id of this PostingSummaryDraft.  # noqa: E501
        :rtype: int
        """
        return self._job_info_id

    @job_info_id.setter
    def job_info_id(self, job_info_id):
        """Sets the job_info_id of this PostingSummaryDraft.


        :param job_info_id: The job_info_id of this PostingSummaryDraft.  # noqa: E501
        :type: int
        """

        self._job_info_id = job_info_id

    @property
    def status(self):
        """Gets the status of this PostingSummaryDraft.  # noqa: E501


        :return: The status of this PostingSummaryDraft.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostingSummaryDraft.


        :param status: The status of this PostingSummaryDraft.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def draft_with_dims(self):
        """Gets the draft_with_dims of this PostingSummaryDraft.  # noqa: E501


        :return: The draft_with_dims of this PostingSummaryDraft.  # noqa: E501
        :rtype: str
        """
        return self._draft_with_dims

    @draft_with_dims.setter
    def draft_with_dims(self, draft_with_dims):
        """Sets the draft_with_dims of this PostingSummaryDraft.


        :param draft_with_dims: The draft_with_dims of this PostingSummaryDraft.  # noqa: E501
        :type: str
        """

        self._draft_with_dims = draft_with_dims

    @property
    def id(self):
        """Gets the id of this PostingSummaryDraft.  # noqa: E501


        :return: The id of this PostingSummaryDraft.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostingSummaryDraft.


        :param id: The id of this PostingSummaryDraft.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def draft_basic(self):
        """Gets the draft_basic of this PostingSummaryDraft.  # noqa: E501


        :return: The draft_basic of this PostingSummaryDraft.  # noqa: E501
        :rtype: str
        """
        return self._draft_basic

    @draft_basic.setter
    def draft_basic(self, draft_basic):
        """Sets the draft_basic of this PostingSummaryDraft.


        :param draft_basic: The draft_basic of this PostingSummaryDraft.  # noqa: E501
        :type: str
        """

        self._draft_basic = draft_basic

    @property
    def custom_values(self):
        """Gets the custom_values of this PostingSummaryDraft.  # noqa: E501


        :return: The custom_values of this PostingSummaryDraft.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this PostingSummaryDraft.


        :param custom_values: The custom_values of this PostingSummaryDraft.  # noqa: E501
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
        if issubclass(PostingSummaryDraft, dict):
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
        if not isinstance(other, PostingSummaryDraft):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
