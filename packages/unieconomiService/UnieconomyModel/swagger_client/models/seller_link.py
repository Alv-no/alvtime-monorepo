# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellerLink(object):
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
        'customer_id': 'int',
        'customer_invoice_id': 'int',
        'customer_order_id': 'int',
        'customer_quote_id': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'percent': 'int',
        'seller_id': 'int',
        'id': 'int',
        'recurring_invoice_id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'customer_id': 'CustomerID',
        'customer_invoice_id': 'CustomerInvoiceID',
        'customer_order_id': 'CustomerOrderID',
        'customer_quote_id': 'CustomerQuoteID',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'percent': 'Percent',
        'seller_id': 'SellerID',
        'id': 'ID',
        'recurring_invoice_id': 'RecurringInvoiceID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'custom_values': 'CustomValues'
    }

    def __init__(self, customer_id=None, customer_invoice_id=None, customer_order_id=None, customer_quote_id=None, status_code=None, deleted=None, percent=None, seller_id=None, id=None, recurring_invoice_id=None, updated_by=None, created_by=None, custom_values=None):  # noqa: E501
        """SellerLink - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._customer_invoice_id = None
        self._customer_order_id = None
        self._customer_quote_id = None
        self._status_code = None
        self._deleted = None
        self._percent = None
        self._seller_id = None
        self._id = None
        self._recurring_invoice_id = None
        self._updated_by = None
        self._created_by = None
        self._custom_values = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_invoice_id is not None:
            self.customer_invoice_id = customer_invoice_id
        if customer_order_id is not None:
            self.customer_order_id = customer_order_id
        if customer_quote_id is not None:
            self.customer_quote_id = customer_quote_id
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if percent is not None:
            self.percent = percent
        if seller_id is not None:
            self.seller_id = seller_id
        if id is not None:
            self.id = id
        if recurring_invoice_id is not None:
            self.recurring_invoice_id = recurring_invoice_id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def customer_id(self):
        """Gets the customer_id of this SellerLink.  # noqa: E501


        :return: The customer_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SellerLink.


        :param customer_id: The customer_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_invoice_id(self):
        """Gets the customer_invoice_id of this SellerLink.  # noqa: E501


        :return: The customer_invoice_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._customer_invoice_id

    @customer_invoice_id.setter
    def customer_invoice_id(self, customer_invoice_id):
        """Sets the customer_invoice_id of this SellerLink.


        :param customer_invoice_id: The customer_invoice_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._customer_invoice_id = customer_invoice_id

    @property
    def customer_order_id(self):
        """Gets the customer_order_id of this SellerLink.  # noqa: E501


        :return: The customer_order_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._customer_order_id

    @customer_order_id.setter
    def customer_order_id(self, customer_order_id):
        """Sets the customer_order_id of this SellerLink.


        :param customer_order_id: The customer_order_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._customer_order_id = customer_order_id

    @property
    def customer_quote_id(self):
        """Gets the customer_quote_id of this SellerLink.  # noqa: E501


        :return: The customer_quote_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._customer_quote_id

    @customer_quote_id.setter
    def customer_quote_id(self, customer_quote_id):
        """Sets the customer_quote_id of this SellerLink.


        :param customer_quote_id: The customer_quote_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._customer_quote_id = customer_quote_id

    @property
    def status_code(self):
        """Gets the status_code of this SellerLink.  # noqa: E501


        :return: The status_code of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this SellerLink.


        :param status_code: The status_code of this SellerLink.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this SellerLink.  # noqa: E501


        :return: The deleted of this SellerLink.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SellerLink.


        :param deleted: The deleted of this SellerLink.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def percent(self):
        """Gets the percent of this SellerLink.  # noqa: E501


        :return: The percent of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this SellerLink.


        :param percent: The percent of this SellerLink.  # noqa: E501
        :type: int
        """

        self._percent = percent

    @property
    def seller_id(self):
        """Gets the seller_id of this SellerLink.  # noqa: E501


        :return: The seller_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this SellerLink.


        :param seller_id: The seller_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._seller_id = seller_id

    @property
    def id(self):
        """Gets the id of this SellerLink.  # noqa: E501


        :return: The id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SellerLink.


        :param id: The id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def recurring_invoice_id(self):
        """Gets the recurring_invoice_id of this SellerLink.  # noqa: E501


        :return: The recurring_invoice_id of this SellerLink.  # noqa: E501
        :rtype: int
        """
        return self._recurring_invoice_id

    @recurring_invoice_id.setter
    def recurring_invoice_id(self, recurring_invoice_id):
        """Sets the recurring_invoice_id of this SellerLink.


        :param recurring_invoice_id: The recurring_invoice_id of this SellerLink.  # noqa: E501
        :type: int
        """

        self._recurring_invoice_id = recurring_invoice_id

    @property
    def updated_by(self):
        """Gets the updated_by of this SellerLink.  # noqa: E501


        :return: The updated_by of this SellerLink.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this SellerLink.


        :param updated_by: The updated_by of this SellerLink.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this SellerLink.  # noqa: E501


        :return: The created_by of this SellerLink.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SellerLink.


        :param created_by: The created_by of this SellerLink.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def custom_values(self):
        """Gets the custom_values of this SellerLink.  # noqa: E501


        :return: The custom_values of this SellerLink.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this SellerLink.


        :param custom_values: The custom_values of this SellerLink.  # noqa: E501
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
        if issubclass(SellerLink, dict):
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
        if not isinstance(other, SellerLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
