from dataclasses import dataclass, field
from typing import Optional
from com.izibiz.invoice.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_4 import (
    ArchiveInvoiceRequest,
    ArchiveInvoiceResponse,
    CancelDraftInvoiceRequest,
    CancelDraftInvoiceResponse,
    CheckUserRequest,
    CheckUserResponse,
    GetEnvelopeRequest,
    GetEnvelopeResponse,
    GetEnvelopeStatusRequest,
    GetEnvelopeStatusResponse,
    GetInvoiceCountRequest,
    GetInvoiceCountResponse,
    GetInvoiceRequest,
    GetInvoiceResponse,
    GetInvoiceStatusAllRequest,
    GetInvoiceStatusAllResponse,
    GetInvoiceStatusRequest,
    GetInvoiceStatusResponse,
    GetInvoiceWithTypeRequest,
    GetInvoiceWithTypeResponse,
    GetUserListBinaryRequest,
    GetUserListBinaryResponse,
    GetUserListRequest,
    GetUserListResponse,
    LoadInvoiceRequest,
    LoadInvoiceResponse,
    LoginRequest,
    LoginResponse,
    LogoutRequest,
    LogoutResponse,
    MarkEnvelopeRequest,
    MarkEnvelopeResponse,
    MarkInvoiceRequest,
    MarkInvoiceResponse,
    PrepareInvoiceResponseRequest,
    PrepareInvoiceResponseResponse,
    RequestFault,
    SendInvoiceRequest,
    SendInvoiceResponse,
    SendInvoiceResponseRequest,
    SendInvoiceResponseResponse,
    SendInvoiceResponseWithServerSignRequest,
    SendInvoiceResponseWithServerSignResponse,
)


@dataclass
class GetAppRespRequestType:
    class Meta:
        name = "getAppRespRequestType"
        target_namespace = "http://gib.gov.tr/vedop3/eFatura"

    instance_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "instanceIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetAppRespResponseType:
    class Meta:
        name = "getAppRespResponseType"
        target_namespace = "http://gib.gov.tr/vedop3/eFatura"

    application_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationResponse",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetAppRespRequest(GetAppRespRequestType):
    class Meta:
        name = "getAppRespRequest"
        namespace = "http://gib.gov.tr/vedop3/eFatura"


@dataclass
class GetAppRespResponse(GetAppRespResponseType):
    class Meta:
        name = "getAppRespResponse"
        namespace = "http://gib.gov.tr/vedop3/eFatura"


