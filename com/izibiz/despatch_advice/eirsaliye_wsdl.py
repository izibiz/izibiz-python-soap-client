from dataclasses import dataclass, field
from typing import Optional
from com.izibiz.despatch_advice.eirsaliye_xsd_2 import (
    GetDespatchAdviceRequest,
    GetDespatchAdviceResponse,
    GetDespatchAdviceStatusRequest,
    GetDespatchAdviceStatusResponse,
    GetDespatchAdviceWithStatusRequest,
    GetDespatchAdviceWithStatusResponse,
    GetReceiptAdviceRequest,
    GetReceiptAdviceResponse,
    GetReceiptAdviceStatusRequest,
    GetReceiptAdviceStatusResponse,
    LoadDespatchAdviceRequest,
    LoadDespatchAdviceResponse,
    LoadReceiptAdviceRequest,
    LoadReceiptAdviceResponse,
    MarkDespatchAdviceRequest,
    MarkDespatchAdviceResponse,
    MarkReceiptAdviceRequest,
    MarkReceiptAdviceResponse,
    RequestFault,
    SendDespatchAdviceRequest,
    SendDespatchAdviceResponse,
    SendDespatchResponseRequest,
    SendDespatchResponseResponse,
    SendReceiptAdviceRequest,
    SendReceiptAdviceResponse,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class EirsaliyeServicePortGetDespatchAdviceStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_status_request: Optional[GetDespatchAdviceStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortGetDespatchAdviceStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_status_response: Optional[GetDespatchAdviceStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortGetDespatchAdviceStatusOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortGetDespatchAdviceStatusOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortGetDespatchAdviceWithStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceWithStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_with_status_request: Optional[GetDespatchAdviceWithStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceWithStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortGetDespatchAdviceWithStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceWithStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_with_status_response: Optional[GetDespatchAdviceWithStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceWithStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortGetDespatchAdviceWithStatusOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortGetDespatchAdviceWithStatusOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortGetDespatchAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_request: Optional[GetDespatchAdviceRequest] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortGetDespatchAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetDespatchAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_despatch_advice_response: Optional[GetDespatchAdviceResponse] = field(
            default=None,
            metadata={
                "name": "GetDespatchAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortGetDespatchAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortGetDespatchAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortGetReceiptAdviceStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetReceiptAdviceStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_receipt_advice_status_request: Optional[GetReceiptAdviceStatusRequest] = field(
            default=None,
            metadata={
                "name": "GetReceiptAdviceStatusRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortGetReceiptAdviceStatusOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetReceiptAdviceStatusOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_receipt_advice_status_response: Optional[GetReceiptAdviceStatusResponse] = field(
            default=None,
            metadata={
                "name": "GetReceiptAdviceStatusResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortGetReceiptAdviceStatusOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortGetReceiptAdviceStatusOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortGetReceiptAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetReceiptAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_receipt_advice_request: Optional[GetReceiptAdviceRequest] = field(
            default=None,
            metadata={
                "name": "GetReceiptAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortGetReceiptAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortGetReceiptAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_receipt_advice_response: Optional[GetReceiptAdviceResponse] = field(
            default=None,
            metadata={
                "name": "GetReceiptAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortGetReceiptAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortGetReceiptAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortLoadDespatchAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortLoadDespatchAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_despatch_advice_request: Optional[LoadDespatchAdviceRequest] = field(
            default=None,
            metadata={
                "name": "LoadDespatchAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortLoadDespatchAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortLoadDespatchAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_despatch_advice_response: Optional[LoadDespatchAdviceResponse] = field(
            default=None,
            metadata={
                "name": "LoadDespatchAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortLoadDespatchAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortLoadDespatchAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortLoadReceiptAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortLoadReceiptAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_receipt_advice_request: Optional[LoadReceiptAdviceRequest] = field(
            default=None,
            metadata={
                "name": "LoadReceiptAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortLoadReceiptAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortLoadReceiptAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        load_receipt_advice_response: Optional[LoadReceiptAdviceResponse] = field(
            default=None,
            metadata={
                "name": "LoadReceiptAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortLoadReceiptAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortLoadReceiptAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortMarkDespatchAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortMarkDespatchAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_despatch_advice_request: Optional[MarkDespatchAdviceRequest] = field(
            default=None,
            metadata={
                "name": "MarkDespatchAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortMarkDespatchAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortMarkDespatchAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_despatch_advice_response: Optional[MarkDespatchAdviceResponse] = field(
            default=None,
            metadata={
                "name": "MarkDespatchAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortMarkDespatchAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortMarkDespatchAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortMarkReceiptAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortMarkReceiptAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_receipt_advice_request: Optional[MarkReceiptAdviceRequest] = field(
            default=None,
            metadata={
                "name": "MarkReceiptAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortMarkReceiptAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortMarkReceiptAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        mark_receipt_advice_response: Optional[MarkReceiptAdviceResponse] = field(
            default=None,
            metadata={
                "name": "MarkReceiptAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortMarkReceiptAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortMarkReceiptAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortSendDespatchAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendDespatchAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_despatch_advice_request: Optional[SendDespatchAdviceRequest] = field(
            default=None,
            metadata={
                "name": "SendDespatchAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortSendDespatchAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendDespatchAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_despatch_advice_response: Optional[SendDespatchAdviceResponse] = field(
            default=None,
            metadata={
                "name": "SendDespatchAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortSendDespatchAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortSendDespatchAdviceOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortSendDespatchResponseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendDespatchResponseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_despatch_response_request: Optional[SendDespatchResponseRequest] = field(
            default=None,
            metadata={
                "name": "SendDespatchResponseRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortSendDespatchResponseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendDespatchResponseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_despatch_response_response: Optional[SendDespatchResponseResponse] = field(
            default=None,
            metadata={
                "name": "SendDespatchResponseResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortSendDespatchResponseOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortSendDespatchResponseOutput.Body.Fault.Detail"] = field(
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
class EirsaliyeServicePortSendReceiptAdviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendReceiptAdviceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_receipt_advice_request: Optional[SendReceiptAdviceRequest] = field(
            default=None,
            metadata={
                "name": "SendReceiptAdviceRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class EirsaliyeServicePortSendReceiptAdviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EirsaliyeServicePortSendReceiptAdviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        send_receipt_advice_response: Optional[SendReceiptAdviceResponse] = field(
            default=None,
            metadata={
                "name": "SendReceiptAdviceResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["EirsaliyeServicePortSendReceiptAdviceOutput.Body.Fault"] = field(
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
            detail: Optional["EirsaliyeServicePortSendReceiptAdviceOutput.Body.Fault.Detail"] = field(
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


class EirsaliyeServicePortGetDespatchAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortGetDespatchAdviceInput
    output = EirsaliyeServicePortGetDespatchAdviceOutput


class EirsaliyeServicePortGetDespatchAdviceStatus:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortGetDespatchAdviceStatusInput
    output = EirsaliyeServicePortGetDespatchAdviceStatusOutput


class EirsaliyeServicePortGetDespatchAdviceWithStatus:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortGetDespatchAdviceWithStatusInput
    output = EirsaliyeServicePortGetDespatchAdviceWithStatusOutput


class EirsaliyeServicePortGetReceiptAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortGetReceiptAdviceInput
    output = EirsaliyeServicePortGetReceiptAdviceOutput


class EirsaliyeServicePortGetReceiptAdviceStatus:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortGetReceiptAdviceStatusInput
    output = EirsaliyeServicePortGetReceiptAdviceStatusOutput


class EirsaliyeServicePortLoadDespatchAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortLoadDespatchAdviceInput
    output = EirsaliyeServicePortLoadDespatchAdviceOutput


class EirsaliyeServicePortLoadReceiptAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortLoadReceiptAdviceInput
    output = EirsaliyeServicePortLoadReceiptAdviceOutput


class EirsaliyeServicePortMarkDespatchAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortMarkDespatchAdviceInput
    output = EirsaliyeServicePortMarkDespatchAdviceOutput


class EirsaliyeServicePortMarkReceiptAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortMarkReceiptAdviceInput
    output = EirsaliyeServicePortMarkReceiptAdviceOutput


class EirsaliyeServicePortSendDespatchAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortSendDespatchAdviceInput
    output = EirsaliyeServicePortSendDespatchAdviceOutput


class EirsaliyeServicePortSendDespatchResponse:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortSendDespatchResponseInput
    output = EirsaliyeServicePortSendDespatchResponseOutput


class EirsaliyeServicePortSendReceiptAdvice:
    uri = "#EIrsaliyeServicePortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = EirsaliyeServicePortSendReceiptAdviceInput
    output = EirsaliyeServicePortSendReceiptAdviceOutput
