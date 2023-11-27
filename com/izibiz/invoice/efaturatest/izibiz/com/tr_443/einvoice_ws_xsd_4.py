from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from com.izibiz.invoice.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_1 import (
    AmountType,
    FlagValue,
)
from com.izibiz.invoice.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_2 import (
    Request,
    RequestErrortype,
    RequestHeadertype,
    RequestReturntype,
)
from com.izibiz.invoice.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_3 import Base64Binary

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl"


class DateType(Enum):
    ISSUE = "ISSUE"
    CREATE = "CREATE"


@dataclass
class Gibuser:
    class Meta:
        name = "GIBUSER"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Element",
            "namespace": "",
        }
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALIAS",
            "type": "Element",
            "namespace": "",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Element",
            "namespace": "",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    register_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "REGISTER_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "UNIT",
            "type": "Element",
            "namespace": "",
        }
    )
    alias_creation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALIAS_CREATION_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOCUMENT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetInvoiceCountResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    portal: Optional[int] = field(
        default=None,
        metadata={
            "name": "PORTAL",
            "type": "Element",
            "namespace": "",
        }
    )
    ws: Optional[int] = field(
        default=None,
        metadata={
            "name": "WS",
            "type": "Element",
            "namespace": "",
        }
    )


class GetUserListBinaryRequestType(Enum):
    CSV = "CSV"
    XML = "XML"


class MarkValue(Enum):
    READ = "READ"
    UNREAD = "UNREAD"


class Signtype(Enum):
    HSM_CUSTOMER = "HSM_CUSTOMER"
    HSM_ENTEGRATOR = "HSM_ENTEGRATOR"
    HSM_CLIENT_SIGNED = "HSM_CLIENT_SIGNED"
    TOKEN_CUSTOMER = "TOKEN_CUSTOMER"
    TOKEN_ENTEGRATOR = "TOKEN_ENTEGRATOR"


class Usercontenttype(Enum):
    PROCESSUSER = "PROCESSUSER"
    CANCELUSER = "CANCELUSER"


class Usertype(Enum):
    USER = "USER"
    ARCHIVE = "ARCHIVE"
    EARCHIVE = "EARCHIVE"
    EARCHIVE_ARCHIVE = "EARCHIVE_ARCHIVE"
    EDESPATCH = "EDESPATCH"
    EDESPATCH_ARCHIVE = "EDESPATCH_ARCHIVE"
    SERBEST_MESLEK = "SERBEST_MESLEK"
    MUSTAHSIL = "MUSTAHSIL"
    CHANGECUSTOMER = "CHANGECUSTOMER"
    ZREPORT = "ZREPORT"
    EBILL = "EBILL"
    EXCHANGE = "EXCHANGE"
    SIGORTAGIDER = "SIGORTAGIDER"


