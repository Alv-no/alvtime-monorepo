# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AvtaleGiroFile(object):
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
        'avtale_giro_agreement_id': 'int',
        'avtale_giro_content': 'str',
        'deleted': 'bool',
        'id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'avtale_giro_merged_file_id': 'int',
        'company_id': 'int',
        'file_id': 'int',
        'company': 'Company',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'avtale_giro_agreement_id': 'AvtaleGiroAgreementID',
        'avtale_giro_content': 'AvtaleGiroContent',
        'deleted': 'Deleted',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'avtale_giro_merged_file_id': 'AvtaleGiroMergedFileID',
        'company_id': 'CompanyID',
        'file_id': 'FileID',
        'company': 'Company',
        'custom_values': 'CustomValues'
    }

    def __init__(self, avtale_giro_agreement_id=None, avtale_giro_content=None, deleted=None, id=None, updated_by=None, created_by=None, avtale_giro_merged_file_id=None, company_id=None, file_id=None, company=None, custom_values=None):  # noqa: E501
        """AvtaleGiroFile - a model defined in Swagger"""  # noqa: E501
        self._avtale_giro_agreement_id = None
        self._avtale_giro_content = None
        self._deleted = None
        self._id = None
        self._updated_by = None
        self._created_by = None
        self._avtale_giro_merged_file_id = None
        self._company_id = None
        self._file_id = None
        self._company = None
        self._custom_values = None
        self.discriminator = None
        if avtale_giro_agreement_id is not None:
            self.avtale_giro_agreement_id = avtale_giro_agreement_id
        if avtale_giro_content is not None:
            self.avtale_giro_content = avtale_giro_content
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if avtale_giro_merged_file_id is not None:
            self.avtale_giro_merged_file_id = avtale_giro_merged_file_id
        if company_id is not None:
            self.company_id = company_id
        if file_id is not None:
            self.file_id = file_id
        if company is not None:
            self.company = company
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def avtale_giro_agreement_id(self):
        """Gets the avtale_giro_agreement_id of this AvtaleGiroFile.  # noqa: E501


        :return: The avtale_giro_agreement_id of this AvtaleGiroFile.  # noqa: E501
        :rtype: int
        """
        return self._avtale_giro_agreement_id

    @avtale_giro_agreement_id.setter
    def avtale_giro_agreement_id(self, avtale_giro_agreement_id):
        """Sets the avtale_giro_agreement_id of this AvtaleGiroFile.


        :param avtale_giro_agreement_id: The avtale_giro_agreement_id of this AvtaleGiroFile.  # noqa: E501
        :type: int
        """

        self._avtale_giro_agreement_id = avtale_giro_agreement_id

    @property
    def avtale_giro_content(self):
        """Gets the avtale_giro_content of this AvtaleGiroFile.  # noqa: E501


        :return: The avtale_giro_content of this AvtaleGiroFile.  # noqa: E501
        :rtype: str
        """
        return self._avtale_giro_content

    @avtale_giro_content.setter
    def avtale_giro_content(self, avtale_giro_content):
        """Sets the avtale_giro_content of this AvtaleGiroFile.


        :param avtale_giro_content: The avtale_giro_content of this AvtaleGiroFile.  # noqa: E501
        :type: str
        """

        self._avtale_giro_content = avtale_giro_content

    @property
    def deleted(self):
        """Gets the deleted of this AvtaleGiroFile.  # noqa: E501


        :return: The deleted of this AvtaleGiroFile.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AvtaleGiroFile.


        :param deleted: The deleted of this AvtaleGiroFile.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this AvtaleGiroFile.  # noqa: E501


        :return: The id of this AvtaleGiroFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvtaleGiroFile.


        :param id: The id of this AvtaleGiroFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this AvtaleGiroFile.  # noqa: E501


        :return: The updated_by of this AvtaleGiroFile.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AvtaleGiroFile.


        :param updated_by: The updated_by of this AvtaleGiroFile.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this AvtaleGiroFile.  # noqa: E501


        :return: The created_by of this AvtaleGiroFile.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AvtaleGiroFile.


        :param created_by: The created_by of this AvtaleGiroFile.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def avtale_giro_merged_file_id(self):
        """Gets the avtale_giro_merged_file_id of this AvtaleGiroFile.  # noqa: E501


        :return: The avtale_giro_merged_file_id of this AvtaleGiroFile.  # noqa: E501
        :rtype: int
        """
        return self._avtale_giro_merged_file_id

    @avtale_giro_merged_file_id.setter
    def avtale_giro_merged_file_id(self, avtale_giro_merged_file_id):
        """Sets the avtale_giro_merged_file_id of this AvtaleGiroFile.


        :param avtale_giro_merged_file_id: The avtale_giro_merged_file_id of this AvtaleGiroFile.  # noqa: E501
        :type: int
        """

        self._avtale_giro_merged_file_id = avtale_giro_merged_file_id

    @property
    def company_id(self):
        """Gets the company_id of this AvtaleGiroFile.  # noqa: E501


        :return: The company_id of this AvtaleGiroFile.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this AvtaleGiroFile.


        :param company_id: The company_id of this AvtaleGiroFile.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def file_id(self):
        """Gets the file_id of this AvtaleGiroFile.  # noqa: E501


        :return: The file_id of this AvtaleGiroFile.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this AvtaleGiroFile.


        :param file_id: The file_id of this AvtaleGiroFile.  # noqa: E501
        :type: int
        """

        self._file_id = file_id

    @property
    def company(self):
        """Gets the company of this AvtaleGiroFile.  # noqa: E501


        :return: The company of this AvtaleGiroFile.  # noqa: E501
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AvtaleGiroFile.


        :param company: The company of this AvtaleGiroFile.  # noqa: E501
        :type: Company
        """

        self._company = company

    @property
    def custom_values(self):
        """Gets the custom_values of this AvtaleGiroFile.  # noqa: E501


        :return: The custom_values of this AvtaleGiroFile.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this AvtaleGiroFile.


        :param custom_values: The custom_values of this AvtaleGiroFile.  # noqa: E501
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
        if issubclass(AvtaleGiroFile, dict):
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
        if not isinstance(other, AvtaleGiroFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
