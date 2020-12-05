# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Payment(object):
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
        'payment_notification_report_file_id': 'int',
        'is_external': 'bool',
        'business_relation_id': 'int',
        'payment_code_id': 'int',
        'description': 'str',
        'customer_invoice_id': 'int',
        'debtor': 'str',
        'serial_number_or_acct_svcr_ref': 'str',
        'is_payment_claim': 'bool',
        'auto_journal': 'bool',
        'invoice_number': 'str',
        'from_bank_account_id': 'int',
        'ocr_payment_strings': 'str',
        'xml_tag_pmt_inf_id_reference': 'str',
        'journal_entry_id': 'int',
        'external_bank_account_number': 'str',
        'status_code': 'int',
        'deleted': 'bool',
        'reconcile_payment': 'bool',
        'xml_tag_end_to_end_id_reference': 'str',
        'domain': 'str',
        'is_payment_cancellation_request': 'bool',
        'in_payment_id': 'str',
        'customer_invoice_reminder_id': 'int',
        'payment_batch_id': 'int',
        'to_bank_account_id': 'int',
        'payment_id': 'str',
        'id': 'int',
        'currency_code_id': 'int',
        'updated_by': 'str',
        'payment_status_report_file_id': 'int',
        'created_by': 'str',
        'proprietary': 'str',
        'status_text': 'str',
        'supplier_invoice_id': 'int',
        'is_customer_payment': 'bool',
        'customer_invoice': 'CustomerInvoice',
        'supplier_invoice': 'SupplierInvoice',
        'customer_invoice_reminder': 'CustomerInvoiceReminder',
        'custom_values': 'CustomValues'
    }

    attribute_map = {
        'payment_notification_report_file_id': 'PaymentNotificationReportFileID',
        'is_external': 'IsExternal',
        'business_relation_id': 'BusinessRelationID',
        'payment_code_id': 'PaymentCodeID',
        'description': 'Description',
        'customer_invoice_id': 'CustomerInvoiceID',
        'debtor': 'Debtor',
        'serial_number_or_acct_svcr_ref': 'SerialNumberOrAcctSvcrRef',
        'is_payment_claim': 'IsPaymentClaim',
        'auto_journal': 'AutoJournal',
        'invoice_number': 'InvoiceNumber',
        'from_bank_account_id': 'FromBankAccountID',
        'ocr_payment_strings': 'OcrPaymentStrings',
        'xml_tag_pmt_inf_id_reference': 'XmlTagPmtInfIdReference',
        'journal_entry_id': 'JournalEntryID',
        'external_bank_account_number': 'ExternalBankAccountNumber',
        'status_code': 'StatusCode',
        'deleted': 'Deleted',
        'reconcile_payment': 'ReconcilePayment',
        'xml_tag_end_to_end_id_reference': 'XmlTagEndToEndIdReference',
        'domain': 'Domain',
        'is_payment_cancellation_request': 'IsPaymentCancellationRequest',
        'in_payment_id': 'InPaymentID',
        'customer_invoice_reminder_id': 'CustomerInvoiceReminderID',
        'payment_batch_id': 'PaymentBatchID',
        'to_bank_account_id': 'ToBankAccountID',
        'payment_id': 'PaymentID',
        'id': 'ID',
        'currency_code_id': 'CurrencyCodeID',
        'updated_by': 'UpdatedBy',
        'payment_status_report_file_id': 'PaymentStatusReportFileID',
        'created_by': 'CreatedBy',
        'proprietary': 'Proprietary',
        'status_text': 'StatusText',
        'supplier_invoice_id': 'SupplierInvoiceID',
        'is_customer_payment': 'IsCustomerPayment',
        'customer_invoice': 'CustomerInvoice',
        'supplier_invoice': 'SupplierInvoice',
        'customer_invoice_reminder': 'CustomerInvoiceReminder',
        'custom_values': 'CustomValues'
    }

    def __init__(self, payment_notification_report_file_id=None, is_external=None, business_relation_id=None, payment_code_id=None, description=None, customer_invoice_id=None, debtor=None, serial_number_or_acct_svcr_ref=None, is_payment_claim=None, auto_journal=None, invoice_number=None, from_bank_account_id=None, ocr_payment_strings=None, xml_tag_pmt_inf_id_reference=None, journal_entry_id=None, external_bank_account_number=None, status_code=None, deleted=None, reconcile_payment=None, xml_tag_end_to_end_id_reference=None, domain=None, is_payment_cancellation_request=None, in_payment_id=None, customer_invoice_reminder_id=None, payment_batch_id=None, to_bank_account_id=None, payment_id=None, id=None, currency_code_id=None, updated_by=None, payment_status_report_file_id=None, created_by=None, proprietary=None, status_text=None, supplier_invoice_id=None, is_customer_payment=None, customer_invoice=None, supplier_invoice=None, customer_invoice_reminder=None, custom_values=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501
        self._payment_notification_report_file_id = None
        self._is_external = None
        self._business_relation_id = None
        self._payment_code_id = None
        self._description = None
        self._customer_invoice_id = None
        self._debtor = None
        self._serial_number_or_acct_svcr_ref = None
        self._is_payment_claim = None
        self._auto_journal = None
        self._invoice_number = None
        self._from_bank_account_id = None
        self._ocr_payment_strings = None
        self._xml_tag_pmt_inf_id_reference = None
        self._journal_entry_id = None
        self._external_bank_account_number = None
        self._status_code = None
        self._deleted = None
        self._reconcile_payment = None
        self._xml_tag_end_to_end_id_reference = None
        self._domain = None
        self._is_payment_cancellation_request = None
        self._in_payment_id = None
        self._customer_invoice_reminder_id = None
        self._payment_batch_id = None
        self._to_bank_account_id = None
        self._payment_id = None
        self._id = None
        self._currency_code_id = None
        self._updated_by = None
        self._payment_status_report_file_id = None
        self._created_by = None
        self._proprietary = None
        self._status_text = None
        self._supplier_invoice_id = None
        self._is_customer_payment = None
        self._customer_invoice = None
        self._supplier_invoice = None
        self._customer_invoice_reminder = None
        self._custom_values = None
        self.discriminator = None
        if payment_notification_report_file_id is not None:
            self.payment_notification_report_file_id = payment_notification_report_file_id
        if is_external is not None:
            self.is_external = is_external
        if business_relation_id is not None:
            self.business_relation_id = business_relation_id
        if payment_code_id is not None:
            self.payment_code_id = payment_code_id
        if description is not None:
            self.description = description
        if customer_invoice_id is not None:
            self.customer_invoice_id = customer_invoice_id
        if debtor is not None:
            self.debtor = debtor
        if serial_number_or_acct_svcr_ref is not None:
            self.serial_number_or_acct_svcr_ref = serial_number_or_acct_svcr_ref
        if is_payment_claim is not None:
            self.is_payment_claim = is_payment_claim
        if auto_journal is not None:
            self.auto_journal = auto_journal
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if from_bank_account_id is not None:
            self.from_bank_account_id = from_bank_account_id
        if ocr_payment_strings is not None:
            self.ocr_payment_strings = ocr_payment_strings
        if xml_tag_pmt_inf_id_reference is not None:
            self.xml_tag_pmt_inf_id_reference = xml_tag_pmt_inf_id_reference
        if journal_entry_id is not None:
            self.journal_entry_id = journal_entry_id
        if external_bank_account_number is not None:
            self.external_bank_account_number = external_bank_account_number
        if status_code is not None:
            self.status_code = status_code
        if deleted is not None:
            self.deleted = deleted
        if reconcile_payment is not None:
            self.reconcile_payment = reconcile_payment
        if xml_tag_end_to_end_id_reference is not None:
            self.xml_tag_end_to_end_id_reference = xml_tag_end_to_end_id_reference
        if domain is not None:
            self.domain = domain
        if is_payment_cancellation_request is not None:
            self.is_payment_cancellation_request = is_payment_cancellation_request
        if in_payment_id is not None:
            self.in_payment_id = in_payment_id
        if customer_invoice_reminder_id is not None:
            self.customer_invoice_reminder_id = customer_invoice_reminder_id
        if payment_batch_id is not None:
            self.payment_batch_id = payment_batch_id
        if to_bank_account_id is not None:
            self.to_bank_account_id = to_bank_account_id
        if payment_id is not None:
            self.payment_id = payment_id
        if id is not None:
            self.id = id
        if currency_code_id is not None:
            self.currency_code_id = currency_code_id
        if updated_by is not None:
            self.updated_by = updated_by
        if payment_status_report_file_id is not None:
            self.payment_status_report_file_id = payment_status_report_file_id
        if created_by is not None:
            self.created_by = created_by
        if proprietary is not None:
            self.proprietary = proprietary
        if status_text is not None:
            self.status_text = status_text
        if supplier_invoice_id is not None:
            self.supplier_invoice_id = supplier_invoice_id
        if is_customer_payment is not None:
            self.is_customer_payment = is_customer_payment
        if customer_invoice is not None:
            self.customer_invoice = customer_invoice
        if supplier_invoice is not None:
            self.supplier_invoice = supplier_invoice
        if customer_invoice_reminder is not None:
            self.customer_invoice_reminder = customer_invoice_reminder
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def payment_notification_report_file_id(self):
        """Gets the payment_notification_report_file_id of this Payment.  # noqa: E501


        :return: The payment_notification_report_file_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._payment_notification_report_file_id

    @payment_notification_report_file_id.setter
    def payment_notification_report_file_id(self, payment_notification_report_file_id):
        """Sets the payment_notification_report_file_id of this Payment.


        :param payment_notification_report_file_id: The payment_notification_report_file_id of this Payment.  # noqa: E501
        :type: int
        """

        self._payment_notification_report_file_id = payment_notification_report_file_id

    @property
    def is_external(self):
        """Gets the is_external of this Payment.  # noqa: E501


        :return: The is_external of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this Payment.


        :param is_external: The is_external of this Payment.  # noqa: E501
        :type: bool
        """

        self._is_external = is_external

    @property
    def business_relation_id(self):
        """Gets the business_relation_id of this Payment.  # noqa: E501


        :return: The business_relation_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._business_relation_id

    @business_relation_id.setter
    def business_relation_id(self, business_relation_id):
        """Sets the business_relation_id of this Payment.


        :param business_relation_id: The business_relation_id of this Payment.  # noqa: E501
        :type: int
        """

        self._business_relation_id = business_relation_id

    @property
    def payment_code_id(self):
        """Gets the payment_code_id of this Payment.  # noqa: E501


        :return: The payment_code_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._payment_code_id

    @payment_code_id.setter
    def payment_code_id(self, payment_code_id):
        """Sets the payment_code_id of this Payment.


        :param payment_code_id: The payment_code_id of this Payment.  # noqa: E501
        :type: int
        """

        self._payment_code_id = payment_code_id

    @property
    def description(self):
        """Gets the description of this Payment.  # noqa: E501


        :return: The description of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Payment.


        :param description: The description of this Payment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer_invoice_id(self):
        """Gets the customer_invoice_id of this Payment.  # noqa: E501


        :return: The customer_invoice_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._customer_invoice_id

    @customer_invoice_id.setter
    def customer_invoice_id(self, customer_invoice_id):
        """Sets the customer_invoice_id of this Payment.


        :param customer_invoice_id: The customer_invoice_id of this Payment.  # noqa: E501
        :type: int
        """

        self._customer_invoice_id = customer_invoice_id

    @property
    def debtor(self):
        """Gets the debtor of this Payment.  # noqa: E501


        :return: The debtor of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._debtor

    @debtor.setter
    def debtor(self, debtor):
        """Sets the debtor of this Payment.


        :param debtor: The debtor of this Payment.  # noqa: E501
        :type: str
        """

        self._debtor = debtor

    @property
    def serial_number_or_acct_svcr_ref(self):
        """Gets the serial_number_or_acct_svcr_ref of this Payment.  # noqa: E501


        :return: The serial_number_or_acct_svcr_ref of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._serial_number_or_acct_svcr_ref

    @serial_number_or_acct_svcr_ref.setter
    def serial_number_or_acct_svcr_ref(self, serial_number_or_acct_svcr_ref):
        """Sets the serial_number_or_acct_svcr_ref of this Payment.


        :param serial_number_or_acct_svcr_ref: The serial_number_or_acct_svcr_ref of this Payment.  # noqa: E501
        :type: str
        """

        self._serial_number_or_acct_svcr_ref = serial_number_or_acct_svcr_ref

    @property
    def is_payment_claim(self):
        """Gets the is_payment_claim of this Payment.  # noqa: E501


        :return: The is_payment_claim of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_payment_claim

    @is_payment_claim.setter
    def is_payment_claim(self, is_payment_claim):
        """Sets the is_payment_claim of this Payment.


        :param is_payment_claim: The is_payment_claim of this Payment.  # noqa: E501
        :type: bool
        """

        self._is_payment_claim = is_payment_claim

    @property
    def auto_journal(self):
        """Gets the auto_journal of this Payment.  # noqa: E501


        :return: The auto_journal of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._auto_journal

    @auto_journal.setter
    def auto_journal(self, auto_journal):
        """Sets the auto_journal of this Payment.


        :param auto_journal: The auto_journal of this Payment.  # noqa: E501
        :type: bool
        """

        self._auto_journal = auto_journal

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Payment.  # noqa: E501


        :return: The invoice_number of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Payment.


        :param invoice_number: The invoice_number of this Payment.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def from_bank_account_id(self):
        """Gets the from_bank_account_id of this Payment.  # noqa: E501


        :return: The from_bank_account_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._from_bank_account_id

    @from_bank_account_id.setter
    def from_bank_account_id(self, from_bank_account_id):
        """Sets the from_bank_account_id of this Payment.


        :param from_bank_account_id: The from_bank_account_id of this Payment.  # noqa: E501
        :type: int
        """

        self._from_bank_account_id = from_bank_account_id

    @property
    def ocr_payment_strings(self):
        """Gets the ocr_payment_strings of this Payment.  # noqa: E501


        :return: The ocr_payment_strings of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._ocr_payment_strings

    @ocr_payment_strings.setter
    def ocr_payment_strings(self, ocr_payment_strings):
        """Sets the ocr_payment_strings of this Payment.


        :param ocr_payment_strings: The ocr_payment_strings of this Payment.  # noqa: E501
        :type: str
        """

        self._ocr_payment_strings = ocr_payment_strings

    @property
    def xml_tag_pmt_inf_id_reference(self):
        """Gets the xml_tag_pmt_inf_id_reference of this Payment.  # noqa: E501


        :return: The xml_tag_pmt_inf_id_reference of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._xml_tag_pmt_inf_id_reference

    @xml_tag_pmt_inf_id_reference.setter
    def xml_tag_pmt_inf_id_reference(self, xml_tag_pmt_inf_id_reference):
        """Sets the xml_tag_pmt_inf_id_reference of this Payment.


        :param xml_tag_pmt_inf_id_reference: The xml_tag_pmt_inf_id_reference of this Payment.  # noqa: E501
        :type: str
        """

        self._xml_tag_pmt_inf_id_reference = xml_tag_pmt_inf_id_reference

    @property
    def journal_entry_id(self):
        """Gets the journal_entry_id of this Payment.  # noqa: E501


        :return: The journal_entry_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._journal_entry_id

    @journal_entry_id.setter
    def journal_entry_id(self, journal_entry_id):
        """Sets the journal_entry_id of this Payment.


        :param journal_entry_id: The journal_entry_id of this Payment.  # noqa: E501
        :type: int
        """

        self._journal_entry_id = journal_entry_id

    @property
    def external_bank_account_number(self):
        """Gets the external_bank_account_number of this Payment.  # noqa: E501


        :return: The external_bank_account_number of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._external_bank_account_number

    @external_bank_account_number.setter
    def external_bank_account_number(self, external_bank_account_number):
        """Sets the external_bank_account_number of this Payment.


        :param external_bank_account_number: The external_bank_account_number of this Payment.  # noqa: E501
        :type: str
        """

        self._external_bank_account_number = external_bank_account_number

    @property
    def status_code(self):
        """Gets the status_code of this Payment.  # noqa: E501


        :return: The status_code of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Payment.


        :param status_code: The status_code of this Payment.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def deleted(self):
        """Gets the deleted of this Payment.  # noqa: E501


        :return: The deleted of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Payment.


        :param deleted: The deleted of this Payment.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def reconcile_payment(self):
        """Gets the reconcile_payment of this Payment.  # noqa: E501


        :return: The reconcile_payment of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._reconcile_payment

    @reconcile_payment.setter
    def reconcile_payment(self, reconcile_payment):
        """Sets the reconcile_payment of this Payment.


        :param reconcile_payment: The reconcile_payment of this Payment.  # noqa: E501
        :type: bool
        """

        self._reconcile_payment = reconcile_payment

    @property
    def xml_tag_end_to_end_id_reference(self):
        """Gets the xml_tag_end_to_end_id_reference of this Payment.  # noqa: E501


        :return: The xml_tag_end_to_end_id_reference of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._xml_tag_end_to_end_id_reference

    @xml_tag_end_to_end_id_reference.setter
    def xml_tag_end_to_end_id_reference(self, xml_tag_end_to_end_id_reference):
        """Sets the xml_tag_end_to_end_id_reference of this Payment.


        :param xml_tag_end_to_end_id_reference: The xml_tag_end_to_end_id_reference of this Payment.  # noqa: E501
        :type: str
        """

        self._xml_tag_end_to_end_id_reference = xml_tag_end_to_end_id_reference

    @property
    def domain(self):
        """Gets the domain of this Payment.  # noqa: E501


        :return: The domain of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Payment.


        :param domain: The domain of this Payment.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def is_payment_cancellation_request(self):
        """Gets the is_payment_cancellation_request of this Payment.  # noqa: E501


        :return: The is_payment_cancellation_request of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_payment_cancellation_request

    @is_payment_cancellation_request.setter
    def is_payment_cancellation_request(self, is_payment_cancellation_request):
        """Sets the is_payment_cancellation_request of this Payment.


        :param is_payment_cancellation_request: The is_payment_cancellation_request of this Payment.  # noqa: E501
        :type: bool
        """

        self._is_payment_cancellation_request = is_payment_cancellation_request

    @property
    def in_payment_id(self):
        """Gets the in_payment_id of this Payment.  # noqa: E501


        :return: The in_payment_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._in_payment_id

    @in_payment_id.setter
    def in_payment_id(self, in_payment_id):
        """Sets the in_payment_id of this Payment.


        :param in_payment_id: The in_payment_id of this Payment.  # noqa: E501
        :type: str
        """

        self._in_payment_id = in_payment_id

    @property
    def customer_invoice_reminder_id(self):
        """Gets the customer_invoice_reminder_id of this Payment.  # noqa: E501


        :return: The customer_invoice_reminder_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._customer_invoice_reminder_id

    @customer_invoice_reminder_id.setter
    def customer_invoice_reminder_id(self, customer_invoice_reminder_id):
        """Sets the customer_invoice_reminder_id of this Payment.


        :param customer_invoice_reminder_id: The customer_invoice_reminder_id of this Payment.  # noqa: E501
        :type: int
        """

        self._customer_invoice_reminder_id = customer_invoice_reminder_id

    @property
    def payment_batch_id(self):
        """Gets the payment_batch_id of this Payment.  # noqa: E501


        :return: The payment_batch_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._payment_batch_id

    @payment_batch_id.setter
    def payment_batch_id(self, payment_batch_id):
        """Sets the payment_batch_id of this Payment.


        :param payment_batch_id: The payment_batch_id of this Payment.  # noqa: E501
        :type: int
        """

        self._payment_batch_id = payment_batch_id

    @property
    def to_bank_account_id(self):
        """Gets the to_bank_account_id of this Payment.  # noqa: E501


        :return: The to_bank_account_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._to_bank_account_id

    @to_bank_account_id.setter
    def to_bank_account_id(self, to_bank_account_id):
        """Sets the to_bank_account_id of this Payment.


        :param to_bank_account_id: The to_bank_account_id of this Payment.  # noqa: E501
        :type: int
        """

        self._to_bank_account_id = to_bank_account_id

    @property
    def payment_id(self):
        """Gets the payment_id of this Payment.  # noqa: E501


        :return: The payment_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this Payment.


        :param payment_id: The payment_id of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def id(self):
        """Gets the id of this Payment.  # noqa: E501


        :return: The id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.


        :param id: The id of this Payment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def currency_code_id(self):
        """Gets the currency_code_id of this Payment.  # noqa: E501


        :return: The currency_code_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._currency_code_id

    @currency_code_id.setter
    def currency_code_id(self, currency_code_id):
        """Sets the currency_code_id of this Payment.


        :param currency_code_id: The currency_code_id of this Payment.  # noqa: E501
        :type: int
        """

        self._currency_code_id = currency_code_id

    @property
    def updated_by(self):
        """Gets the updated_by of this Payment.  # noqa: E501


        :return: The updated_by of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Payment.


        :param updated_by: The updated_by of this Payment.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def payment_status_report_file_id(self):
        """Gets the payment_status_report_file_id of this Payment.  # noqa: E501


        :return: The payment_status_report_file_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._payment_status_report_file_id

    @payment_status_report_file_id.setter
    def payment_status_report_file_id(self, payment_status_report_file_id):
        """Sets the payment_status_report_file_id of this Payment.


        :param payment_status_report_file_id: The payment_status_report_file_id of this Payment.  # noqa: E501
        :type: int
        """

        self._payment_status_report_file_id = payment_status_report_file_id

    @property
    def created_by(self):
        """Gets the created_by of this Payment.  # noqa: E501


        :return: The created_by of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Payment.


        :param created_by: The created_by of this Payment.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def proprietary(self):
        """Gets the proprietary of this Payment.  # noqa: E501


        :return: The proprietary of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._proprietary

    @proprietary.setter
    def proprietary(self, proprietary):
        """Sets the proprietary of this Payment.


        :param proprietary: The proprietary of this Payment.  # noqa: E501
        :type: str
        """

        self._proprietary = proprietary

    @property
    def status_text(self):
        """Gets the status_text of this Payment.  # noqa: E501


        :return: The status_text of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """Sets the status_text of this Payment.


        :param status_text: The status_text of this Payment.  # noqa: E501
        :type: str
        """

        self._status_text = status_text

    @property
    def supplier_invoice_id(self):
        """Gets the supplier_invoice_id of this Payment.  # noqa: E501


        :return: The supplier_invoice_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._supplier_invoice_id

    @supplier_invoice_id.setter
    def supplier_invoice_id(self, supplier_invoice_id):
        """Sets the supplier_invoice_id of this Payment.


        :param supplier_invoice_id: The supplier_invoice_id of this Payment.  # noqa: E501
        :type: int
        """

        self._supplier_invoice_id = supplier_invoice_id

    @property
    def is_customer_payment(self):
        """Gets the is_customer_payment of this Payment.  # noqa: E501


        :return: The is_customer_payment of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_customer_payment

    @is_customer_payment.setter
    def is_customer_payment(self, is_customer_payment):
        """Sets the is_customer_payment of this Payment.


        :param is_customer_payment: The is_customer_payment of this Payment.  # noqa: E501
        :type: bool
        """

        self._is_customer_payment = is_customer_payment

    @property
    def customer_invoice(self):
        """Gets the customer_invoice of this Payment.  # noqa: E501


        :return: The customer_invoice of this Payment.  # noqa: E501
        :rtype: CustomerInvoice
        """
        return self._customer_invoice

    @customer_invoice.setter
    def customer_invoice(self, customer_invoice):
        """Sets the customer_invoice of this Payment.


        :param customer_invoice: The customer_invoice of this Payment.  # noqa: E501
        :type: CustomerInvoice
        """

        self._customer_invoice = customer_invoice

    @property
    def supplier_invoice(self):
        """Gets the supplier_invoice of this Payment.  # noqa: E501


        :return: The supplier_invoice of this Payment.  # noqa: E501
        :rtype: SupplierInvoice
        """
        return self._supplier_invoice

    @supplier_invoice.setter
    def supplier_invoice(self, supplier_invoice):
        """Sets the supplier_invoice of this Payment.


        :param supplier_invoice: The supplier_invoice of this Payment.  # noqa: E501
        :type: SupplierInvoice
        """

        self._supplier_invoice = supplier_invoice

    @property
    def customer_invoice_reminder(self):
        """Gets the customer_invoice_reminder of this Payment.  # noqa: E501


        :return: The customer_invoice_reminder of this Payment.  # noqa: E501
        :rtype: CustomerInvoiceReminder
        """
        return self._customer_invoice_reminder

    @customer_invoice_reminder.setter
    def customer_invoice_reminder(self, customer_invoice_reminder):
        """Sets the customer_invoice_reminder of this Payment.


        :param customer_invoice_reminder: The customer_invoice_reminder of this Payment.  # noqa: E501
        :type: CustomerInvoiceReminder
        """

        self._customer_invoice_reminder = customer_invoice_reminder

    @property
    def custom_values(self):
        """Gets the custom_values of this Payment.  # noqa: E501


        :return: The custom_values of this Payment.  # noqa: E501
        :rtype: CustomValues
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this Payment.


        :param custom_values: The custom_values of this Payment.  # noqa: E501
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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
