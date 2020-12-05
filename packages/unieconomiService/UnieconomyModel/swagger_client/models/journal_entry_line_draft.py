# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class JournalEntryLineDraft(object):
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
        'post_post_journal_entry_line_id': 'int',
        'description': 'str',
        'customer_invoice_id': 'int',
        'customer_order_id': 'int',
        'signature': 'str',
        'journal_entry_number': 'str',
        'account_id': 'int',
        'invoice_number': 'str',
        'dimensions_id': 'int',
        'accrual_id': 'int',
        'sub_account_id': 'int',
        'journal_entry_id': 'int',
        'status_code': 'int',
        'deleted': 'bool',
        'vat_period_id': 'int',
        'period_id': 'int',
        'payment_id': 'str',
        'id': 'int',
        'vat_type_id': 'int',
        'payment_info_type_id': 'int',
        'payment_reference_id': 'int',
        'currency_code_id': 'int',
        'updated_by': 'str',
        'created_by': 'str',
        'vat_deduction_percent': 'int',
        'journal_entry_number_numeric': 'int',
        'journal_entry_type_id': 'int',
        'supplier_invoice_id': 'int',
        'batch_number': 'int',
        'dimensions': 'Dimensions',
        'accrual': 'Accrual',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'post_post_journal_entry_line_id': 'PostPostJournalEntryLineID',
        'description': 'Description',
        'customer_invoice_id': 'CustomerInvoiceID',
        'customer_order_id': 'CustomerOrderID',
        'signature': 'Signature',
        'journal_entry_number': 'JournalEntryNumber',
        'account_id': 'AccountID',
        'invoice_number': 'InvoiceNumber',
        'dimensions_id': 'DimensionsID',
        'accrual_id': 'AccrualID',
        'sub_account_id': 'SubAccountID',
        'journal_entry_id': 'JournalEntryID',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'vat_period_id': 'VatPeriodID',
        'period_id': 'PeriodID',
        'payment_id': 'PaymentID',
        'id': 'ID',
        'vat_type_id': 'VatTypeID',
        'payment_info_type_id': 'PaymentInfoTypeID',
        'payment_reference_id': 'PaymentReferenceID',
        'currency_code_id': 'CurrencyCodeID',
        'updated_by': 'UpdatedBy',
        'created_by': 'CreatedBy',
        'vat_deduction_percent': 'VatDeductionPercent',
        'journal_entry_number_numeric': 'JournalEntryNumberNumeric',
        'journal_entry_type_id': 'JournalEntryTypeID',
        'supplier_invoice_id': 'SupplierInvoiceID',
        'batch_number': 'BatchNumber',
        'dimensions': 'Dimensions',
        'accrual': 'Accrual',
        'custom_values': 'CustomValues'
    }

    def __init__(self, post_post_journal_entry_line_id=None, description=None, customer_invoice_id=None, customer_order_id=None, signature=None, journal_entry_number=None, account_id=None, invoice_number=None, dimensions_id=None, accrual_id=None, sub_account_id=None, journal_entry_id=None, status_code=None, deleted=None, vat_period_id=None, period_id=None, payment_id=None, id=None, vat_type_id=None, payment_info_type_id=None, payment_reference_id=None, currency_code_id=None, updated_by=None, created_by=None, vat_deduction_percent=None, journal_entry_number_numeric=None, journal_entry_type_id=None, supplier_invoice_id=None, batch_number=None, dimensions=None, accrual=None, custom_values=None):  # noqa: E501
        """JournalEntryLineDraft - a model defined in Swagger"""  # noqa: E501
        self._post_post_journal_entry_line_id = None
        self._description = None
        self._customer_invoice_id = None
        self._customer_order_id = None
        self._signature = None
        self._journal_entry_number = None
        self._account_id = None
        self._invoice_number = None
        self._dimensions_id = None
        self._accrual_id = None
        self._sub_account_id = None
        self._journal_entry_id = None
        self._status_code = None
        self._deleted = None
        self._vat_period_id = None
        self._period_id = None
        self._payment_id = None
        self._id = None
        self._vat_type_id = None
        self._payment_info_type_id = None
        self._payment_reference_id = None
        self._currency_code_id = None
        self._updated_by = None
        self._created_by = None
        self._vat_deduction_percent = None
        self._journal_entry_number_numeric = None
        self._journal_entry_type_id = None
        self._supplier_invoice_id = None
        self._batch_number = None
        self._dimensions = None
        self._accrual = None
        self._custom_values = None
        self.discriminator = None
        if post_post_journal_entry_line_id is not None:
            self.post_post_journal_entry_line_id = post_post_journal_entry_line_id
        if description is not None:
            self.description = description
        if customer_invoice_id is not None:
            self.customer_invoice_id = customer_invoice_id
        if customer_order_id is not None:
            self.customer_order_id = customer_order_id
        if signature is not None:
            self.signature = signature
        if journal_entry_number is not None:
            self.journal_entry_number = journal_entry_number
        if account_id is not None:
            self.account_id = account_id
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if dimensions_id is not None:
            self.dimensions_id = dimensions_id
        if accrual_id is not None:
            self.accrual_id = accrual_id
        if sub_account_id is not None:
            self.sub_account_id = sub_account_id
        if journal_entry_id is not None:
            self.journal_entry_id = journal_entry_id
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if vat_period_id is not None:
            self.vat_period_id = vat_period_id
        if period_id is not None:
            self.period_id = period_id
        if payment_id is not None:
            self.payment_id = payment_id
        if id is not None:
            self.id = id
        if vat_type_id is not None:
            self.vat_type_id = vat_type_id
        if payment_info_type_id is not None:
            self.payment_info_type_id = payment_info_type_id
        if payment_reference_id is not None:
            self.payment_reference_id = payment_reference_id
        if currency_code_id is not None:
            self.currency_code_id = currency_code_id
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if vat_deduction_percent is not None:
            self.vat_deduction_percent = vat_deduction_percent
        if journal_entry_number_numeric is not None:
            self.journal_entry_number_numeric = journal_entry_number_numeric
        if journal_entry_type_id is not None:
            self.journal_entry_type_id = journal_entry_type_id
        if supplier_invoice_id is not None:
            self.supplier_invoice_id = supplier_invoice_id
        if batch_number is not None:
            self.batch_number = batch_number
        if dimensions is not None:
            self.dimensions = dimensions
        if accrual is not None:
            self.accrual = accrual
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def post_post_journal_entry_line_id(self):
        """Gets the post_post_journal_entry_line_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The post_post_journal_entry_line_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._post_post_journal_entry_line_id

    @post_post_journal_entry_line_id.setter
    def post_post_journal_entry_line_id(self, post_post_journal_entry_line_id):
        """Sets the post_post_journal_entry_line_id of this JournalEntryLineDraft.


        :param post_post_journal_entry_line_id: The post_post_journal_entry_line_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._post_post_journal_entry_line_id = post_post_journal_entry_line_id

    @property
    def description(self):
        """Gets the description of this JournalEntryLineDraft.  # noqa: E501


        :return: The description of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JournalEntryLineDraft.


        :param description: The description of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer_invoice_id(self):
        """Gets the customer_invoice_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The customer_invoice_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._customer_invoice_id

    @customer_invoice_id.setter
    def customer_invoice_id(self, customer_invoice_id):
        """Sets the customer_invoice_id of this JournalEntryLineDraft.


        :param customer_invoice_id: The customer_invoice_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._customer_invoice_id = customer_invoice_id

    @property
    def customer_order_id(self):
        """Gets the customer_order_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The customer_order_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._customer_order_id

    @customer_order_id.setter
    def customer_order_id(self, customer_order_id):
        """Sets the customer_order_id of this JournalEntryLineDraft.


        :param customer_order_id: The customer_order_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._customer_order_id = customer_order_id

    @property
    def signature(self):
        """Gets the signature of this JournalEntryLineDraft.  # noqa: E501


        :return: The signature of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this JournalEntryLineDraft.


        :param signature: The signature of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def journal_entry_number(self):
        """Gets the journal_entry_number of this JournalEntryLineDraft.  # noqa: E501


        :return: The journal_entry_number of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._journal_entry_number

    @journal_entry_number.setter
    def journal_entry_number(self, journal_entry_number):
        """Sets the journal_entry_number of this JournalEntryLineDraft.


        :param journal_entry_number: The journal_entry_number of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._journal_entry_number = journal_entry_number

    @property
    def account_id(self):
        """Gets the account_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The account_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this JournalEntryLineDraft.


        :param account_id: The account_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def invoice_number(self):
        """Gets the invoice_number of this JournalEntryLineDraft.  # noqa: E501


        :return: The invoice_number of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this JournalEntryLineDraft.


        :param invoice_number: The invoice_number of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def dimensions_id(self):
        """Gets the dimensions_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The dimensions_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._dimensions_id

    @dimensions_id.setter
    def dimensions_id(self, dimensions_id):
        """Sets the dimensions_id of this JournalEntryLineDraft.


        :param dimensions_id: The dimensions_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._dimensions_id = dimensions_id

    @property
    def accrual_id(self):
        """Gets the accrual_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The accrual_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._accrual_id

    @accrual_id.setter
    def accrual_id(self, accrual_id):
        """Sets the accrual_id of this JournalEntryLineDraft.


        :param accrual_id: The accrual_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._accrual_id = accrual_id

    @property
    def sub_account_id(self):
        """Gets the sub_account_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The sub_account_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._sub_account_id

    @sub_account_id.setter
    def sub_account_id(self, sub_account_id):
        """Sets the sub_account_id of this JournalEntryLineDraft.


        :param sub_account_id: The sub_account_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._sub_account_id = sub_account_id

    @property
    def journal_entry_id(self):
        """Gets the journal_entry_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The journal_entry_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._journal_entry_id

    @journal_entry_id.setter
    def journal_entry_id(self, journal_entry_id):
        """Sets the journal_entry_id of this JournalEntryLineDraft.


        :param journal_entry_id: The journal_entry_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._journal_entry_id = journal_entry_id

    @property
    def status_code(self):
        """Gets the status_code of this JournalEntryLineDraft.  # noqa: E501


        :return: The status_code of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this JournalEntryLineDraft.


        :param status_code: The status_code of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this JournalEntryLineDraft.  # noqa: E501


        :return: The deleted of this JournalEntryLineDraft.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this JournalEntryLineDraft.


        :param deleted: The deleted of this JournalEntryLineDraft.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def vat_period_id(self):
        """Gets the vat_period_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The vat_period_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._vat_period_id

    @vat_period_id.setter
    def vat_period_id(self, vat_period_id):
        """Sets the vat_period_id of this JournalEntryLineDraft.


        :param vat_period_id: The vat_period_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._vat_period_id = vat_period_id

    @property
    def period_id(self):
        """Gets the period_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The period_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this JournalEntryLineDraft.


        :param period_id: The period_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._period_id = period_id

    @property
    def payment_id(self):
        """Gets the payment_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The payment_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this JournalEntryLineDraft.


        :param payment_id: The payment_id of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def id(self):
        """Gets the id of this JournalEntryLineDraft.  # noqa: E501


        :return: The id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JournalEntryLineDraft.


        :param id: The id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def vat_type_id(self):
        """Gets the vat_type_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The vat_type_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._vat_type_id

    @vat_type_id.setter
    def vat_type_id(self, vat_type_id):
        """Sets the vat_type_id of this JournalEntryLineDraft.


        :param vat_type_id: The vat_type_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._vat_type_id = vat_type_id

    @property
    def payment_info_type_id(self):
        """Gets the payment_info_type_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The payment_info_type_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._payment_info_type_id

    @payment_info_type_id.setter
    def payment_info_type_id(self, payment_info_type_id):
        """Sets the payment_info_type_id of this JournalEntryLineDraft.


        :param payment_info_type_id: The payment_info_type_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._payment_info_type_id = payment_info_type_id

    @property
    def payment_reference_id(self):
        """Gets the payment_reference_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The payment_reference_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._payment_reference_id

    @payment_reference_id.setter
    def payment_reference_id(self, payment_reference_id):
        """Sets the payment_reference_id of this JournalEntryLineDraft.


        :param payment_reference_id: The payment_reference_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._payment_reference_id = payment_reference_id

    @property
    def currency_code_id(self):
        """Gets the currency_code_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The currency_code_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._currency_code_id

    @currency_code_id.setter
    def currency_code_id(self, currency_code_id):
        """Sets the currency_code_id of this JournalEntryLineDraft.


        :param currency_code_id: The currency_code_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._currency_code_id = currency_code_id

    @property
    def updated_by(self):
        """Gets the updated_by of this JournalEntryLineDraft.  # noqa: E501


        :return: The updated_by of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this JournalEntryLineDraft.


        :param updated_by: The updated_by of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this JournalEntryLineDraft.  # noqa: E501


        :return: The created_by of this JournalEntryLineDraft.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JournalEntryLineDraft.


        :param created_by: The created_by of this JournalEntryLineDraft.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def vat_deduction_percent(self):
        """Gets the vat_deduction_percent of this JournalEntryLineDraft.  # noqa: E501


        :return: The vat_deduction_percent of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._vat_deduction_percent

    @vat_deduction_percent.setter
    def vat_deduction_percent(self, vat_deduction_percent):
        """Sets the vat_deduction_percent of this JournalEntryLineDraft.


        :param vat_deduction_percent: The vat_deduction_percent of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._vat_deduction_percent = vat_deduction_percent

    @property
    def journal_entry_number_numeric(self):
        """Gets the journal_entry_number_numeric of this JournalEntryLineDraft.  # noqa: E501


        :return: The journal_entry_number_numeric of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._journal_entry_number_numeric

    @journal_entry_number_numeric.setter
    def journal_entry_number_numeric(self, journal_entry_number_numeric):
        """Sets the journal_entry_number_numeric of this JournalEntryLineDraft.


        :param journal_entry_number_numeric: The journal_entry_number_numeric of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._journal_entry_number_numeric = journal_entry_number_numeric

    @property
    def journal_entry_type_id(self):
        """Gets the journal_entry_type_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The journal_entry_type_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._journal_entry_type_id

    @journal_entry_type_id.setter
    def journal_entry_type_id(self, journal_entry_type_id):
        """Sets the journal_entry_type_id of this JournalEntryLineDraft.


        :param journal_entry_type_id: The journal_entry_type_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._journal_entry_type_id = journal_entry_type_id

    @property
    def supplier_invoice_id(self):
        """Gets the supplier_invoice_id of this JournalEntryLineDraft.  # noqa: E501


        :return: The supplier_invoice_id of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._supplier_invoice_id

    @supplier_invoice_id.setter
    def supplier_invoice_id(self, supplier_invoice_id):
        """Sets the supplier_invoice_id of this JournalEntryLineDraft.


        :param supplier_invoice_id: The supplier_invoice_id of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._supplier_invoice_id = supplier_invoice_id

    @property
    def batch_number(self):
        """Gets the batch_number of this JournalEntryLineDraft.  # noqa: E501


        :return: The batch_number of this JournalEntryLineDraft.  # noqa: E501
        :rtype: int
        """
        return self._batch_number

    @batch_number.setter
    def batch_number(self, batch_number):
        """Sets the batch_number of this JournalEntryLineDraft.


        :param batch_number: The batch_number of this JournalEntryLineDraft.  # noqa: E501
        :type: int
        """

        self._batch_number = batch_number

    @property
    def dimensions(self):
        """Gets the dimensions of this JournalEntryLineDraft.  # noqa: E501


        :return: The dimensions of this JournalEntryLineDraft.  # noqa: E501
        :rtype: Dimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this JournalEntryLineDraft.


        :param dimensions: The dimensions of this JournalEntryLineDraft.  # noqa: E501
        :type: Dimensions
        """

        self._dimensions = dimensions

    @property
    def accrual(self):
        """Gets the accrual of this JournalEntryLineDraft.  # noqa: E501


        :return: The accrual of this JournalEntryLineDraft.  # noqa: E501
        :rtype: Accrual
        """
        return self._accrual

    @accrual.setter
    def accrual(self, accrual):
        """Sets the accrual of this JournalEntryLineDraft.


        :param accrual: The accrual of this JournalEntryLineDraft.  # noqa: E501
        :type: Accrual
        """

        self._accrual = accrual

    @property
    def custom_values(self):
        """Gets the custom_values of this JournalEntryLineDraft.  # noqa: E501


        :return: The custom_values of this JournalEntryLineDraft.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this JournalEntryLineDraft.


        :param custom_values: The custom_values of this JournalEntryLineDraft.  # noqa: E501
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
        if issubclass(JournalEntryLineDraft, dict):
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
        if not isinstance(other, JournalEntryLineDraft):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