@dataclass
class ArchiveInvoiceRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Element",
            "namespace": "",
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ArchiveInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CancelDraftInvoiceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CancelDraftInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CancelUserResponse(RequestReturntype):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class CheckUserRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    user: Optional[Gibuser] = field(
        default=None,
        metadata={
            "name": "USER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CheckUserResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    user: List[Gibuser] = field(
        default_factory=list,
        metadata={
            "name": "USER",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Envelope:
    class Meta:
        name = "ENVELOPE"

    header: Optional["Envelope.Header"] = field(
        default=None,
        metadata={
            "name": "HEADER",
            "type": "Element",
            "namespace": "",
        }
    )
    content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )
    instanceidentifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "INSTANCEIDENTIFIER",
            "type": "Attribute",
        }
    )

    @dataclass
    class Header:
        sender: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Element",
                "namespace": "",
            }
        )
        receiver: Optional[str] = field(
            default=None,
            metadata={
                "name": "RECEIVER",
                "type": "Element",
                "namespace": "",
            }
        )
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "FROM",
                "type": "Element",
                "namespace": "",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "TO",
                "type": "Element",
                "namespace": "",
            }
        )
        date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        status: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "TYPE",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetEnvelopeRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    envelope_search_key: Optional["GetEnvelopeRequest.EnvelopeSearchKey"] = field(
        default=None,
        metadata={
            "name": "ENVELOPE_SEARCH_KEY",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    header_only: Optional[str] = field(
        default=None,
        metadata={
            "name": "HEADER_ONLY",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class EnvelopeSearchKey:
        limit: Optional[int] = field(
            default=None,
            metadata={
                "name": "LIMIT",
                "type": "Element",
                "namespace": "",
            }
        )
        identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "FROM",
                "type": "Element",
                "namespace": "",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "TO",
                "type": "Element",
                "namespace": "",
            }
        )
        start_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "START_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        end_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "END_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        read_included: Optional[bool] = field(
            default=None,
            metadata={
                "name": "READ_INCLUDED",
                "type": "Element",
                "namespace": "",
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        sender: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Element",
                "namespace": "",
            }
        )
        receiver: Optional[str] = field(
            default=None,
            metadata={
                "name": "RECEIVER",
                "type": "Element",
                "namespace": "",
            }
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "TYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        element: Optional["GetEnvelopeRequest.EnvelopeSearchKey.Element"] = field(
            default=None,
            metadata={
                "name": "ELEMENT",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class Element:
            """
            Used to search for the envelopes having package content with the given type and
            uuid with this element.

            :ivar type_value: One of the values of
                (INVOICE,APPLICATIONRESPONSE)
            :ivar uuid: UUID of the target element
            """
            type_value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TYPE",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            uuid: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UUID",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )


@dataclass
class GetEnvelopeStatusRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    envelope: List["GetEnvelopeStatusRequest.Envelope"] = field(
        default_factory=list,
        metadata={
            "name": "ENVELOPE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Envelope:
        instanceidentifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "INSTANCEIDENTIFIER",
                "type": "Attribute",
            }
        )


@dataclass
class GetInvoiceCountRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    issue_date_start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ISSUE_DATE_START",
            "type": "Element",
            "namespace": "",
        }
    )
    issue_date_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ISSUE_DATE_END",
            "type": "Element",
            "namespace": "",
        }
    )
    cdate_start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CDATE_START",
            "type": "Element",
            "namespace": "",
        }
    )
    cdate_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CDATE_END",
            "type": "Element",
            "namespace": "",
        }
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetInvoiceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice_search_key: Optional["GetInvoiceRequest.InvoiceSearchKey"] = field(
        default=None,
        metadata={
            "name": "INVOICE_SEARCH_KEY",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    header_only: Optional[str] = field(
        default=None,
        metadata={
            "name": "HEADER_ONLY",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class InvoiceSearchKey:
        limit: Optional[int] = field(
            default=None,
            metadata={
                "name": "LIMIT",
                "type": "Element",
                "namespace": "",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Element",
                "namespace": "",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "UUID",
                "type": "Element",
                "namespace": "",
            }
        )
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "FROM",
                "type": "Element",
                "namespace": "",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "TO",
                "type": "Element",
                "namespace": "",
            }
        )
        date_type: Optional[DateType] = field(
            default=None,
            metadata={
                "name": "DATE_TYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        start_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "START_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        end_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "END_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        read_included: Optional[bool] = field(
            default=None,
            metadata={
                "name": "READ_INCLUDED",
                "type": "Element",
                "namespace": "",
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        sender: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Element",
                "namespace": "",
            }
        )
        receiver: Optional[str] = field(
            default=None,
            metadata={
                "name": "RECEIVER",
                "type": "Element",
                "namespace": "",
            }
        )
        draft_flag: Optional[str] = field(
            default=None,
            metadata={
                "name": "DRAFT_FLAG",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetInvoiceStatusAllRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    uuid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class GetInvoiceWithTypeRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice_search_key: Optional["GetInvoiceWithTypeRequest.InvoiceSearchKey"] = field(
        default=None,
        metadata={
            "name": "INVOICE_SEARCH_KEY",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    header_only: Optional[str] = field(
        default=None,
        metadata={
            "name": "HEADER_ONLY",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class InvoiceSearchKey:
        limit: Optional[int] = field(
            default=None,
            metadata={
                "name": "LIMIT",
                "type": "Element",
                "namespace": "",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Element",
                "namespace": "",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "UUID",
                "type": "Element",
                "namespace": "",
            }
        )
        external_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "EXTERNAL_ID",
                "type": "Element",
                "namespace": "",
            }
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "TYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "FROM",
                "type": "Element",
                "namespace": "",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "TO",
                "type": "Element",
                "namespace": "",
            }
        )
        start_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "START_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        end_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "END_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        read_included: Optional[bool] = field(
            default=None,
            metadata={
                "name": "READ_INCLUDED",
                "type": "Element",
                "namespace": "",
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        sender: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Element",
                "namespace": "",
            }
        )
        receiver: Optional[str] = field(
            default=None,
            metadata={
                "name": "RECEIVER",
                "type": "Element",
                "namespace": "",
            }
        )
        payable_amount: Optional[AmountType] = field(
            default=None,
            metadata={
                "name": "PAYABLE_AMOUNT",
                "type": "Element",
                "namespace": "",
            }
        )
        draft_flag: Optional[str] = field(
            default=None,
            metadata={
                "name": "DRAFT_FLAG",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetUserListBinaryRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    type_value: Optional[GetUserListBinaryRequestType] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOCUMENT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    register_time_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "REGISTER_TIME_START",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetUserListBinaryResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetUserListRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    register_time_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "REGISTER_TIME_START",
            "type": "Element",
            "namespace": "",
        }
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOCUMENT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetUserListResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    user: List[Gibuser] = field(
        default_factory=list,
        metadata={
            "name": "USER",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Invoice:
    class Meta:
        name = "INVOICE"

    header: Optional["Invoice.Header"] = field(
        default=None,
        metadata={
            "name": "HEADER",
            "type": "Element",
            "namespace": "",
        }
    )
    content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )
    list_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LIST_ID",
            "type": "Attribute",
        }
    )

    @dataclass
    class Header:
        sender: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER",
                "type": "Element",
                "namespace": "",
            }
        )
        receiver: Optional[str] = field(
            default=None,
            metadata={
                "name": "RECEIVER",
                "type": "Element",
                "namespace": "",
            }
        )
        supplier: Optional[str] = field(
            default=None,
            metadata={
                "name": "SUPPLIER",
                "type": "Element",
                "namespace": "",
            }
        )
        customer: Optional[str] = field(
            default=None,
            metadata={
                "name": "CUSTOMER",
                "type": "Element",
                "namespace": "",
            }
        )
        issue_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "ISSUE_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        payable_amount: Optional[AmountType] = field(
            default=None,
            metadata={
                "name": "PAYABLE_AMOUNT",
                "type": "Element",
                "namespace": "",
            }
        )
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "FROM",
                "type": "Element",
                "namespace": "",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "TO",
                "type": "Element",
                "namespace": "",
            }
        )
        profileid: Optional[str] = field(
            default=None,
            metadata={
                "name": "PROFILEID",
                "type": "Element",
                "namespace": "",
            }
        )
        invoice_type_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_TYPE_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        status: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        response_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        response_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        filename: Optional[str] = field(
            default=None,
            metadata={
                "name": "FILENAME",
                "type": "Element",
                "namespace": "",
            }
        )
        hash: Optional[str] = field(
            default=None,
            metadata={
                "name": "HASH",
                "type": "Element",
                "namespace": "",
            }
        )
        cdate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "CDATE",
                "type": "Element",
                "namespace": "",
            }
        )
        envelope_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "ENVELOPE_IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_refno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_REFNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_gcb_tescilno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_GCB_TESCILNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_fiili_ihracat_tarihi: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_FIILI_IHRACAT_TARIHI",
                "type": "Element",
                "namespace": "",
            }
        )
        status_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class LoadInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LoginRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "USER_NAME",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "name": "PASSWORD",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class LoginResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    session_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SESSION_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LogoutRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class LogoutResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MarkEnvelopeRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    mark: Optional["MarkEnvelopeRequest.Mark"] = field(
        default=None,
        metadata={
            "name": "MARK",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Mark:
        envelope: List["MarkEnvelopeRequest.Mark.Envelope"] = field(
            default_factory=list,
            metadata={
                "name": "ENVELOPE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        value: Optional[MarkValue] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass
        class Envelope:
            instanceidentifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "INSTANCEIDENTIFIER",
                    "type": "Attribute",
                }
            )


@dataclass
class MarkEnvelopeResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MarkInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PrepareInvoiceResponseResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    appresponse: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "APPRESPONSE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ProcessUserResponse(RequestReturntype):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class RequestFault(RequestErrortype):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class SendInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    invoice_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "INVOICE_ID",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SendInvoiceResponseRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    appresponse: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "APPRESPONSE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SendInvoiceResponseResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SendInvoiceResponseWithServerSignResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    request_return: Optional[RequestReturntype] = field(
        default=None,
        metadata={
            "name": "REQUEST_RETURN",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Usercontent(Base64Binary):
    class Meta:
        name = "USERCONTENT"

    userid: Optional[str] = field(
        default=None,
        metadata={
            "name": "USERID",
            "type": "Attribute",
        }
    )
    usertype: Optional[Usertype] = field(
        default=None,
        metadata={
            "name": "USERTYPE",
            "type": "Attribute",
        }
    )
    signtype: Optional[Signtype] = field(
        default=None,
        metadata={
            "name": "SIGNTYPE",
            "type": "Attribute",
        }
    )
    type_value: Optional[Usercontenttype] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        }
    )
    alias_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALIAS_TYPE",
            "type": "Attribute",
        }
    )