@dataclass
class EinvoiceWsportArchiveInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportArchiveInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_request: Optional[ArchiveInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportArchiveInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportArchiveInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        archive_invoice_response: Optional[ArchiveInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "ArchiveInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportArchiveInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportArchiveInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportCancelDraftInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportCancelDraftInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_draft_invoice_request: Optional[CancelDraftInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "CancelDraftInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportCancelDraftInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportCancelDraftInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancel_draft_invoice_response: Optional[CancelDraftInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "CancelDraftInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportCancelDraftInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportCancelDraftInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportCheckUserInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportCheckUserInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        check_user_request: Optional[CheckUserRequest] = field(
            default=None,
            metadata={
                "name": "CheckUserRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportCheckUserOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportCheckUserOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        check_user_response: Optional[CheckUserResponse] = field(
            default=None,
            metadata={
                "name": "CheckUserResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportCheckUserOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportCheckUserOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetEnvelopeStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetEnvelopeStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_envelope_status_request: Optional[GetEnvelopeStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetEnvelopeStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetEnvelopeStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetEnvelopeStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_envelope_status_response: Optional[GetEnvelopeStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetEnvelopeStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetEnvelopeStatusOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetEnvelopeStatusOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetEnvelopeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetEnvelopeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_envelope_request: Optional[GetEnvelopeRequest] = field(
            default=None,
            metadata={
                "name": "GetEnvelopeRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetEnvelopeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetEnvelopeOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_envelope_response: Optional[GetEnvelopeResponse] = field(
            default=None,
            metadata={
                "name": "GetEnvelopeResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetEnvelopeOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetEnvelopeOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetInvoiceCountInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceCountInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_count_request: Optional[GetInvoiceCountRequest] = field(
            default=None,
            metadata={
                "name": "GetInvoiceCountRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetInvoiceCountOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceCountOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_count_response: Optional[GetInvoiceCountResponse] = field(
            default=None,
            metadata={
                "name": "GetInvoiceCountResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetInvoiceCountOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetInvoiceCountOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetInvoiceStatusAllInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceStatusAllInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_status_all_request: Optional[GetInvoiceStatusAllRequest] = field(
            default=None,
            metadata={
                "name": "GetInvoiceStatusAllRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetInvoiceStatusAllOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceStatusAllOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_status_all_response: Optional[GetInvoiceStatusAllResponse] = field(
            default=None,
            metadata={
                "name": "GetInvoiceStatusAllResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetInvoiceStatusAllOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetInvoiceStatusAllOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetInvoiceStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_status_request: Optional[GetInvoiceStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetInvoiceStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetInvoiceStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_status_response: Optional[GetInvoiceStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetInvoiceStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetInvoiceStatusOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetInvoiceStatusOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetInvoiceWithTypeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceWithTypeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_with_type_request: Optional[GetInvoiceWithTypeRequest] = field(
            default=None,
            metadata={
                "name": "GetInvoiceWithTypeRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetInvoiceWithTypeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceWithTypeOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_with_type_response: Optional[GetInvoiceWithTypeResponse] = field(
            default=None,
            metadata={
                "name": "GetInvoiceWithTypeResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetInvoiceWithTypeOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetInvoiceWithTypeOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_request: Optional[GetInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "GetInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_invoice_response: Optional[GetInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "GetInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetUserListBinaryInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetUserListBinaryInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_list_binary_request: Optional[GetUserListBinaryRequest] = field(
            default=None,
            metadata={
                "name": "GetUserListBinaryRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetUserListBinaryOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetUserListBinaryOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_list_binary_response: Optional[GetUserListBinaryResponse] = field(
            default=None,
            metadata={
                "name": "GetUserListBinaryResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetUserListBinaryOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetUserListBinaryOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportGetUserListInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetUserListInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_list_request: Optional[GetUserListRequest] = field(
            default=None,
            metadata={
                "name": "GetUserListRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportGetUserListOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetUserListOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_list_response: Optional[GetUserListResponse] = field(
            default=None,
            metadata={
                "name": "GetUserListResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportGetUserListOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetUserListOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportLoadInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLoadInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_invoice_request: Optional[LoadInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "LoadInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportLoadInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLoadInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_invoice_response: Optional[LoadInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "LoadInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportLoadInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportLoadInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportLoginInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLoginInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        login_request: Optional[LoginRequest] = field(
            default=None,
            metadata={
                "name": "LoginRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportLoginOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLoginOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        login_response: Optional[LoginResponse] = field(
            default=None,
            metadata={
                "name": "LoginResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportLoginOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportLoginOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportLogoutInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLogoutInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        logout_request: Optional[LogoutRequest] = field(
            default=None,
            metadata={
                "name": "LogoutRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportLogoutOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportLogoutOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        logout_response: Optional[LogoutResponse] = field(
            default=None,
            metadata={
                "name": "LogoutResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportLogoutOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportLogoutOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportMarkEnvelopeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportMarkEnvelopeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_envelope_request: Optional[MarkEnvelopeRequest] = field(
            default=None,
            metadata={
                "name": "MarkEnvelopeRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportMarkEnvelopeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportMarkEnvelopeOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_envelope_response: Optional[MarkEnvelopeResponse] = field(
            default=None,
            metadata={
                "name": "MarkEnvelopeResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportMarkEnvelopeOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportMarkEnvelopeOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportMarkInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportMarkInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_invoice_request: Optional[MarkInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "MarkInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportMarkInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportMarkInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_invoice_response: Optional[MarkInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "MarkInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportMarkInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportMarkInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportPrepareInvoiceResponseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportPrepareInvoiceResponseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        prepare_invoice_response_request: Optional[PrepareInvoiceResponseRequest] = field(
            default=None,
            metadata={
                "name": "PrepareInvoiceResponseRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportPrepareInvoiceResponseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportPrepareInvoiceResponseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        prepare_invoice_response_response: Optional[PrepareInvoiceResponseResponse] = field(
            default=None,
            metadata={
                "name": "PrepareInvoiceResponseResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportPrepareInvoiceResponseOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportPrepareInvoiceResponseOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportSendInvoiceResponseWithServerSignInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceResponseWithServerSignInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_response_with_server_sign_request: Optional[SendInvoiceResponseWithServerSignRequest] = field(
            default=None,
            metadata={
                "name": "SendInvoiceResponseWithServerSignRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportSendInvoiceResponseWithServerSignOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceResponseWithServerSignOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_response_with_server_sign_response: Optional[SendInvoiceResponseWithServerSignResponse] = field(
            default=None,
            metadata={
                "name": "SendInvoiceResponseWithServerSignResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportSendInvoiceResponseWithServerSignOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportSendInvoiceResponseWithServerSignOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportSendInvoiceResponseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceResponseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_response_request: Optional[SendInvoiceResponseRequest] = field(
            default=None,
            metadata={
                "name": "SendInvoiceResponseRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportSendInvoiceResponseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceResponseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_response_response: Optional[SendInvoiceResponseResponse] = field(
            default=None,
            metadata={
                "name": "SendInvoiceResponseResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportSendInvoiceResponseOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportSendInvoiceResponseOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


@dataclass
class EinvoiceWsportSendInvoiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_request: Optional[SendInvoiceRequest] = field(
            default=None,
            metadata={
                "name": "SendInvoiceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EinvoiceWsportSendInvoiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportSendInvoiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_invoice_response: Optional[SendInvoiceResponse] = field(
            default=None,
            metadata={
                "name": "SendInvoiceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EinvoiceWsportSendInvoiceOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportSendInvoiceOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


class EinvoiceWsportArchiveInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportArchiveInvoiceInput
    output = EinvoiceWsportArchiveInvoiceOutput


class EinvoiceWsportCancelDraftInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportCancelDraftInvoiceInput
    output = EinvoiceWsportCancelDraftInvoiceOutput


class EinvoiceWsportCheckUser:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportCheckUserInput
    output = EinvoiceWsportCheckUserOutput


class EinvoiceWsportGetEnvelope:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetEnvelopeInput
    output = EinvoiceWsportGetEnvelopeOutput


class EinvoiceWsportGetEnvelopeStatus:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetEnvelopeStatusInput
    output = EinvoiceWsportGetEnvelopeStatusOutput


class EinvoiceWsportGetInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetInvoiceInput
    output = EinvoiceWsportGetInvoiceOutput


class EinvoiceWsportGetInvoiceCount:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetInvoiceCountInput
    output = EinvoiceWsportGetInvoiceCountOutput


class EinvoiceWsportGetInvoiceStatus:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetInvoiceStatusInput
    output = EinvoiceWsportGetInvoiceStatusOutput


class EinvoiceWsportGetInvoiceStatusAll:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetInvoiceStatusAllInput
    output = EinvoiceWsportGetInvoiceStatusAllOutput


class EinvoiceWsportGetInvoiceWithType:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetInvoiceWithTypeInput
    output = EinvoiceWsportGetInvoiceWithTypeOutput


class EinvoiceWsportGetUserList:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetUserListInput
    output = EinvoiceWsportGetUserListOutput


class EinvoiceWsportGetUserListBinary:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetUserListBinaryInput
    output = EinvoiceWsportGetUserListBinaryOutput


class EinvoiceWsportLoadInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportLoadInvoiceInput
    output = EinvoiceWsportLoadInvoiceOutput


class EinvoiceWsportLogin:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportLoginInput
    output = EinvoiceWsportLoginOutput


class EinvoiceWsportLogout:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportLogoutInput
    output = EinvoiceWsportLogoutOutput


class EinvoiceWsportMarkEnvelope:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportMarkEnvelopeInput
    output = EinvoiceWsportMarkEnvelopeOutput


class EinvoiceWsportMarkInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportMarkInvoiceInput
    output = EinvoiceWsportMarkInvoiceOutput


class EinvoiceWsportPrepareInvoiceResponse:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportPrepareInvoiceResponseInput
    output = EinvoiceWsportPrepareInvoiceResponseOutput


class EinvoiceWsportSendInvoice:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportSendInvoiceInput
    output = EinvoiceWsportSendInvoiceOutput


class EinvoiceWsportSendInvoiceResponse:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportSendInvoiceResponseInput
    output = EinvoiceWsportSendInvoiceResponseOutput


class EinvoiceWsportSendInvoiceResponseWithServerSign:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportSendInvoiceResponseWithServerSignInput
    output = EinvoiceWsportSendInvoiceResponseWithServerSignOutput


@dataclass
class EinvoiceWsportGetApplicationResponseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetApplicationResponseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_app_resp_request: Optional[GetAppRespRequest] = field(
            default=None,
            metadata={
                "name": "getAppRespRequest",
                "type": "Element",
                "namespace": "http://gib.gov.tr/vedop3/eFatura",
            }
        )


@dataclass
class EinvoiceWsportGetApplicationResponseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://schemas.i2i.com/ei/wsdl"

    body: Optional["EinvoiceWsportGetApplicationResponseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_app_resp_response: Optional[GetAppRespResponse] = field(
            default=None,
            metadata={
                "name": "getAppRespResponse",
                "type": "Element",
                "namespace": "http://gib.gov.tr/vedop3/eFatura",
            }
        )
        fault: Optional["EinvoiceWsportGetApplicationResponseOutput.Body.Fault"] = field(
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
            detail: Optional["EinvoiceWsportGetApplicationResponseOutput.Body.Fault.Detail"] = field(
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
                        "namespace": "http://schemas.i2i.com/ei/wsdl",
                    }
                )


class EinvoiceWsportGetApplicationResponse:
    style = "document"
    location = "https://efaturatest.izibiz.com.tr:443/EInvoiceWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EinvoiceWsportGetApplicationResponseInput
    output = EinvoiceWsportGetApplicationResponseOutput
