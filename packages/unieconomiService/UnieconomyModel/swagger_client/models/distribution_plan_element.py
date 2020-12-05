# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DistributionPlanElement(object):
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
        'priority': 'int',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'distribution_plan_id': 'int',
        'distribution_plan_element_type_id': 'int',
        'element_type': 'DistributionPlanElementType',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'priority': 'Priority',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'distribution_plan_id': 'DistributionPlanID',
        'distribution_plan_element_type_id': 'DistributionPlanElementTypeID',
        'element_type': 'ElementType',
        'custom_values': 'CustomValues'
    }

    def __init__(self, status_code=None, deleted=None, priority=None, id=None, updated_by=None, created_by=None, distribution_plan_id=None, distribution_plan_element_type_id=None, element_type=None, custom_values=None):  # noqa: E501
        """DistributionPlanElement - a model defined in Swagger"""  # noqa: E501
        self._status_code = None
        self._deleted = None
        self._priority = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._distribution_plan_id = None
        self._distribution_plan_element_type_id = None
        self._element_type = None
        self._custom_values = None
        self.discriminator = None
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if priority is not None:
            self.priority = priority
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if distribution_plan_id is not None:
            self.distribution_plan_id = distribution_plan_id
        if distribution_plan_element_type_id is not None:
            self.distribution_plan_element_type_id = distribution_plan_element_type_id
        if element_type is not None:
            self.element_type = element_type
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def status_code(self):
        """Gets the status_code of this DistributionPlanElement.  # noqa: E501


        :return: The status_code of this DistributionPlanElement.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this DistributionPlanElement.


        :param status_code: The status_code of this DistributionPlanElement.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this DistributionPlanElement.  # noqa: E501


        :return: The deleted of this DistributionPlanElement.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DistributionPlanElement.


        :param deleted: The deleted of this DistributionPlanElement.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def priority(self):
        """Gets the priority of this DistributionPlanElement.  # noqa: E501


        :return: The priority of this DistributionPlanElement.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DistributionPlanElement.


        :param priority: The priority of this DistributionPlanElement.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def id(self):
        """Gets the id of this DistributionPlanElement.  # noqa: E501


        :return: The id of this DistributionPlanElement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionPlanElement.


        :param id: The id of this DistributionPlanElement.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this DistributionPlanElement.  # noqa: E501


        :return: The updated_by of this DistributionPlanElement.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this DistributionPlanElement.


        :param updated_by: The updated_by of this DistributionPlanElement.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this DistributionPlanElement.  # noqa: E501


        :return: The created_by of this DistributionPlanElement.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DistributionPlanElement.


        :param created_by: The created_by of this DistributionPlanElement.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def distribution_plan_id(self):
        """Gets the distribution_plan_id of this DistributionPlanElement.  # noqa: E501


        :return: The distribution_plan_id of this DistributionPlanElement.  # noqa: E501
        :rtype: int
        """
        return self._distribution_plan_id

    @distribution_plan_id.setter
    def distribution_plan_id(self, distribution_plan_id):
        """Sets the distribution_plan_id of this DistributionPlanElement.


        :param distribution_plan_id: The distribution_plan_id of this DistributionPlanElement.  # noqa: E501
        :type: int
        """

        self._distribution_plan_id = distribution_plan_id

    @property
    def distribution_plan_element_type_id(self):
        """Gets the distribution_plan_element_type_id of this DistributionPlanElement.  # noqa: E501


        :return: The distribution_plan_element_type_id of this DistributionPlanElement.  # noqa: E501
        :rtype: int
        """
        return self._distribution_plan_element_type_id

    @distribution_plan_element_type_id.setter
    def distribution_plan_element_type_id(self, distribution_plan_element_type_id):
        """Sets the distribution_plan_element_type_id of this DistributionPlanElement.


        :param distribution_plan_element_type_id: The distribution_plan_element_type_id of this DistributionPlanElement.  # noqa: E501
        :type: int
        """

        self._distribution_plan_element_type_id = distribution_plan_element_type_id

    @property
    def element_type(self):
        """Gets the element_type of this DistributionPlanElement.  # noqa: E501


        :return: The element_type of this DistributionPlanElement.  # noqa: E501
        :rtype: DistributionPlanElementType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this DistributionPlanElement.


        :param element_type: The element_type of this DistributionPlanElement.  # noqa: E501
        :type: DistributionPlanElementType
        """

        self._element_type = element_type

    @property
    def custom_values(self):
        """Gets the custom_values of this DistributionPlanElement.  # noqa: E501


        :return: The custom_values of this DistributionPlanElement.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this DistributionPlanElement.


        :param custom_values: The custom_values of this DistributionPlanElement.  # noqa: E501
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
        if issubclass(DistributionPlanElement, dict):
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
        if not isinstance(other, DistributionPlanElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
