from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_7 import (
    RequestErrortype,
    RequestHeadertype,
    RequestReturntype,
)
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_8 import Base64Binary

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl/archive"


class DocType(Enum):
    KEBIR_DEFTERI = "KEBIR DEFTERI"
    YEVMIYE_DEFTERI = "YEVMIYE DEFTERI"
    KEBIR_BERATI = "KEBIR BERATI"
    YEVMIYE_BERATI = "YEVMIYE BERATI"
    GIB_KEBIR_BERATI = "GIB KEBIR BERATI"
    GIB_YEVMIYE_BERATI = "GIB YEVMIYE BERATI"
    DEFTER_RAPORU = "DEFTER RAPORU"


@dataclass
class EarchiveInvoice:
    class Meta:
        name = "EARCHIVE_INVOICE"

    header: Optional["EarchiveInvoice.Header"] = field(
        default=None,
        metadata={
            "name": "HEADER",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Header:
        invoice_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_ID",
                "type": "Element",
                "namespace": "",
            }
        )
        profile: Optional[str] = field(
            default=None,
            metadata={
                "name": "PROFILE",
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
        invoice_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_DATE",
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
        status_desc: Optional[str] = field(
            default=None,
            metadata={
                "name": "STATUS_DESC",
                "type": "Element",
                "namespace": "",
            }
        )
        email_status: Optional[str] = field(
            default=None,
            metadata={
                "name": "EMAIL_STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        email_status_desc: Optional[str] = field(
            default=None,
            metadata={
                "name": "EMAIL_STATUS_DESC",
                "type": "Element",
                "namespace": "",
            }
        )
        report_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "REPORT_ID",
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


class EarsivTypeValue(Enum):
    INTERNET = "INTERNET"
    NORMAL = "NORMAL"


@dataclass
class EcommerceUpload:
    class Meta:
        name = "ECOMMERCE_UPLOAD"

    ecommerce_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ECOMMERCE_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    ecommerce_package_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ECOMMERCE_PACKAGE_ID",
            "type": "Element",
            "namespace": "",
        }
    )


class FlagValue(Enum):
    Y = "Y"
    N = "N"


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

    @dataclass
    class Header:
        invoice_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_ID",
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
        profile_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "PROFILE_ID",
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
        sub_status: Optional[str] = field(
            default=None,
            metadata={
                "name": "SUB_STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        issue_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISSUE_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        cdate: Optional[str] = field(
            default=None,
            metadata={
                "name": "CDATE",
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


class MarkValue(Enum):
    READ = "READ"
    UNREAD = "UNREAD"


@dataclass
class Report:
    class Meta:
        name = "REPORT"

    report_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_NO",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    report_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_PERIOD",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    report_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    report_sub_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_SUB_STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ReportInvoice:
    class Meta:
        name = "REPORT_INVOICE"

    invoice_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "INVOICE_ID",
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    status_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "STATUS_DESC",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    invoice_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "INVOICE_DATE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CDATE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    payable_amount: Optional[int] = field(
        default=None,
        metadata={
            "name": "PAYABLE_AMOUNT",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    email_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMAIL_STATUS",
            "type": "Element",
            "namespace": "",
        }
    )
    email_status_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMAIL_STATUS_DESC",
            "type": "Element",
            "namespace": "",
        }
    )


class SubStatusValue(Enum):
    NEW = "NEW"
    DRAFT = "DRAFT"


@dataclass
class ArchiveGenericDocumentResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class ArchiveGetInvoiceInfoRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    page_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "PAGE_SIZE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "PAGE_NUMBER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ArchiveGetInvoiceInfoResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    page_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "PAGE_SIZE",
            "type": "Element",
            "namespace": "",
        }
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "PAGE_NUMBER",
            "type": "Element",
            "namespace": "",
        }
    )
    total_invoice_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TOTAL_INVOICE_COUNT",
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
class ArchiveInvoiceCopyRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    invoice_uuid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE_UUID",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    portal_direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "PORTAL_DIRECTION",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    external_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "EXTERNAL_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    archive_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ARCHIVE_NOTE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ArchiveInvoiceCopyResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class ArchiveInvoiceExtendedResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
    web_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "WEB_KEY",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ArchiveInvoiceReadRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    invoiceid: Optional[str] = field(
        default=None,
        metadata={
            "name": "INVOICEID",
            "type": "Element",
            "namespace": "",
        }
    )
    portal_direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "PORTAL_DIRECTION",
            "type": "Element",
            "namespace": "",
        }
    )
    external_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "EXTERNAL_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "PROFILE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ArchiveInvoiceReadResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    invoice: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
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
class ArchiveInvoiceWriteContent:
    elements: List["ArchiveInvoiceWriteContent.Elements"] = field(
        default_factory=list,
        metadata={
            "name": "Elements",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Elements:
        element_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "ElementType",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        element_count: Optional[int] = field(
            default=None,
            metadata={
                "name": "ElementCount",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        element_list: List[Base64Binary] = field(
            default_factory=list,
            metadata={
                "name": "ElementList",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class ArchiveInvoiceWriteResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class CancelEarchiveInvoiceRequest:
    class Meta:
        name = "CancelEArchiveInvoiceRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cancel_earsiv_invoice_content: List["CancelEarchiveInvoiceRequest.CancelEarsivInvoiceContent"] = field(
        default_factory=list,
        metadata={
            "name": "CancelEArsivInvoiceContent",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class CancelEarsivInvoiceContent:
        upload_flag: Optional[FlagValue] = field(
            default=None,
            metadata={
                "name": "UPLOAD_FLAG",
                "type": "Element",
                "namespace": "",
            }
        )
        fatura_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "FATURA_UUID",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        fatura_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "FATURA_ID",
                "type": "Element",
                "namespace": "",
            }
        )
        earsiv_cancel_email: Optional[str] = field(
            default=None,
            metadata={
                "name": "EARSIV_CANCEL_EMAIL",
                "type": "Element",
                "namespace": "",
            }
        )
        delete_flag: Optional[str] = field(
            default=None,
            metadata={
                "name": "DELETE_FLAG",
                "type": "Element",
                "namespace": "",
            }
        )
        iptal_tarihi: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "IPTAL_TARIHI",
                "type": "Element",
                "namespace": "",
            }
        )
        toplam_tutar: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "TOPLAM_TUTAR",
                "type": "Element",
                "namespace": "",
            }
        )
        invoice_content: Optional[Base64Binary] = field(
            default=None,
            metadata={
                "name": "INVOICE_CONTENT",
                "type": "Element",
                "namespace": "",
            }
        )
        iptal_notu: Optional[str] = field(
            default=None,
            metadata={
                "name": "IPTAL_NOTU",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class CancelEarchiveInvoiceResponse:
    class Meta:
        name = "CancelEArchiveInvoiceResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class CancelEdefterRequest:
    class Meta:
        name = "CancelEDefterRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cancel_edefter_content: List["CancelEdefterRequest.CancelEdefterContent"] = field(
        default_factory=list,
        metadata={
            "name": "CancelEDefterContent",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class CancelEdefterContent:
        vkn: Optional[str] = field(
            default=None,
            metadata={
                "name": "VKN",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        donem: Optional[str] = field(
            default=None,
            metadata={
                "name": "DONEM",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )


@dataclass
class CancelEdefterResponse:
    class Meta:
        name = "CancelEDefterResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class Earchiveinv:
    class Meta:
        name = "EARCHIVEINV"

    header: Optional["Earchiveinv.Header"] = field(
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

    @dataclass
    class Header:
        invoice_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_ID",
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
        sender_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER_NAME",
                "type": "Element",
                "namespace": "",
            }
        )
        sender_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDER_IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        customer_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "CUSTOMER_NAME",
                "type": "Element",
                "namespace": "",
            }
        )
        customer_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "CUSTOMER_IDENTIFIER",
                "type": "Element",
                "namespace": "",
            }
        )
        profile_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "PROFILE_ID",
                "type": "Element",
                "namespace": "",
            }
        )
        invoice_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "INVOICE_TYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        earchive_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "EARCHIVE_TYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        sending_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "SENDING_TYPE",
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
        issue_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISSUE_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        payable_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "PAYABLE_AMOUNT",
                "type": "Element",
                "namespace": "",
            }
        )
        taxable_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "TAXABLE_AMOUNT",
                "type": "Element",
                "namespace": "",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CURRENCY_CODE",
                "type": "Element",
                "namespace": "",
            }
        )
        reported: Optional[str] = field(
            default=None,
            metadata={
                "name": "REPORTED",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class EarsivProperties:
    class Meta:
        name = "EARSIV_PROPERTIES"

    earsiv_type: Optional[EarsivTypeValue] = field(
        default=None,
        metadata={
            "name": "EARSIV_TYPE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    earsiv_email_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "EARSIV_EMAIL_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    earsiv_email: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EARSIV_EMAIL",
            "type": "Element",
            "namespace": "",
        }
    )
    sub_status: Optional[SubStatusValue] = field(
        default=None,
        metadata={
            "name": "SUB_STATUS",
            "type": "Element",
            "namespace": "",
        }
    )
    arch_invoice_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ARCH_INVOICE_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    seri: Optional[str] = field(
        default=None,
        metadata={
            "name": "SERI",
            "type": "Element",
            "namespace": "",
        }
    )
    earchive_test_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "EARCHIVE_TEST_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    earsiv_sms_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "EARSIV_SMS_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    sms_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SMS_PHONE_NUMBER",
            "type": "Element",
            "namespace": "",
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
    xslt_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "XSLT_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    ecommerce_upload: Optional[EcommerceUpload] = field(
        default=None,
        metadata={
            "name": "ECOMMERCE_UPLOAD",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class EarchiveInvoiceCountRequest:
    class Meta:
        name = "EArchiveInvoiceCountRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
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


@dataclass
class EarchiveInvoiceCountResponse:
    class Meta:
        name = "EArchiveInvoiceCountResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GenericContent:
    class Meta:
        name = "GENERIC_CONTENT"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FILE_NAME",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    par_index1: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX1",
            "type": "Element",
            "namespace": "",
        }
    )
    par_index2: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX2",
            "type": "Element",
            "namespace": "",
        }
    )
    par_index3: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX3",
            "type": "Element",
            "namespace": "",
        }
    )
    par_index4: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX4",
            "type": "Element",
            "namespace": "",
        }
    )
    par_index5: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX5",
            "type": "Element",
            "namespace": "",
        }
    )
    par_index6: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAR_INDEX6",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par1: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR1",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par2: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR2",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par3: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR3",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par4: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR4",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par5: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR5",
            "type": "Element",
            "namespace": "",
        }
    )
    fix_par6: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIX_PAR6",
            "type": "Element",
            "namespace": "",
        }
    )
    date_index1: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DATE_INDEX1",
            "type": "Element",
            "namespace": "",
        }
    )
    date_index2: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DATE_INDEX2",
            "type": "Element",
            "namespace": "",
        }
    )
    date_index3: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DATE_INDEX3",
            "type": "Element",
            "namespace": "",
        }
    )
    archive_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ARCHIVE_TYPE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    archive_sub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ARCHIVE_SUB_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FILE_TYPE",
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
    parse_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "PARSE_FLAG",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    override: Optional[str] = field(
        default=None,
        metadata={
            "name": "OVERRIDE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    content: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "CONTENT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class GenericReadRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    document: List["GenericReadRequest.Document"] = field(
        default_factory=list,
        metadata={
            "name": "DOCUMENT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Document:
        donem: Optional[str] = field(
            default=None,
            metadata={
                "name": "DONEM",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        doc_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "DOC_NAME",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        doc_type: Optional[DocType] = field(
            default=None,
            metadata={
                "name": "DOC_TYPE",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        sube_no: Optional[str] = field(
            default=None,
            metadata={
                "name": "SUBE_NO",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class GenericReadResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    gen_archive_doc: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "GEN_ARCHIVE_DOC",
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
class GetEarchiveInvoiceListRequest:
    class Meta:
        name = "GetEArchiveInvoiceListRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
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
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "START_DATE",
            "type": "Element",
            "namespace": "",
        }
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "END_DATE",
            "type": "Element",
            "namespace": "",
        }
    )
    period: Optional[str] = field(
        default=None,
        metadata={
            "name": "PERIOD",
            "type": "Element",
            "namespace": "",
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "PREFIX",
            "type": "Element",
            "namespace": "",
        }
    )
    report_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "REPORT_ID ",
            "type": "Element",
            "namespace": "",
        }
    )
    report_included: Optional[bool] = field(
        default=None,
        metadata={
            "name": "REPORT_INCLUDED",
            "type": "Element",
            "namespace": "",
        }
    )
    report_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_FLAG",
            "type": "Element",
            "namespace": "",
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
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CONTENT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    read_included: Optional[str] = field(
        default=None,
        metadata={
            "name": "READ_INCLUDED",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetEarchiveInvoiceRequest:
    class Meta:
        name = "GetEArchiveInvoiceRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    web_validation_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "WEB_VALIDATION_KEY",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GetEarchiveInvoiceResponse:
    class Meta:
        name = "GetEArchiveInvoiceResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    invoice: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
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
class GetEarchiveInvoiceStatusRequest:
    class Meta:
        name = "GetEArchiveInvoiceStatusRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    uuid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 500,
        }
    )


@dataclass
class GetEarchiveInvoiceStatusResponse:
    class Meta:
        name = "GetEArchiveInvoiceStatusResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    invoice: List[EarchiveInvoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "max_occurs": 500,
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
class GetEarchiveReportRequest:
    class Meta:
        name = "GetEArchiveReportRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    report_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_PERIOD",
            "type": "Element",
            "namespace": "",
        }
    )
    report_status_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPORT_STATUS_FLAG",
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


@dataclass
class GetEarchiveReportResponse:
    class Meta:
        name = "GetEArchiveReportResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    report: List[Report] = field(
        default_factory=list,
        metadata={
            "name": "REPORT",
            "type": "Element",
            "namespace": "",
        }
    )
    invoice: List[ReportInvoice] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
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
class GetEledgerStatusRequest:
    class Meta:
        name = "GetELedgerStatusRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    period: Optional[str] = field(
        default=None,
        metadata={
            "name": "PERIOD",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    part_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "PART_NO",
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


@dataclass
class GetEledgerStatusResponse:
    class Meta:
        name = "GetELedgerStatusResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    eledger: List["GetEledgerStatusResponse.Eledger"] = field(
        default_factory=list,
        metadata={
            "name": "ELEDGER",
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
    class Eledger:
        part_no: Optional[str] = field(
            default=None,
            metadata={
                "name": "PART_NO",
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
        period: Optional[str] = field(
            default=None,
            metadata={
                "name": "PERIOD",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_archive_consent: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_ARCHIVE_CONSENT",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_archive_consent_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "GIB_ARCHIVE_CONSENT_DATE",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_archive_status: Optional[int] = field(
            default=None,
            metadata={
                "name": "GIB_ARCHIVE_STATUS",
                "type": "Element",
                "namespace": "",
            }
        )
        gib_archive_status_desc: Optional[str] = field(
            default=None,
            metadata={
                "name": "GIB_ARCHIVE_STATUS_DESC",
                "type": "Element",
                "namespace": "",
            }
        )
        eledger_detail: List["GetEledgerStatusResponse.Eledger.EledgerDetail"] = field(
            default_factory=list,
            metadata={
                "name": "ELEDGER_DETAIL",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class EledgerDetail:
            unique_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UNIQUE_ID",
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
            gib_archive_date: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "GIB_ARCHIVE_DATE",
                    "type": "Element",
                    "namespace": "",
                }
            )
            gib_archive_status_desc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "GIB_ARCHIVE_STATUS_DESC",
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class GetEmailEarchiveInvoiceRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fatura_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "FATURA_UUID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fatura_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FATURA_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMAIL",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetEmailEarchiveInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    gen_archive_doc: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "GEN_ARCHIVE_DOC",
            "type": "Element",
            "namespace": "",
            "required": True,
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
class GetGenericArchiveByPeriodRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    donem: Optional[str] = field(
        default=None,
        metadata={
            "name": "DONEM",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "VKN",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GetGenericArchiveByPeriodResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    gen_archive_doc: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "GEN_ARCHIVE_DOC",
            "type": "Element",
            "namespace": "",
            "required": True,
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
class GetGenericArchiveStatusRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    donem: Optional[str] = field(
        default=None,
        metadata={
            "name": "DONEM",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    donem_parca_sayisi: Optional[str] = field(
        default=None,
        metadata={
            "name": "DONEM_PARCA_SAYISI",
            "type": "Element",
            "namespace": "",
        }
    )
    donem_parca_kodu: Optional[str] = field(
        default=None,
        metadata={
            "name": "DONEM_PARCA_KODU",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetGenericArchiveStatusResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    gen_archive_doc: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "GEN_ARCHIVE_DOC",
            "type": "Element",
            "namespace": "",
            "required": True,
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
class MarkEarchiveInvoiceResponse:
    class Meta:
        name = "MarkEArchiveInvoiceResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
class Oiboperation:
    class Meta:
        name = "OIBOperation"

    request_fault_response: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "RequestFaultResponse",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class PdfProperties:
    class Meta:
        name = "PDF_PROPERTIES"

    earsiv_pdf_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "EARSIV_PDF_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    pdf_signature_flag: Optional[FlagValue] = field(
        default=None,
        metadata={
            "name": "PDF_SIGNATURE_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    pdf_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PDF_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    earchive_pdf_xslt_filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "EARCHIVE_PDF_XSLT_FILENAME",
            "type": "Element",
            "namespace": "",
        }
    )
    pdf_content: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "PDF_CONTENT",
            "type": "Element",
            "namespace": "",
        }
    )
    earchive_pdf_visualsign_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "EARCHIVE_PDF_VISUALSIGN_FILE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ReadEarchiveReportRequest:
    class Meta:
        name = "ReadEArchiveReportRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rapor_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "RAPOR_NO",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ReadEarchiveReportResponse:
    class Meta:
        name = "ReadEArchiveReportResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    earchivereport: List[Base64Binary] = field(
        default_factory=list,
        metadata={
            "name": "EARCHIVEREPORT",
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
class RequestFaultType:
    request_fault_response: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "RequestFaultResponse",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SendSmsEarchiveInvoiceRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fatura_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "FATURA_UUID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    telefon_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TELEFON_NO",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SendSmsEarchiveInvoiceResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    gen_archive_doc: Optional[Base64Binary] = field(
        default=None,
        metadata={
            "name": "GEN_ARCHIVE_DOC",
            "type": "Element",
            "namespace": "",
            "required": True,
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
class ArchiveGenericDocumentRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    generic_content: List[GenericContent] = field(
        default_factory=list,
        metadata={
            "name": "GENERIC_CONTENT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ArchiveInvoiceExtendedContent:
    invoice_properties: List["ArchiveInvoiceExtendedContent.InvoiceProperties"] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE_PROPERTIES",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InvoiceProperties:
        earsiv_flag: FlagValue = field(
            default=FlagValue.N,
            metadata={
                "name": "EARSIV_FLAG",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        earsiv_properties: Optional[EarsivProperties] = field(
            default=None,
            metadata={
                "name": "EARSIV_PROPERTIES",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        pdf_properties: Optional[PdfProperties] = field(
            default=None,
            metadata={
                "name": "PDF_PROPERTIES",
                "type": "Element",
                "namespace": "",
            }
        )
        archive_note: Optional[str] = field(
            default=None,
            metadata={
                "name": "ARCHIVE_NOTE",
                "type": "Element",
                "namespace": "",
            }
        )
        invoice_content: Optional[Base64Binary] = field(
            default=None,
            metadata={
                "name": "INVOICE_CONTENT",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )


@dataclass
class ArchiveInvoiceWriteRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    archive_invoice_write_content: Optional[ArchiveInvoiceWriteContent] = field(
        default=None,
        metadata={
            "name": "ArchiveInvoiceWriteContent",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GetEarchiveInvoiceListResponse:
    class Meta:
        name = "GetEArchiveInvoiceListResponse"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

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
    invoice: List[Earchiveinv] = field(
        default_factory=list,
        metadata={
            "name": "INVOICE",
            "type": "Element",
            "namespace": "",
            "max_occurs": 10000,
        }
    )


@dataclass
class MarkEarchiveInvoiceRequest:
    class Meta:
        name = "MarkEArchiveInvoiceRequest"
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mark: Optional["MarkEarchiveInvoiceRequest.Mark"] = field(
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
        earchive_invoice: List[Earchiveinv] = field(
            default_factory=list,
            metadata={
                "name": "EARCHIVE_INVOICE",
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
class RequestFault(RequestFaultType):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"


@dataclass
class ArchiveInvoiceExtendedRequest:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl/archive"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    archive_invoice_extended_content: Optional[ArchiveInvoiceExtendedContent] = field(
        default=None,
        metadata={
            "name": "ArchiveInvoiceExtendedContent",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
