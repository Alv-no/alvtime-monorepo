# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CompanyAccountingSettings(object):
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
        'asset_sale_profit_no_vat_account_id': 'int',
        're_invoicing_costsharing_product_id': 'int',
        'asset_sale_profit_vat_account_id': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'asset_sale_product_id': 'int',
        're_invoicing_method': 'int',
        'asset_sale_profit_balancing_account_id': 'int',
        'id': 'int',
        're_invoicing_turnover_product_id': 'int',
        'updated_by': 'str',
        'asset_writeoff_account_id': 'int',
        'asset_sale_loss_balancing_account_id': 'int',
        'created_by': 'str',
        'asset_sale_loss_vat_account_id': 'int',
        'asset_sale_loss_no_vat_account_id': 'int',
        're_invoicing_costsharing_product': 'Product',
        're_invoicing_turnover_product': 'Product',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'asset_sale_profit_no_vat_account_id': 'AssetSaleProfitNoVatAccountID',
        're_invoicing_costsharing_product_id': 'ReInvoicingCostsharingProductID',
        'asset_sale_profit_vat_account_id': 'AssetSaleProfitVatAccountID',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'asset_sale_product_id': 'AssetSaleProductID',
        're_invoicing_method': 'ReInvoicingMethod',
        'asset_sale_profit_balancing_account_id': 'AssetSaleProfitBalancingAccountID',
        'id': 'ID',
        're_invoicing_turnover_product_id': 'ReInvoicingTurnoverProductID',
        'updated_by': 'UpdatedBy',
        'asset_writeoff_account_id': 'AssetWriteoffAccountID',
        'asset_sale_loss_balancing_account_id': 'AssetSaleLossBalancingAccountID',
        'created_by': 'CreatedBy',
        'asset_sale_loss_vat_account_id': 'AssetSaleLossVatAccountID',
        'asset_sale_loss_no_vat_account_id': 'AssetSaleLossNoVatAccountID',
        're_invoicing_costsharing_product': 'ReInvoicingCostsharingProduct',
        're_invoicing_turnover_product': 'ReInvoicingTurnoverProduct',
        'custom_values': 'CustomValues'
    }

    def __init__(self, asset_sale_profit_no_vat_account_id=None, re_invoicing_costsharing_product_id=None, asset_sale_profit_vat_account_id=None, status_code=None, deleted=None, asset_sale_product_id=None, re_invoicing_method=None, asset_sale_profit_balancing_account_id=None, id=None, re_invoicing_turnover_product_id=None, updated_by=None, asset_writeoff_account_id=None, asset_sale_loss_balancing_account_id=None, created_by=None, asset_sale_loss_vat_account_id=None, asset_sale_loss_no_vat_account_id=None, re_invoicing_costsharing_product=None, re_invoicing_turnover_product=None, custom_values=None):  # noqa: E501
        """CompanyAccountingSettings - a model defined in Swagger"""  # noqa: E501
        self._asset_sale_profit_no_vat_account_id = None
        self._re_invoicing_costsharing_product_id = None
        self._asset_sale_profit_vat_account_id = None
        self._status_code = None
        self._deleted = None
        self._asset_sale_product_id = None
        self._re_invoicing_method = None
        self._asset_sale_profit_balancing_account_id = None
        self._id = None
        self._re_invoicing_turnover_product_id = None
        self._updated_by = None
        self._asset_writeoff_account_id = None
        self._asset_sale_loss_balancing_account_id = None
        self._created_by = None
        self._asset_sale_loss_vat_account_id = None
        self._asset_sale_loss_no_vat_account_id = None
        self._re_invoicing_costsharing_product = None
        self._re_invoicing_turnover_product = None
        self._custom_values = None
        self.discriminator = None
        if asset_sale_profit_no_vat_account_id is not None:
            self.asset_sale_profit_no_vat_account_id = asset_sale_profit_no_vat_account_id
        if re_invoicing_costsharing_product_id is not None:
            self.re_invoicing_costsharing_product_id = re_invoicing_costsharing_product_id
        if asset_sale_profit_vat_account_id is not None:
            self.asset_sale_profit_vat_account_id = asset_sale_profit_vat_account_id
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if asset_sale_product_id is not None:
            self.asset_sale_product_id = asset_sale_product_id
        if re_invoicing_method is not None:
            self.re_invoicing_method = re_invoicing_method
        if asset_sale_profit_balancing_account_id is not None:
            self.asset_sale_profit_balancing_account_id = asset_sale_profit_balancing_account_id
        if id is not None:
            self.id = id
        if re_invoicing_turnover_product_id is not None:
            self.re_invoicing_turnover_product_id = re_invoicing_turnover_product_id
        if updated_by is not None:
            self.updated_by = updated_by
        if asset_writeoff_account_id is not None:
            self.asset_writeoff_account_id = asset_writeoff_account_id
        if asset_sale_loss_balancing_account_id is not None:
            self.asset_sale_loss_balancing_account_id = asset_sale_loss_balancing_account_id
        if created_by is not None:
            self.created_by = created_by
        if asset_sale_loss_vat_account_id is not None:
            self.asset_sale_loss_vat_account_id = asset_sale_loss_vat_account_id
        if asset_sale_loss_no_vat_account_id is not None:
            self.asset_sale_loss_no_vat_account_id = asset_sale_loss_no_vat_account_id
        if re_invoicing_costsharing_product is not None:
            self.re_invoicing_costsharing_product = re_invoicing_costsharing_product
        if re_invoicing_turnover_product is not None:
            self.re_invoicing_turnover_product = re_invoicing_turnover_product
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def asset_sale_profit_no_vat_account_id(self):
        """Gets the asset_sale_profit_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_profit_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_profit_no_vat_account_id

    @asset_sale_profit_no_vat_account_id.setter
    def asset_sale_profit_no_vat_account_id(self, asset_sale_profit_no_vat_account_id):
        """Sets the asset_sale_profit_no_vat_account_id of this CompanyAccountingSettings.


        :param asset_sale_profit_no_vat_account_id: The asset_sale_profit_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_profit_no_vat_account_id = asset_sale_profit_no_vat_account_id

    @property
    def re_invoicing_costsharing_product_id(self):
        """Gets the re_invoicing_costsharing_product_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The re_invoicing_costsharing_product_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._re_invoicing_costsharing_product_id

    @re_invoicing_costsharing_product_id.setter
    def re_invoicing_costsharing_product_id(self, re_invoicing_costsharing_product_id):
        """Sets the re_invoicing_costsharing_product_id of this CompanyAccountingSettings.


        :param re_invoicing_costsharing_product_id: The re_invoicing_costsharing_product_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._re_invoicing_costsharing_product_id = re_invoicing_costsharing_product_id

    @property
    def asset_sale_profit_vat_account_id(self):
        """Gets the asset_sale_profit_vat_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_profit_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_profit_vat_account_id

    @asset_sale_profit_vat_account_id.setter
    def asset_sale_profit_vat_account_id(self, asset_sale_profit_vat_account_id):
        """Sets the asset_sale_profit_vat_account_id of this CompanyAccountingSettings.


        :param asset_sale_profit_vat_account_id: The asset_sale_profit_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_profit_vat_account_id = asset_sale_profit_vat_account_id

    @property
    def status_code(self):
        """Gets the status_code of this CompanyAccountingSettings.  # noqa: E501


        :return: The status_code of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CompanyAccountingSettings.


        :param status_code: The status_code of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this CompanyAccountingSettings.  # noqa: E501


        :return: The deleted of this CompanyAccountingSettings.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CompanyAccountingSettings.


        :param deleted: The deleted of this CompanyAccountingSettings.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def asset_sale_product_id(self):
        """Gets the asset_sale_product_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_product_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_product_id

    @asset_sale_product_id.setter
    def asset_sale_product_id(self, asset_sale_product_id):
        """Sets the asset_sale_product_id of this CompanyAccountingSettings.


        :param asset_sale_product_id: The asset_sale_product_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_product_id = asset_sale_product_id

    @property
    def re_invoicing_method(self):
        """Gets the re_invoicing_method of this CompanyAccountingSettings.  # noqa: E501


        :return: The re_invoicing_method of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._re_invoicing_method

    @re_invoicing_method.setter
    def re_invoicing_method(self, re_invoicing_method):
        """Sets the re_invoicing_method of this CompanyAccountingSettings.


        :param re_invoicing_method: The re_invoicing_method of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._re_invoicing_method = re_invoicing_method

    @property
    def asset_sale_profit_balancing_account_id(self):
        """Gets the asset_sale_profit_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_profit_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_profit_balancing_account_id

    @asset_sale_profit_balancing_account_id.setter
    def asset_sale_profit_balancing_account_id(self, asset_sale_profit_balancing_account_id):
        """Sets the asset_sale_profit_balancing_account_id of this CompanyAccountingSettings.


        :param asset_sale_profit_balancing_account_id: The asset_sale_profit_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_profit_balancing_account_id = asset_sale_profit_balancing_account_id

    @property
    def id(self):
        """Gets the id of this CompanyAccountingSettings.  # noqa: E501


        :return: The id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyAccountingSettings.


        :param id: The id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def re_invoicing_turnover_product_id(self):
        """Gets the re_invoicing_turnover_product_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The re_invoicing_turnover_product_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._re_invoicing_turnover_product_id

    @re_invoicing_turnover_product_id.setter
    def re_invoicing_turnover_product_id(self, re_invoicing_turnover_product_id):
        """Sets the re_invoicing_turnover_product_id of this CompanyAccountingSettings.


        :param re_invoicing_turnover_product_id: The re_invoicing_turnover_product_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._re_invoicing_turnover_product_id = re_invoicing_turnover_product_id

    @property
    def updated_by(self):
        """Gets the updated_by of this CompanyAccountingSettings.  # noqa: E501


        :return: The updated_by of this CompanyAccountingSettings.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this CompanyAccountingSettings.


        :param updated_by: The updated_by of this CompanyAccountingSettings.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def asset_writeoff_account_id(self):
        """Gets the asset_writeoff_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_writeoff_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_writeoff_account_id

    @asset_writeoff_account_id.setter
    def asset_writeoff_account_id(self, asset_writeoff_account_id):
        """Sets the asset_writeoff_account_id of this CompanyAccountingSettings.


        :param asset_writeoff_account_id: The asset_writeoff_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_writeoff_account_id = asset_writeoff_account_id

    @property
    def asset_sale_loss_balancing_account_id(self):
        """Gets the asset_sale_loss_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_loss_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_loss_balancing_account_id

    @asset_sale_loss_balancing_account_id.setter
    def asset_sale_loss_balancing_account_id(self, asset_sale_loss_balancing_account_id):
        """Sets the asset_sale_loss_balancing_account_id of this CompanyAccountingSettings.


        :param asset_sale_loss_balancing_account_id: The asset_sale_loss_balancing_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_loss_balancing_account_id = asset_sale_loss_balancing_account_id

    @property
    def created_by(self):
        """Gets the created_by of this CompanyAccountingSettings.  # noqa: E501


        :return: The created_by of this CompanyAccountingSettings.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CompanyAccountingSettings.


        :param created_by: The created_by of this CompanyAccountingSettings.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def asset_sale_loss_vat_account_id(self):
        """Gets the asset_sale_loss_vat_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_loss_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_loss_vat_account_id

    @asset_sale_loss_vat_account_id.setter
    def asset_sale_loss_vat_account_id(self, asset_sale_loss_vat_account_id):
        """Sets the asset_sale_loss_vat_account_id of this CompanyAccountingSettings.


        :param asset_sale_loss_vat_account_id: The asset_sale_loss_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_loss_vat_account_id = asset_sale_loss_vat_account_id

    @property
    def asset_sale_loss_no_vat_account_id(self):
        """Gets the asset_sale_loss_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501


        :return: The asset_sale_loss_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sale_loss_no_vat_account_id

    @asset_sale_loss_no_vat_account_id.setter
    def asset_sale_loss_no_vat_account_id(self, asset_sale_loss_no_vat_account_id):
        """Sets the asset_sale_loss_no_vat_account_id of this CompanyAccountingSettings.


        :param asset_sale_loss_no_vat_account_id: The asset_sale_loss_no_vat_account_id of this CompanyAccountingSettings.  # noqa: E501
        :type: int
        """

        self._asset_sale_loss_no_vat_account_id = asset_sale_loss_no_vat_account_id

    @property
    def re_invoicing_costsharing_product(self):
        """Gets the re_invoicing_costsharing_product of this CompanyAccountingSettings.  # noqa: E501


        :return: The re_invoicing_costsharing_product of this CompanyAccountingSettings.  # noqa: E501
        :rtype: Product
        """
        return self._re_invoicing_costsharing_product

    @re_invoicing_costsharing_product.setter
    def re_invoicing_costsharing_product(self, re_invoicing_costsharing_product):
        """Sets the re_invoicing_costsharing_product of this CompanyAccountingSettings.


        :param re_invoicing_costsharing_product: The re_invoicing_costsharing_product of this CompanyAccountingSettings.  # noqa: E501
        :type: Product
        """

        self._re_invoicing_costsharing_product = re_invoicing_costsharing_product

    @property
    def re_invoicing_turnover_product(self):
        """Gets the re_invoicing_turnover_product of this CompanyAccountingSettings.  # noqa: E501


        :return: The re_invoicing_turnover_product of this CompanyAccountingSettings.  # noqa: E501
        :rtype: Product
        """
        return self._re_invoicing_turnover_product

    @re_invoicing_turnover_product.setter
    def re_invoicing_turnover_product(self, re_invoicing_turnover_product):
        """Sets the re_invoicing_turnover_product of this CompanyAccountingSettings.


        :param re_invoicing_turnover_product: The re_invoicing_turnover_product of this CompanyAccountingSettings.  # noqa: E501
        :type: Product
        """

        self._re_invoicing_turnover_product = re_invoicing_turnover_product

    @property
    def custom_values(self):
        """Gets the custom_values of this CompanyAccountingSettings.  # noqa: E501


        :return: The custom_values of this CompanyAccountingSettings.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this CompanyAccountingSettings.


        :param custom_values: The custom_values of this CompanyAccountingSettings.  # noqa: E501
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
        if issubclass(CompanyAccountingSettings, dict):
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
        if not isinstance(other, CompanyAccountingSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
