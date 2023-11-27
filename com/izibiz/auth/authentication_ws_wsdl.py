from dataclasses import dataclass, field
from typing import Optional
from com.izibiz.auth.authentication_ws_xsd_2 import (
    CheckUserRequest,
    CheckUserResponse,
    GetAccountRequest,
    GetAccountResponse,
    GetGibUserListRequest,
    GetGibUserListResponse,
    GetUserAuthorizationRequest,
    GetUserAuthorizationResponse,
    LoginRequest,
    LoginResponse,
    LogoutRequest,
    LogoutResponse,
    RequestFault,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class AuthenticationServicePortCheckUserInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortCheckUserInput.Body"] = field(
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
class AuthenticationServicePortCheckUserOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortCheckUserOutput.Body"] = field(
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
        fault: Optional["AuthenticationServicePortCheckUserOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortCheckUserOutput.Body.Fault.Detail"] = field(
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
class AuthenticationServicePortGetAccountInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetAccountInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_account_request: Optional[GetAccountRequest] = field(
            default=None,
            metadata={
                "name": "GetAccountRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class AuthenticationServicePortGetAccountOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetAccountOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_account_response: Optional[GetAccountResponse] = field(
            default=None,
            metadata={
                "name": "GetAccountResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["AuthenticationServicePortGetAccountOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortGetAccountOutput.Body.Fault.Detail"] = field(
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
class AuthenticationServicePortGetGibUserListInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetGibUserListInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_gib_user_list_request: Optional[GetGibUserListRequest] = field(
            default=None,
            metadata={
                "name": "GetGibUserListRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class AuthenticationServicePortGetGibUserListOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetGibUserListOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_gib_user_list_response: Optional[GetGibUserListResponse] = field(
            default=None,
            metadata={
                "name": "GetGibUserListResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["AuthenticationServicePortGetGibUserListOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortGetGibUserListOutput.Body.Fault.Detail"] = field(
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
class AuthenticationServicePortGetUserAuthorizationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetUserAuthorizationInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_authorization_request: Optional[GetUserAuthorizationRequest] = field(
            default=None,
            metadata={
                "name": "GetUserAuthorizationRequest",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )


@dataclass
class AuthenticationServicePortGetUserAuthorizationOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortGetUserAuthorizationOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_user_authorization_response: Optional[GetUserAuthorizationResponse] = field(
            default=None,
            metadata={
                "name": "GetUserAuthorizationResponse",
                "type": "Element",
                "namespace": "http://schemas.i2i.com/ei/wsdl",
            }
        )
        fault: Optional["AuthenticationServicePortGetUserAuthorizationOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortGetUserAuthorizationOutput.Body.Fault.Detail"] = field(
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
class AuthenticationServicePortLoginInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortLoginInput.Body"] = field(
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
class AuthenticationServicePortLoginOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortLoginOutput.Body"] = field(
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
        fault: Optional["AuthenticationServicePortLoginOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortLoginOutput.Body.Fault.Detail"] = field(
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
class AuthenticationServicePortLogoutInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortLogoutInput.Body"] = field(
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
class AuthenticationServicePortLogoutOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AuthenticationServicePortLogoutOutput.Body"] = field(
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
        fault: Optional["AuthenticationServicePortLogoutOutput.Body.Fault"] = field(
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
            detail: Optional["AuthenticationServicePortLogoutOutput.Body.Fault.Detail"] = field(
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


class AuthenticationServicePortCheckUser:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortCheckUserInput
    output = AuthenticationServicePortCheckUserOutput


class AuthenticationServicePortGetAccount:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortGetAccountInput
    output = AuthenticationServicePortGetAccountOutput


class AuthenticationServicePortGetGibUserList:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortGetGibUserListInput
    output = AuthenticationServicePortGetGibUserListOutput


class AuthenticationServicePortGetUserAuthorization:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortGetUserAuthorizationInput
    output = AuthenticationServicePortGetUserAuthorizationOutput


class AuthenticationServicePortLogin:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortLoginInput
    output = AuthenticationServicePortLoginOutput


class AuthenticationServicePortLogout:
    uri = "#AuthenticationPortBinding_MTOM_Policy"
    style = "document"
    location = "https://efaturatest.izibiz.com.tr/AuthenticationWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = AuthenticationServicePortLogoutInput
    output = AuthenticationServicePortLogoutOutput
