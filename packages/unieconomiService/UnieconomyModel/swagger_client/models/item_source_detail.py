# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemSourceDetail(object):
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
        'description': 'str',
        'status_code': 'int',
        'deleted': 'bool',
        'id': 'int',
        'source_fk': 'int',
        'updated_by': 'str',
        'source_type': 'str',
        'tag': 'str',
        'created_by': 'str',
        'item_source_id': 'int',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'description': 'Description',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'id': 'ID',
        'source_fk': 'SourceFK',
        'updated_by': 'UpdatedBy',
        'source_type': 'SourceType',
        'tag': 'Tag',
        'created_by': 'CreatedBy',
        'item_source_id': 'ItemSourceID',
        'custom_values': 'CustomValues'
    }

    def __init__(self, description=None, status_code=None, deleted=None, id=None, source_fk=None, updated_by=None, source_type=None, tag=None, created_by=None, item_source_id=None, custom_values=None):  # noqa: E501
        """ItemSourceDetail - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._status_code = None
        self._deleted = None
        self._id = None
        self._source_fk = None
        self._updated_by = None
        self._source_type = None
        self._tag = None
        self._created_by = None
        self._item_source_id = None
        self._custom_values = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if source_fk is not None:
            self.source_fk = source_fk
        if updated_by is not None:
            self.updated_by = updated_by
        if source_type is not None:
            self.source_type = source_type
        if tag is not None:
            self.tag = tag
        if created_by is not None:
            self.created_by = created_by
        if item_source_id is not None:
            self.item_source_id = item_source_id
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def description(self):
        """Gets the description of this ItemSourceDetail.  # noqa: E501


        :return: The description of this ItemSourceDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemSourceDetail.


        :param description: The description of this ItemSourceDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status_code(self):
        """Gets the status_code of this ItemSourceDetail.  # noqa: E501


        :return: The status_code of this ItemSourceDetail.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ItemSourceDetail.


        :param status_code: The status_code of this ItemSourceDetail.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this ItemSourceDetail.  # noqa: E501


        :return: The deleted of this ItemSourceDetail.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ItemSourceDetail.


        :param deleted: The deleted of this ItemSourceDetail.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this ItemSourceDetail.  # noqa: E501


        :return: The id of this ItemSourceDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemSourceDetail.


        :param id: The id of this ItemSourceDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def source_fk(self):
        """Gets the source_fk of this ItemSourceDetail.  # noqa: E501


        :return: The source_fk of this ItemSourceDetail.  # noqa: E501
        :rtype: int
        """
        return self._source_fk

    @source_fk.setter
    def source_fk(self, source_fk):
        """Sets the source_fk of this ItemSourceDetail.


        :param source_fk: The source_fk of this ItemSourceDetail.  # noqa: E501
        :type: int
        """

        self._source_fk = source_fk

    @property
    def updated_by(self):
        """Gets the updated_by of this ItemSourceDetail.  # noqa: E501


        :return: The updated_by of this ItemSourceDetail.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ItemSourceDetail.


        :param updated_by: The updated_by of this ItemSourceDetail.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def source_type(self):
        """Gets the source_type of this ItemSourceDetail.  # noqa: E501


        :return: The source_type of this ItemSourceDetail.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ItemSourceDetail.


        :param source_type: The source_type of this ItemSourceDetail.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def tag(self):
        """Gets the tag of this ItemSourceDetail.  # noqa: E501


        :return: The tag of this ItemSourceDetail.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ItemSourceDetail.


        :param tag: The tag of this ItemSourceDetail.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def created_by(self):
        """Gets the created_by of this ItemSourceDetail.  # noqa: E501


        :return: The created_by of this ItemSourceDetail.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ItemSourceDetail.


        :param created_by: The created_by of this ItemSourceDetail.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def item_source_id(self):
        """Gets the item_source_id of this ItemSourceDetail.  # noqa: E501


        :return: The item_source_id of this ItemSourceDetail.  # noqa: E501
        :rtype: int
        """
        return self._item_source_id

    @item_source_id.setter
    def item_source_id(self, item_source_id):
        """Sets the item_source_id of this ItemSourceDetail.


        :param item_source_id: The item_source_id of this ItemSourceDetail.  # noqa: E501
        :type: int
        """

        self._item_source_id = item_source_id

    @property
    def custom_values(self):
        """Gets the custom_values of this ItemSourceDetail.  # noqa: E501


        :return: The custom_values of this ItemSourceDetail.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ItemSourceDetail.


        :param custom_values: The custom_values of this ItemSourceDetail.  # noqa: E501
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
        if issubclass(ItemSourceDetail, dict):
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
        if not isinstance(other, ItemSourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
