# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Model(object):
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
        'shared': 'bool',
        'label': 'str',
        'admin': 'bool',
        'description': 'str',
        'name': 'str',
        'deleted': 'bool',
        'label_plural': 'str',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'fields': 'list[Field]',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'shared': 'Shared',
        'label': 'Label',
        'admin': 'Admin',
        'description': 'Description',
        'name': 'Name',
        'deleted': 'Deleted',
        'label_plural': 'LabelPlural',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'fields': 'Fields',
        'custom_values': 'CustomValues'
    }

    def __init__(self, shared=None, label=None, admin=None, description=None, name=None, deleted=None, label_plural=None, id=None, updated_by=None, created_by=None, fields=None, custom_values=None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501
        self._shared = None
        self._label = None
        self._admin = None
        self._description = None
        self._name = None
        self._deleted = None
        self._label_plural = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._fields = None
        self._custom_values = None
        self.discriminator = None
        if shared is not None:
            self.shared = shared
        if label is not None:
            self.label = label
        if admin is not None:
            self.admin = admin
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if deleted is not None:
            self.deleted = deleted
        if label_plural is not None:
            self.label_plural = label_plural
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if fields is not None:
            self.fields = fields
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def shared(self):
        """Gets the shared of this Model.  # noqa: E501


        :return: The shared of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Model.


        :param shared: The shared of this Model.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def label(self):
        """Gets the label of this Model.  # noqa: E501


        :return: The label of this Model.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Model.


        :param label: The label of this Model.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def admin(self):
        """Gets the admin of this Model.  # noqa: E501


        :return: The admin of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Model.


        :param admin: The admin of this Model.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def description(self):
        """Gets the description of this Model.  # noqa: E501


        :return: The description of this Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.


        :param description: The description of this Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this Model.  # noqa: E501


        :return: The name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.


        :param name: The name of this Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deleted(self):
        """Gets the deleted of this Model.  # noqa: E501


        :return: The deleted of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Model.


        :param deleted: The deleted of this Model.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def label_plural(self):
        """Gets the label_plural of this Model.  # noqa: E501


        :return: The label_plural of this Model.  # noqa: E501
        :rtype: str
        """
        return self._label_plural

    @label_plural.setter
    def label_plural(self, label_plural):
        """Sets the label_plural of this Model.


        :param label_plural: The label_plural of this Model.  # noqa: E501
        :type: str
        """

        self._label_plural = label_plural

    @property
    def id(self):
        """Gets the id of this Model.  # noqa: E501


        :return: The id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.


        :param id: The id of this Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this Model.  # noqa: E501


        :return: The updated_by of this Model.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Model.


        :param updated_by: The updated_by of this Model.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this Model.  # noqa: E501


        :return: The created_by of this Model.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Model.


        :param created_by: The created_by of this Model.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def fields(self):
        """Gets the fields of this Model.  # noqa: E501


        :return: The fields of this Model.  # noqa: E501
        :rtype: list[Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Model.


        :param fields: The fields of this Model.  # noqa: E501
        :type: list[Field]
        """

        self._fields = fields

    @property
    def custom_values(self):
        """Gets the custom_values of this Model.  # noqa: E501


        :return: The custom_values of this Model.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Model.


        :param custom_values: The custom_values of this Model.  # noqa: E501
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
        if issubclass(Model, dict):
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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
