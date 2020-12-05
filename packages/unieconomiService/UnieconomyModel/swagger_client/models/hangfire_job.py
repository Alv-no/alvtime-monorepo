# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HangfireJob(object):
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
        'completed': 'bool',
        'year': 'int',
        'company_key': 'str',
        'status': 'int',
        'has_error': 'bool',
        'id': 'int',
        'global_identity': 'str',
        'job_id': 'str',
        'company_id': 'int',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'completed': 'Completed',
        'year': 'Year',
        'company_key': 'CompanyKey',
        'status': 'Status',
        'has_error': 'HasError',
        'id': 'ID',
        'global_identity': 'GlobalIdentity',
        'job_id': 'JobId',
        'company_id': 'CompanyID',
        'custom_values': 'CustomValues'
    }

    def __init__(self, completed=None, year=None, company_key=None, status=None, has_error=None, id=None, global_identity=None, job_id=None, company_id=None, custom_values=None):  # noqa: E501
        """HangfireJob - a model defined in Swagger"""  # noqa: E501
        self._completed = None
        self._year = None
        self._company_key = None
        self._status = None
        self._has_error = None
        self._id = None
        self._global_identity = None
        self._job_id = None
        self._company_id = None
        self._custom_values = None
        self.discriminator = None
        if completed is not None:
            self.completed = completed
        if year is not None:
            self.year = year
        if company_key is not None:
            self.company_key = company_key
        if status is not None:
            self.status = status
        if has_error is not None:
            self.has_error = has_error
        if id is not None:
            self.id = id
        if global_identity is not None:
            self.global_identity = global_identity
        if job_id is not None:
            self.job_id = job_id
        if company_id is not None:
            self.company_id = company_id
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def completed(self):
        """Gets the completed of this HangfireJob.  # noqa: E501


        :return: The completed of this HangfireJob.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this HangfireJob.


        :param completed: The completed of this HangfireJob.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def year(self):
        """Gets the year of this HangfireJob.  # noqa: E501


        :return: The year of this HangfireJob.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this HangfireJob.


        :param year: The year of this HangfireJob.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def company_key(self):
        """Gets the company_key of this HangfireJob.  # noqa: E501


        :return: The company_key of this HangfireJob.  # noqa: E501
        :rtype: str
        """
        return self._company_key

    @company_key.setter
    def company_key(self, company_key):
        """Sets the company_key of this HangfireJob.


        :param company_key: The company_key of this HangfireJob.  # noqa: E501
        :type: str
        """

        self._company_key = company_key

    @property
    def status(self):
        """Gets the status of this HangfireJob.  # noqa: E501


        :return: The status of this HangfireJob.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HangfireJob.


        :param status: The status of this HangfireJob.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def has_error(self):
        """Gets the has_error of this HangfireJob.  # noqa: E501


        :return: The has_error of this HangfireJob.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this HangfireJob.


        :param has_error: The has_error of this HangfireJob.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    @property
    def id(self):
        """Gets the id of this HangfireJob.  # noqa: E501


        :return: The id of this HangfireJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HangfireJob.


        :param id: The id of this HangfireJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def global_identity(self):
        """Gets the global_identity of this HangfireJob.  # noqa: E501


        :return: The global_identity of this HangfireJob.  # noqa: E501
        :rtype: str
        """
        return self._global_identity

    @global_identity.setter
    def global_identity(self, global_identity):
        """Sets the global_identity of this HangfireJob.


        :param global_identity: The global_identity of this HangfireJob.  # noqa: E501
        :type: str
        """

        self._global_identity = global_identity

    @property
    def job_id(self):
        """Gets the job_id of this HangfireJob.  # noqa: E501


        :return: The job_id of this HangfireJob.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this HangfireJob.


        :param job_id: The job_id of this HangfireJob.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def company_id(self):
        """Gets the company_id of this HangfireJob.  # noqa: E501


        :return: The company_id of this HangfireJob.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this HangfireJob.


        :param company_id: The company_id of this HangfireJob.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def custom_values(self):
        """Gets the custom_values of this HangfireJob.  # noqa: E501


        :return: The custom_values of this HangfireJob.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this HangfireJob.


        :param custom_values: The custom_values of this HangfireJob.  # noqa: E501
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
        if issubclass(HangfireJob, dict):
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
        if not isinstance(other, HangfireJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