@dataclass
class GetEnvelopeResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    envelope: List[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "ENVELOPE",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetEnvelopeStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    envelope: List[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "ENVELOPE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetInvoiceStatusAllResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice_status: List["GetInvoiceStatusAllResponse.InvoiceStatus"] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE_STATUS",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class InvoiceStatus(Invoice):
        status: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        response_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        response_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        cdate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "CDATE",
                "type": "Element",
                "namespace": "",
            }
        )
        envelope_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "ENVELOPE_IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_refno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_REFNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_gcb_tescilno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_GCB_TESCILNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_fiili_ihracat_tarihi: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_FIILI_IHRACAT_TARIHI",
                "type": "Element",
                "namespace": "",
            }
        )
        status_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        web_key: Optional[str] = field(
            default=None,
            metadata={
                "name": "WEB_KEY",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetInvoiceStatusRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice: Optional[Invoice] = field(
        default=None,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GetInvoiceStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice_status: Optional["GetInvoiceStatusResponse.InvoiceStatus"] = field(
        default=None,
        metadata={
            "name": "INVOICE_STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class InvoiceStatus(Invoice):
        status: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        gib_status_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_status_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_STATUS_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        response_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        response_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "RESPONSE_DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        cdate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "CDATE",
                "type": "Element",
                "namespace": "",
            }
        )
        envelope_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "ENVELOPE_IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_refno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_REFNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_gcb_tescilno: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_GCB_TESCILNO",
                "type": "Element",
                "namespace": "",
            }
        )
        gtb_fiili_ihracat_tarihi: Optional[str] = field(
            default=None,
            metadata={
                "name": "GTB_FIILI_IHRACAT_TARIHI",
                "type": "Element",
                "namespace": "",
            }
        )
        status_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_CODE",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        direction: Optional[str] = field(
            default=None,
            metadata={
                "name": "DIRECTION",
                "type": "Element",
                "namespace": "",
            }
        )
        web_key: Optional[str] = field(
            default=None,
            metadata={
                "name": "WEB_KEY",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetInvoiceWithTypeResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
        }
    )
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LoadInvoiceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    validation_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "VALIDATION_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MarkInvoiceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    mark: Optional["MarkInvoiceRequest.Mark"] = field(
        default=None,
        metadata={
            "name": "MARK",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Mark:
        invoice: List[Invoice] = field(
            default_factory=list,
            metadata={
                "name": "INVOICE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        value: Optional[MarkValue] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class PrepareInvoiceResponseRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DESCRIPTION",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SendInvoiceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    sender: Optional["SendInvoiceRequest.Sender"] = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiver: Optional["SendInvoiceRequest.Receiver"] = field(
        default=None,
        metadata={
            "name": "RECEIVER",
            "type": "Element",
            "namespace": "",
        }
    )
    xslt_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "XSLT_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    seri_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "SERI_PREFIX",
            "type": "Element",
            "namespace": "",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z0-9]+",
        }
    )
    disable_date_control: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "DISABLE_DATE_CONTROL",
            "type": "Element",
            "namespace": "",
        }
    )
    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Sender:
        vkn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        alias: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Receiver:
        vkn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        alias: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class SendInvoiceResponseWithServerSignRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    invoice: List[Invoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DESCRIPTION",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class UserRequest(Request):
    usercontent: List[Usercontent] = field(
        default_factory=list,
        metadata={
            "name": "USERCONTENT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class UserResponse:
    usercontent: List[Usercontent] = field(
        default_factory=list,
        metadata={
            "name": "USERCONTENT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class CancelUserRequest(UserRequest):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class PrepareCancelUserRequest(UserRequest):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class PrepareCancelUserResponse(UserResponse):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class PrepareProcessUserRequest(UserRequest):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class PrepareProcessUserResponse(UserResponse):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class ProcessUserRequest(UserRequest):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"
