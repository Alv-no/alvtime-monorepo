# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ContractAddress(object):
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
        'entity_type': 'str',
        'contract_id': 'int',
        'type': 'str',
        'address': 'str',
        'contract_asset_id': 'int',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'entity_id': 'int',
        'asset_address': 'str',
        'contract': 'Contract',
        'contract_asset': 'ContractAsset',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'entity_type': 'EntityType',
        'contract_id': 'ContractID',
        'type': 'Type',
        'address': 'Address',
        'contract_asset_id': 'ContractAssetID',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'entity_id': 'EntityID',
        'asset_address': 'AssetAddress',
        'contract': 'Contract',
        'contract_asset': 'ContractAsset',
        'custom_values': 'CustomValues'
    }

    def __init__(self, status_code=None, deleted=None, entity_type=None, contract_id=None, type=None, address=None, contract_asset_id=None, id=None, updated_by=None, created_by=None, entity_id=None, asset_address=None, contract=None, contract_asset=None, custom_values=None):  # noqa: E501
        """ContractAddress - a model defined in Swagger"""  # noqa: E501
        self._status_code = None
        self._deleted = None
        self._entity_type = None
        self._contract_id = None
        self._type = None
        self._address = None
        self._contract_asset_id = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._entity_id = None
        self._asset_address = None
        self._contract = None
        self._contract_asset = None
        self._custom_values = None
        self.discriminator = None
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if entity_type is not None:
            self.entity_type = entity_type
        if contract_id is not None:
            self.contract_id = contract_id
        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if contract_asset_id is not None:
            self.contract_asset_id = contract_asset_id
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if entity_id is not None:
            self.entity_id = entity_id
        if asset_address is not None:
            self.asset_address = asset_address
        if contract is not None:
            self.contract = contract
        if contract_asset is not None:
            self.contract_asset = contract_asset
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def status_code(self):
        """Gets the status_code of this ContractAddress.  # noqa: E501


        :return: The status_code of this ContractAddress.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ContractAddress.


        :param status_code: The status_code of this ContractAddress.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this ContractAddress.  # noqa: E501


        :return: The deleted of this ContractAddress.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ContractAddress.


        :param deleted: The deleted of this ContractAddress.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def entity_type(self):
        """Gets the entity_type of this ContractAddress.  # noqa: E501


        :return: The entity_type of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ContractAddress.


        :param entity_type: The entity_type of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractAddress.  # noqa: E501


        :return: The contract_id of this ContractAddress.  # noqa: E501
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractAddress.


        :param contract_id: The contract_id of this ContractAddress.  # noqa: E501
        :type: int
        """

        self._contract_id = contract_id

    @property
    def type(self):
        """Gets the type of this ContractAddress.  # noqa: E501


        :return: The type of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContractAddress.


        :param type: The type of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """Gets the address of this ContractAddress.  # noqa: E501


        :return: The address of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ContractAddress.


        :param address: The address of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def contract_asset_id(self):
        """Gets the contract_asset_id of this ContractAddress.  # noqa: E501


        :return: The contract_asset_id of this ContractAddress.  # noqa: E501
        :rtype: int
        """
        return self._contract_asset_id

    @contract_asset_id.setter
    def contract_asset_id(self, contract_asset_id):
        """Sets the contract_asset_id of this ContractAddress.


        :param contract_asset_id: The contract_asset_id of this ContractAddress.  # noqa: E501
        :type: int
        """

        self._contract_asset_id = contract_asset_id

    @property
    def id(self):
        """Gets the id of this ContractAddress.  # noqa: E501


        :return: The id of this ContractAddress.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContractAddress.


        :param id: The id of this ContractAddress.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this ContractAddress.  # noqa: E501


        :return: The updated_by of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ContractAddress.


        :param updated_by: The updated_by of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this ContractAddress.  # noqa: E501


        :return: The created_by of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ContractAddress.


        :param created_by: The created_by of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def entity_id(self):
        """Gets the entity_id of this ContractAddress.  # noqa: E501


        :return: The entity_id of this ContractAddress.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ContractAddress.


        :param entity_id: The entity_id of this ContractAddress.  # noqa: E501
        :type: int
        """

        self._entity_id = entity_id

    @property
    def asset_address(self):
        """Gets the asset_address of this ContractAddress.  # noqa: E501


        :return: The asset_address of this ContractAddress.  # noqa: E501
        :rtype: str
        """
        return self._asset_address

    @asset_address.setter
    def asset_address(self, asset_address):
        """Sets the asset_address of this ContractAddress.


        :param asset_address: The asset_address of this ContractAddress.  # noqa: E501
        :type: str
        """

        self._asset_address = asset_address

    @property
    def contract(self):
        """Gets the contract of this ContractAddress.  # noqa: E501


        :return: The contract of this ContractAddress.  # noqa: E501
        :rtype: Contract
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this ContractAddress.


        :param contract: The contract of this ContractAddress.  # noqa: E501
        :type: Contract
        """

        self._contract = contract

    @property
    def contract_asset(self):
        """Gets the contract_asset of this ContractAddress.  # noqa: E501


        :return: The contract_asset of this ContractAddress.  # noqa: E501
        :rtype: ContractAsset
        """
        return self._contract_asset

    @contract_asset.setter
    def contract_asset(self, contract_asset):
        """Sets the contract_asset of this ContractAddress.


        :param contract_asset: The contract_asset of this ContractAddress.  # noqa: E501
        :type: ContractAsset
        """

        self._contract_asset = contract_asset

    @property
    def custom_values(self):
        """Gets the custom_values of this ContractAddress.  # noqa: E501


        :return: The custom_values of this ContractAddress.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ContractAddress.


        :param custom_values: The custom_values of this ContractAddress.  # noqa: E501
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
        if issubclass(ContractAddress, dict):
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
        if not isinstance(other, ContractAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
