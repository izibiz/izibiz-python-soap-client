from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from com.izibiz.despatch_advice.eirsaliye_xsd_1 import Base64Binary
from com.izibiz.despatch_advice.eirsaliye_xsd_3 import (
    Request,
    RequestErrortype,
    RequestReturntype,
)
from com.izibiz.despatch_advice.eirsaliye_xsd_4 import (
    AmountType,
    ContentType,
    FlagValue,
    Partinfo,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl"


class DateType(Enum):
    ISSUE = "ISSUE"
    CREATE = "CREATE"


class DespatchResponseStatus(Enum):
    KABUL = "KABUL"
    RED = "RED"


class PrintedFlag(Enum):
    Y = "Y"
    N = "N"


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


@dataclass
class Despatchadviceheader:
    class Meta:
        name = "DESPATCHADVICEHEADER"

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
    profileid: Optional[str] = field(
        default=None,
        metadata={
            "name": "PROFILEID",
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
    issue_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSUE_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    actual_shipment_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ACTUAL_SHIPMENT_DATE",
            "type": "Element",
            "namespace": "",
        }
    )
    actual_shipment_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ACTUAL_SHIPMENT_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYPE_CODE",
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
    sender: Optional[Partinfo] = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiver: Optional[Partinfo] = field(
        default=None,
        metadata={
            "name": "RECEIVER",
            "type": "Element",
            "namespace": "",
        }
    )
    amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AMOUNT",
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
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS_CODE",
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
    email: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EMAIL",
            "type": "Element",
            "namespace": "",
        }
    )
    email_status_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "EMAIL_STATUS_CODE",
            "type": "Element",
            "namespace": "",
        }
    )
    email_status_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMAIL_STATUS_DESCRIPTION",
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


