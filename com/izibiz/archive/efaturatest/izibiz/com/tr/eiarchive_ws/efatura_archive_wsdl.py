from dataclasses import dataclass, field
from typing import Optional
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_5 import (
    ArchiveGenericDocumentRequest,
    ArchiveGenericDocumentResponse,
    ArchiveGetInvoiceInfoRequest,
    ArchiveGetInvoiceInfoResponse,
    ArchiveInvoiceCopyRequest,
    ArchiveInvoiceCopyResponse,
    ArchiveInvoiceExtendedRequest,
    ArchiveInvoiceExtendedResponse,
    ArchiveInvoiceReadRequest,
    ArchiveInvoiceReadResponse,
    ArchiveInvoiceWriteRequest,
    ArchiveInvoiceWriteResponse,
    CancelEarchiveInvoiceRequest,
    CancelEarchiveInvoiceResponse,
    CancelEdefterRequest,
    CancelEdefterResponse,
    EarchiveInvoiceCountRequest,
    EarchiveInvoiceCountResponse,
    GenericReadRequest,
    GenericReadResponse,
    GetEarchiveInvoiceListRequest,
    GetEarchiveInvoiceListResponse,
    GetEarchiveInvoiceRequest,
    GetEarchiveInvoiceResponse,
    GetEarchiveInvoiceStatusRequest,
    GetEarchiveInvoiceStatusResponse,
    GetEarchiveReportRequest,
    GetEarchiveReportResponse,
    GetEledgerStatusRequest,
    GetEledgerStatusResponse,
    GetEmailEarchiveInvoiceRequest,
    GetEmailEarchiveInvoiceResponse,
    GetGenericArchiveByPeriodRequest,
    GetGenericArchiveByPeriodResponse,
    GetGenericArchiveStatusRequest,
    GetGenericArchiveStatusResponse,
    MarkEarchiveInvoiceRequest,
    MarkEarchiveInvoiceResponse,
    ReadEarchiveReportRequest,
    ReadEarchiveReportResponse,
    RequestFault,
    SendSmsEarchiveInvoiceRequest,
    SendSmsEarchiveInvoiceResponse,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl/archive"


@dataclass
class EfaturaArchivePortArchiveGenericDocumentInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortArchiveGenericDocumentInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_generic_document_request: Optional[ArchiveGenericDocumentRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveGenericDocumentRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortArchiveGenericDocumentOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortArchiveGenericDocumentOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_generic_document_response: Optional[ArchiveGenericDocumentResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveGenericDocumentResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortArchiveGenericDocumentOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortArchiveGenericDocumentOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortArchiveGetInvoiceInfoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortArchiveGetInvoiceInfoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_get_invoice_info_request: Optional[ArchiveGetInvoiceInfoRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveGetInvoiceInfoRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortArchiveGetInvoiceInfoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortArchiveGetInvoiceInfoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_get_invoice_info_response: Optional[ArchiveGetInvoiceInfoResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveGetInvoiceInfoResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortArchiveGetInvoiceInfoOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortArchiveGetInvoiceInfoOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortCancelEarchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCancelEarchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_earchive_invoice_request: Optional[CancelEarchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "CancelEArchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortCancelEarchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCancelEarchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_earchive_invoice_response: Optional[CancelEarchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "CancelEArchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortCancelEarchiveInvoiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortCancelEarchiveInvoiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortCancelEdefterInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCancelEdefterInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_edefter_request: Optional[CancelEdefterRequest] = field(
            default=None,
            metadata={
                "name": "CancelEDefterRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortCancelEdefterOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCancelEdefterOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_edefter_response: Optional[CancelEdefterResponse] = field(
            default=None,
            metadata={
                "name": "CancelEDefterResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortCancelEdefterOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortCancelEdefterOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortCopyToArchiveInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCopyToArchiveInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_copy_request: Optional[ArchiveInvoiceCopyRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceCopyRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortCopyToArchiveOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortCopyToArchiveOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_copy_response: Optional[ArchiveInvoiceCopyResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceCopyResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortCopyToArchiveOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortCopyToArchiveOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortEarchiveInvoiceCountInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortEarchiveInvoiceCountInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        earchive_invoice_count_request: Optional[EarchiveInvoiceCountRequest] = field(
            default=None,
            metadata={
                "name": "EArchiveInvoiceCountRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortEarchiveInvoiceCountOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortEarchiveInvoiceCountOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        earchive_invoice_count_response: Optional[EarchiveInvoiceCountResponse] = field(
            default=None,
            metadata={
                "name": "EArchiveInvoiceCountResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortEarchiveInvoiceCountOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortEarchiveInvoiceCountOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGenericReadInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGenericReadInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        generic_read_request: Optional[GenericReadRequest] = field(
            default=None,
            metadata={
                "name": "GenericReadRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGenericReadOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGenericReadOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        generic_read_response: Optional[GenericReadResponse] = field(
            default=None,
            metadata={
                "name": "GenericReadResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGenericReadOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGenericReadOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceListInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceListInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_list_request: Optional[GetEarchiveInvoiceListRequest] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceListRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceListOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceListOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_list_response: Optional[GetEarchiveInvoiceListResponse] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceListResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEarchiveInvoiceListOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEarchiveInvoiceListOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_status_request: Optional[GetEarchiveInvoiceStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_status_response: Optional[GetEarchiveInvoiceStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEarchiveInvoiceStatusOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEarchiveInvoiceStatusOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_request: Optional[GetEarchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEarchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_invoice_response: Optional[GetEarchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "GetEArchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEarchiveInvoiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEarchiveInvoiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEarchiveReportInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveReportInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_report_request: Optional[GetEarchiveReportRequest] = field(
            default=None,
            metadata={
                "name": "GetEArchiveReportRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEarchiveReportOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEarchiveReportOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_earchive_report_response: Optional[GetEarchiveReportResponse] = field(
            default=None,
            metadata={
                "name": "GetEArchiveReportResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEarchiveReportOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEarchiveReportOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEledgerStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEledgerStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_eledger_status_request: Optional[GetEledgerStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetELedgerStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEledgerStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEledgerStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_eledger_status_response: Optional[GetEledgerStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetELedgerStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEledgerStatusOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEledgerStatusOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetEmailEarchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEmailEarchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_email_earchive_invoice_request: Optional[GetEmailEarchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "GetEmailEarchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetEmailEarchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetEmailEarchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_email_earchive_invoice_response: Optional[GetEmailEarchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "GetEmailEarchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetEmailEarchiveInvoiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetEmailEarchiveInvoiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetGenericArchiveByPeriodInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetGenericArchiveByPeriodInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_generic_archive_by_period_request: Optional[GetGenericArchiveByPeriodRequest] = field(
            default=None,
            metadata={
                "name": "GetGenericArchiveByPeriodRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetGenericArchiveByPeriodOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetGenericArchiveByPeriodOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_generic_archive_by_period_response: Optional[GetGenericArchiveByPeriodResponse] = field(
            default=None,
            metadata={
                "name": "GetGenericArchiveByPeriodResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetGenericArchiveByPeriodOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetGenericArchiveByPeriodOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortGetGenericArchiveStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetGenericArchiveStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_generic_archive_status_request: Optional[GetGenericArchiveStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetGenericArchiveStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortGetGenericArchiveStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortGetGenericArchiveStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_generic_archive_status_response: Optional[GetGenericArchiveStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetGenericArchiveStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortGetGenericArchiveStatusOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortGetGenericArchiveStatusOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortMarkEarchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortMarkEarchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_earchive_invoice_request: Optional[MarkEarchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "MarkEArchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortMarkEarchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortMarkEarchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_earchive_invoice_response: Optional[MarkEarchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "MarkEArchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortMarkEarchiveInvoiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortMarkEarchiveInvoiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortReadEarchiveReportInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortReadEarchiveReportInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        read_earchive_report_request: Optional[ReadEarchiveReportRequest] = field(
            default=None,
            metadata={
                "name": "ReadEArchiveReportRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortReadEarchiveReportOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortReadEarchiveReportOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        read_earchive_report_response: Optional[ReadEarchiveReportResponse] = field(
            default=None,
            metadata={
                "name": "ReadEArchiveReportResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortReadEarchiveReportOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortReadEarchiveReportOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortReadFromArchiveInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortReadFromArchiveInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_read_request: Optional[ArchiveInvoiceReadRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceReadRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortReadFromArchiveOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortReadFromArchiveOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_read_response: Optional[ArchiveInvoiceReadResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceReadResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortReadFromArchiveOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortReadFromArchiveOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortSendSmsEarchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortSendSmsEarchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_sms_earchive_invoice_request: Optional[SendSmsEarchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "SendSmsEarchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortSendSmsEarchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortSendSmsEarchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_sms_earchive_invoice_response: Optional[SendSmsEarchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "SendSmsEarchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortSendSmsEarchiveInvoiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortSendSmsEarchiveInvoiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortWriteToArchiveExtendedInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortWriteToArchiveExtendedInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_extended_request: Optional[ArchiveInvoiceExtendedRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceExtendedRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortWriteToArchiveExtendedOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortWriteToArchiveExtendedOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_extended_response: Optional[ArchiveInvoiceExtendedResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceExtendedResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortWriteToArchiveExtendedOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortWriteToArchiveExtendedOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


@dataclass
class EfaturaArchivePortWriteToArchiveInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortWriteToArchiveInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_write_request: Optional[ArchiveInvoiceWriteRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceWriteRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )


@dataclass
class EfaturaArchivePortWriteToArchiveOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EfaturaArchivePortWriteToArchiveOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_write_response: Optional[ArchiveInvoiceWriteResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceWriteResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
            }
        )
        fault: Optional["EfaturaArchivePortWriteToArchiveOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EfaturaArchivePortWriteToArchiveOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                request_fault: Optional[RequestFault] = field(
                    default=None,
                    metadata={
                        "name": "RequestFault",
                        "type": "Element",
                        "namespace": "http://schemas.i2i.com/ei/wsdl/archive",
                    }
                )


class EfaturaArchivePortArchiveGenericDocument:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortArchiveGenericDocumentInput
    output = EfaturaArchivePortArchiveGenericDocumentOutput


class EfaturaArchivePortArchiveGetInvoiceInfo:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortArchiveGetInvoiceInfoInput
    output = EfaturaArchivePortArchiveGetInvoiceInfoOutput


class EfaturaArchivePortCancelEarchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortCancelEarchiveInvoiceInput
    output = EfaturaArchivePortCancelEarchiveInvoiceOutput


class EfaturaArchivePortCancelEdefter:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortCancelEdefterInput
    output = EfaturaArchivePortCancelEdefterOutput


class EfaturaArchivePortCopyToArchive:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortCopyToArchiveInput
    output = EfaturaArchivePortCopyToArchiveOutput


class EfaturaArchivePortEarchiveInvoiceCount:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortEarchiveInvoiceCountInput
    output = EfaturaArchivePortEarchiveInvoiceCountOutput


class EfaturaArchivePortGenericRead:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGenericReadInput
    output = EfaturaArchivePortGenericReadOutput


class EfaturaArchivePortGetEarchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEarchiveInvoiceInput
    output = EfaturaArchivePortGetEarchiveInvoiceOutput


class EfaturaArchivePortGetEarchiveInvoiceList:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEarchiveInvoiceListInput
    output = EfaturaArchivePortGetEarchiveInvoiceListOutput


class EfaturaArchivePortGetEarchiveInvoiceStatus:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEarchiveInvoiceStatusInput
    output = EfaturaArchivePortGetEarchiveInvoiceStatusOutput


class EfaturaArchivePortGetEarchiveReport:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEarchiveReportInput
    output = EfaturaArchivePortGetEarchiveReportOutput


class EfaturaArchivePortGetEledgerStatus:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEledgerStatusInput
    output = EfaturaArchivePortGetEledgerStatusOutput


class EfaturaArchivePortGetEmailEarchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetEmailEarchiveInvoiceInput
    output = EfaturaArchivePortGetEmailEarchiveInvoiceOutput


class EfaturaArchivePortGetGenericArchiveByPeriod:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetGenericArchiveByPeriodInput
    output = EfaturaArchivePortGetGenericArchiveByPeriodOutput


class EfaturaArchivePortGetGenericArchiveStatus:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortGetGenericArchiveStatusInput
    output = EfaturaArchivePortGetGenericArchiveStatusOutput


class EfaturaArchivePortMarkEarchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortMarkEarchiveInvoiceInput
    output = EfaturaArchivePortMarkEarchiveInvoiceOutput


class EfaturaArchivePortReadEarchiveReport:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortReadEarchiveReportInput
    output = EfaturaArchivePortReadEarchiveReportOutput


class EfaturaArchivePortReadFromArchive:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortReadFromArchiveInput
    output = EfaturaArchivePortReadFromArchiveOutput


class EfaturaArchivePortSendSmsEarchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortSendSmsEarchiveInvoiceInput
    output = EfaturaArchivePortSendSmsEarchiveInvoiceOutput


class EfaturaArchivePortWriteToArchive:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortWriteToArchiveInput
    output = EfaturaArchivePortWriteToArchiveOutput


class EfaturaArchivePortWriteToArchiveExtended:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EIArchiveWS/EFaturaArchive"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EfaturaArchivePortWriteToArchiveExtendedInput
    output = EfaturaArchivePortWriteToArchiveExtendedOutput
