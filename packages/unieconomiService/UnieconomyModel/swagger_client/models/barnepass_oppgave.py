# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BarnepassOppgave(object):
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
        'email': 'str',
        'status_code': 'int',
        'deleted': 'bool',
        'foedselsnummer': 'str',
        'barnepass_id': 'int',
        'id': 'int',
        'updated_by': 'str',
        'navn': 'str',
        'created_by': 'str',
        'paaloept_beloep': 'int',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'email': 'email',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'foedselsnummer': 'foedselsnummer',
        'barnepass_id': 'BarnepassID',
        'id': 'ID',
        'updated_by': 'UpdatedBy',
        'navn': 'navn',
        'created_by': 'CreatedBy',
        'paaloept_beloep': 'paaloeptBeloep',
        'custom_values': 'CustomValues'
    }

    def __init__(self, email=None, status_code=None, deleted=None, foedselsnummer=None, barnepass_id=None, id=None, updated_by=None, navn=None, created_by=None, paaloept_beloep=None, custom_values=None):  # noqa: E501
        """BarnepassOppgave - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._status_code = None
        self._deleted = None
        self._foedselsnummer = None
        self._barnepass_id = None
        self._id = None
        self._updated_by = None
        self._navn = None
        self._created_by = None
        self._paaloept_beloep = None
        self._custom_values = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if foedselsnummer is not None:
            self.foedselsnummer = foedselsnummer
        if barnepass_id is not None:
            self.barnepass_id = barnepass_id
        if id is not None:
            self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        if navn is not None:
            self.navn = navn
        if created_by is not None:
            self.created_by = created_by
        if paaloept_beloep is not None:
            self.paaloept_beloep = paaloept_beloep
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def email(self):
        """Gets the email of this BarnepassOppgave.  # noqa: E501


        :return: The email of this BarnepassOppgave.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BarnepassOppgave.


        :param email: The email of this BarnepassOppgave.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def status_code(self):
        """Gets the status_code of this BarnepassOppgave.  # noqa: E501


        :return: The status_code of this BarnepassOppgave.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this BarnepassOppgave.


        :param status_code: The status_code of this BarnepassOppgave.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this BarnepassOppgave.  # noqa: E501


        :return: The deleted of this BarnepassOppgave.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this BarnepassOppgave.


        :param deleted: The deleted of this BarnepassOppgave.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def foedselsnummer(self):
        """Gets the foedselsnummer of this BarnepassOppgave.  # noqa: E501


        :return: The foedselsnummer of this BarnepassOppgave.  # noqa: E501
        :rtype: str
        """
        return self._foedselsnummer

    @foedselsnummer.setter
    def foedselsnummer(self, foedselsnummer):
        """Sets the foedselsnummer of this BarnepassOppgave.


        :param foedselsnummer: The foedselsnummer of this BarnepassOppgave.  # noqa: E501
        :type: str
        """

        self._foedselsnummer = foedselsnummer

    @property
    def barnepass_id(self):
        """Gets the barnepass_id of this BarnepassOppgave.  # noqa: E501


        :return: The barnepass_id of this BarnepassOppgave.  # noqa: E501
        :rtype: int
        """
        return self._barnepass_id

    @barnepass_id.setter
    def barnepass_id(self, barnepass_id):
        """Sets the barnepass_id of this BarnepassOppgave.


        :param barnepass_id: The barnepass_id of this BarnepassOppgave.  # noqa: E501
        :type: int
        """

        self._barnepass_id = barnepass_id

    @property
    def id(self):
        """Gets the id of this BarnepassOppgave.  # noqa: E501


        :return: The id of this BarnepassOppgave.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BarnepassOppgave.


        :param id: The id of this BarnepassOppgave.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this BarnepassOppgave.  # noqa: E501


        :return: The updated_by of this BarnepassOppgave.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this BarnepassOppgave.


        :param updated_by: The updated_by of this BarnepassOppgave.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def navn(self):
        """Gets the navn of this BarnepassOppgave.  # noqa: E501


        :return: The navn of this BarnepassOppgave.  # noqa: E501
        :rtype: str
        """
        return self._navn

    @navn.setter
    def navn(self, navn):
        """Sets the navn of this BarnepassOppgave.


        :param navn: The navn of this BarnepassOppgave.  # noqa: E501
        :type: str
        """

        self._navn = navn

    @property
    def created_by(self):
        """Gets the created_by of this BarnepassOppgave.  # noqa: E501


        :return: The created_by of this BarnepassOppgave.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BarnepassOppgave.


        :param created_by: The created_by of this BarnepassOppgave.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def paaloept_beloep(self):
        """Gets the paaloept_beloep of this BarnepassOppgave.  # noqa: E501


        :return: The paaloept_beloep of this BarnepassOppgave.  # noqa: E501
        :rtype: int
        """
        return self._paaloept_beloep

    @paaloept_beloep.setter
    def paaloept_beloep(self, paaloept_beloep):
        """Sets the paaloept_beloep of this BarnepassOppgave.


        :param paaloept_beloep: The paaloept_beloep of this BarnepassOppgave.  # noqa: E501
        :type: int
        """

        self._paaloept_beloep = paaloept_beloep

    @property
    def custom_values(self):
        """Gets the custom_values of this BarnepassOppgave.  # noqa: E501


        :return: The custom_values of this BarnepassOppgave.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this BarnepassOppgave.


        :param custom_values: The custom_values of this BarnepassOppgave.  # noqa: E501
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
        if issubclass(BarnepassOppgave, dict):
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
        if not isinstance(other, BarnepassOppgave):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
