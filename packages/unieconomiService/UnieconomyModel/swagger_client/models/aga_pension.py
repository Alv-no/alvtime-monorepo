# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AGAPension(object):
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
        'aga_rate_id': 'int',
        'zone': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'aga_calculation_id': 'int',
        'id': 'int',
        'beregnings_kode': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'sub_entity_id': 'int',
        'sub_entity': 'SubEntity',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'aga_rate_id': 'AGARateID',
        'zone': 'zone',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'aga_calculation_id': 'AGACalculationID',
        'id': 'ID',
        'beregnings_kode': 'beregningsKode',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'sub_entity_id': 'SubEntityID',
        'sub_entity': 'subEntity',
        'custom_values': 'CustomValues'
    }

    def __init__(self, aga_rate_id=None, zone=None, status_code=None, deleted=None, aga_calculation_id=None, id=None, beregnings_kode=None, updated_by=None, created_by=None, sub_entity_id=None, sub_entity=None, custom_values=None):  # noqa: E501
        """AGAPension - a model defined in Swagger"""  # noqa: E501
        self._aga_rate_id = None
        self._zone = None
        self._status_code = None
        self._deleted = None
        self._aga_calculation_id = None
        self._id = None
        self._beregnings_kode = None
        self._updated_by = None
        self._created_by = None
        self._sub_entity_id = None
        self._sub_entity = None
        self._custom_values = None
        self.discriminator = None
        if aga_rate_id is not None:
            self.aga_rate_id = aga_rate_id
        if zone is not None:
            self.zone = zone
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if aga_calculation_id is not None:
            self.aga_calculation_id = aga_calculation_id
        if id is not None:
            self.id = id
        if beregnings_kode is not None:
            self.beregnings_kode = beregnings_kode
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if sub_entity_id is not None:
            self.sub_entity_id = sub_entity_id
        if sub_entity is not None:
            self.sub_entity = sub_entity
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def aga_rate_id(self):
        """Gets the aga_rate_id of this AGAPension.  # noqa: E501


        :return: The aga_rate_id of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._aga_rate_id

    @aga_rate_id.setter
    def aga_rate_id(self, aga_rate_id):
        """Sets the aga_rate_id of this AGAPension.


        :param aga_rate_id: The aga_rate_id of this AGAPension.  # noqa: E501
        :type: int
        """

        self._aga_rate_id = aga_rate_id

    @property
    def zone(self):
        """Gets the zone of this AGAPension.  # noqa: E501


        :return: The zone of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this AGAPension.


        :param zone: The zone of this AGAPension.  # noqa: E501
        :type: int
        """

        self._zone = zone

    @property
    def status_code(self):
        """Gets the status_code of this AGAPension.  # noqa: E501


        :return: The status_code of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this AGAPension.


        :param status_code: The status_code of this AGAPension.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this AGAPension.  # noqa: E501


        :return: The deleted of this AGAPension.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AGAPension.


        :param deleted: The deleted of this AGAPension.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def aga_calculation_id(self):
        """Gets the aga_calculation_id of this AGAPension.  # noqa: E501


        :return: The aga_calculation_id of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._aga_calculation_id

    @aga_calculation_id.setter
    def aga_calculation_id(self, aga_calculation_id):
        """Sets the aga_calculation_id of this AGAPension.


        :param aga_calculation_id: The aga_calculation_id of this AGAPension.  # noqa: E501
        :type: int
        """

        self._aga_calculation_id = aga_calculation_id

    @property
    def id(self):
        """Gets the id of this AGAPension.  # noqa: E501


        :return: The id of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AGAPension.


        :param id: The id of this AGAPension.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def beregnings_kode(self):
        """Gets the beregnings_kode of this AGAPension.  # noqa: E501


        :return: The beregnings_kode of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._beregnings_kode

    @beregnings_kode.setter
    def beregnings_kode(self, beregnings_kode):
        """Sets the beregnings_kode of this AGAPension.


        :param beregnings_kode: The beregnings_kode of this AGAPension.  # noqa: E501
        :type: int
        """

        self._beregnings_kode = beregnings_kode

    @property
    def updated_by(self):
        """Gets the updated_by of this AGAPension.  # noqa: E501


        :return: The updated_by of this AGAPension.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AGAPension.


        :param updated_by: The updated_by of this AGAPension.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this AGAPension.  # noqa: E501


        :return: The created_by of this AGAPension.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AGAPension.


        :param created_by: The created_by of this AGAPension.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def sub_entity_id(self):
        """Gets the sub_entity_id of this AGAPension.  # noqa: E501


        :return: The sub_entity_id of this AGAPension.  # noqa: E501
        :rtype: int
        """
        return self._sub_entity_id

    @sub_entity_id.setter
    def sub_entity_id(self, sub_entity_id):
        """Sets the sub_entity_id of this AGAPension.


        :param sub_entity_id: The sub_entity_id of this AGAPension.  # noqa: E501
        :type: int
        """

        self._sub_entity_id = sub_entity_id

    @property
    def sub_entity(self):
        """Gets the sub_entity of this AGAPension.  # noqa: E501


        :return: The sub_entity of this AGAPension.  # noqa: E501
        :rtype: SubEntity
        """
        return self._sub_entity

    @sub_entity.setter
    def sub_entity(self, sub_entity):
        """Sets the sub_entity of this AGAPension.


        :param sub_entity: The sub_entity of this AGAPension.  # noqa: E501
        :type: SubEntity
        """

        self._sub_entity = sub_entity

    @property
    def custom_values(self):
        """Gets the custom_values of this AGAPension.  # noqa: E501


        :return: The custom_values of this AGAPension.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this AGAPension.


        :param custom_values: The custom_values of this AGAPension.  # noqa: E501
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
        if issubclass(AGAPension, dict):
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
        if not isinstance(other, AGAPension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