@dataclass
class DespatchadviceProperties:
    class Meta:
        name = "DESPATCHADVICE_PROPERTIES"

    email_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "EMAIL_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EMAIL",
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
class GetDespatchAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    search_key: Optional["GetDespatchAdviceRequest.SearchKey"] = field(
        default=None,
        metadata={
            "name": "SEARCH_KEY",
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
    class SearchKey:
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
        content_type: Optional[ContentType] = field(
            default=None,
            metadata={
                "name": "CONTENT_TYPE",
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


@dataclass
class GetDespatchAdviceStatusRequest(Request):
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
class GetDespatchAdviceWithStatusRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    search_key: Optional["GetDespatchAdviceWithStatusRequest.SearchKey"] = field(
        default=None,
        metadata={
            "name": "SEARCH_KEY",
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
    class SearchKey:
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
        content_type: Optional[ContentType] = field(
            default=None,
            metadata={
                "name": "CONTENT_TYPE",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GetReceiptAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    search_key: Optional["GetReceiptAdviceRequest.SearchKey"] = field(
        default=None,
        metadata={
            "name": "SEARCH_KEY",
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
    class SearchKey:
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
        content_type: Optional[ContentType] = field(
            default=None,
            metadata={
                "name": "CONTENT_TYPE",
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


@dataclass
class GetReceiptAdviceStatusRequest(Request):
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
class LoadDespatchAdviceResponse:
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
class LoadReceiptAdviceResponse:
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
class MarkDespatchAdviceResponse:
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
class MarkReceiptAdviceResponse:
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
class Receiptadviceheader:
    class Meta:
        name = "RECEIPTADVICEHEADER"

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
    profileid: Optional[str] = field(
        default=None,
        metadata={
            "name": "PROFILEID",
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
    issue_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSUE_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    actual_shipment_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ACTUAL_SHIPMENT_DATE",
            "type": "Element",
            "namespace": "",
        }
    )
    actual_shipment_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ACTUAL_SHIPMENT_TIME",
            "type": "Element",
            "namespace": "",
        }
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYPE_CODE",
            "type": "Element",
            "namespace": "",
        }
    )
    sender: Optional[Partinfo] = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiver: Optional[Partinfo] = field(
        default=None,
        metadata={
            "name": "RECEIVER",
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
    despatch_advice_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESPATCH_ADVICE_UUID",
            "type": "Element",
            "namespace": "",
        }
    )
    despatch_advice_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESPATCH_ADVICE_ID",
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
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS_CODE",
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


@dataclass
class RequestFault(RequestErrortype):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class SendDespatchAdviceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESPATCH_ID",
            "type": "Element",
            "namespace": "",
        }
    )
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
class SendDespatchResponseResponse:
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
    receipt_advice_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RECEIPT_ADVICE_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    receipt_advice_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "RECEIPT_ADVICE_UUID",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SendReceiptAdviceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RECEIPT_ID",
            "type": "Element",
            "namespace": "",
        }
    )
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


@dataclass
class Despatchadviceinfo:
    class Meta:
        name = "DESPATCHADVICEINFO"

    despatchadviceheader: Optional[Despatchadviceheader] = field(
        default=None,
        metadata={
            "name": "DESPATCHADVICEHEADER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiptadviceheader: Optional[Receiptadviceheader] = field(
        default=None,
        metadata={
            "name": "RECEIPTADVICEHEADER",
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
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Attribute",
        }
    )


@dataclass
class GetDespatchAdviceStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatchadvice_status: List[Despatchadviceheader] = field(
        default_factory=list,
        metadata={
            "name": "DESPATCHADVICE_STATUS",
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
class GetReceiptAdviceStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    receiptadvice_status: List[Receiptadviceheader] = field(
        default_factory=list,
        metadata={
            "name": "RECEIPTADVICE_STATUS",
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
class Receiptadviceinfo:
    class Meta:
        name = "RECEIPTADVICEINFO"

    receiptadviceheader: Optional[Receiptadviceheader] = field(
        default=None,
        metadata={
            "name": "RECEIPTADVICEHEADER",
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
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Attribute",
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
class Despatchadvice(Despatchadviceinfo):
    class Meta:
        name = "DESPATCHADVICE"

    content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MarkDespatchAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    mark: Optional["MarkDespatchAdviceRequest.Mark"] = field(
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
        despatchadviceinfo: List[Despatchadviceinfo] = field(
            default_factory=list,
            metadata={
                "name": "DESPATCHADVICEINFO",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class MarkReceiptAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    mark: Optional["MarkReceiptAdviceRequest.Mark"] = field(
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
        receiptadviceinfo: List[Receiptadviceinfo] = field(
            default_factory=list,
            metadata={
                "name": "RECEIPTADVICEINFO",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class Receiptadvice(Receiptadviceinfo):
    class Meta:
        name = "RECEIPTADVICE"

    content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetDespatchAdviceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatchadvice: List[Despatchadvice] = field(
        default_factory=list,
        metadata={
            "name": "DESPATCHADVICE",
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
class GetDespatchAdviceWithStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatchadvice: List[Despatchadvice] = field(
        default_factory=list,
        metadata={
            "name": "DESPATCHADVICE",
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
class GetReceiptAdviceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    receiptadvice: List[Receiptadvice] = field(
        default_factory=list,
        metadata={
            "name": "RECEIPTADVICE",
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
class LoadDespatchAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatchadvice: List[Despatchadvice] = field(
        default_factory=list,
        metadata={
            "name": "DESPATCHADVICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    printed_flag: Optional[PrintedFlag] = field(
        default=None,
        metadata={
            "name": "PRINTED_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LoadReceiptAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    receiptadvice: List[Receiptadvice] = field(
        default_factory=list,
        metadata={
            "name": "RECEIPTADVICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SendDespatchAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    sender: Optional["SendDespatchAdviceRequest.Sender"] = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiver: Optional["SendDespatchAdviceRequest.Receiver"] = field(
        default=None,
        metadata={
            "name": "RECEIVER",
            "type": "Element",
            "namespace": "",
        }
    )
    id_assign_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ID_ASSIGN_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    id_assign_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID_ASSIGN_PREFIX",
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
    despatchadvice: List[Despatchadvice] = field(
        default_factory=list,
        metadata={
            "name": "DESPATCHADVICE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    despatchadvice_properties: Optional[DespatchadviceProperties] = field(
        default=None,
        metadata={
            "name": "DESPATCHADVICE_PROPERTIES",
            "type": "Element",
            "namespace": "",
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
class SendDespatchResponseRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    despatchadvice: Optional[Despatchadvice] = field(
        default=None,
        metadata={
            "name": "DESPATCHADVICE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    status: Optional[DespatchResponseStatus] = field(
        default=None,
        metadata={
            "name": "STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESCRIPTION",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SendReceiptAdviceRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    sender: Optional["SendReceiptAdviceRequest.Sender"] = field(
        default=None,
        metadata={
            "name": "SENDER",
            "type": "Element",
            "namespace": "",
        }
    )
    receiver: Optional["SendReceiptAdviceRequest.Receiver"] = field(
        default=None,
        metadata={
            "name": "RECEIVER",
            "type": "Element",
            "namespace": "",
        }
    )
    id_assign_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ID_ASSIGN_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    id_assign_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID_ASSIGN_PREFIX",
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
    receiptadvice: List[Receiptadvice] = field(
        default_factory=list,
        metadata={
            "name": "RECEIPTADVICE",
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
