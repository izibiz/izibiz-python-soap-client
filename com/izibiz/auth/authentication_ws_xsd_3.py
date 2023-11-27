from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from com.izibiz.auth.authentication_ws_xsd_4 import (
    Attributestype,
    ChangeInfotype,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/entity"


@dataclass
class RequestErrortype:
    class Meta:
        name = "REQUEST_ERRORType"

    intl_txn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "INTL_TXN_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    client_txn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CLIENT_TXN_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    error_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "ERROR_CODE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    error_short_des: Optional[str] = field(
        default=None,
        metadata={
            "name": "ERROR_SHORT_DES",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    error_long_des: Optional[str] = field(
        default=None,
        metadata={
            "name": "ERROR_LONG_DES",
            "type": "Element",
            "namespace": "",
        }
    )
    stacktrace: Optional[str] = field(
        default=None,
        metadata={
            "name": "STACKTRACE",
            "type": "Element",
            "namespace": "",
        }
    )
    error_element_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ERROR_ELEMENT_INDEX",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RequestReturntype:
    class Meta:
        name = "REQUEST_RETURNType"

    intl_txn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "INTL_TXN_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    client_txn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CLIENT_TXN_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    return_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "RETURN_CODE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    warnings: List[str] = field(
        default_factory=list,
        metadata={
            "name": "WARNINGS",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RequestHeadertype:
    class Meta:
        name = "REQUEST_HEADERType"

    session_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SESSION_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    client_txn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CLIENT_TXN_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    intl_txn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "INTL_TXN_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    intl_parent_txn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "INTL_PARENT_TXN_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    action_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ACTION_DATE",
            "type": "Element",
            "namespace": "",
        }
    )
    change_info: Optional[ChangeInfotype] = field(
        default=None,
        metadata={
            "name": "CHANGE_INFO",
            "type": "Element",
            "namespace": "",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "REASON",
            "type": "Element",
            "namespace": "",
        }
    )
    application_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "APPLICATION_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    hostname: Optional[str] = field(
        default=None,
        metadata={
            "name": "HOSTNAME",
            "type": "Element",
            "namespace": "",
        }
    )
    channel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHANNEL_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    simulation_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "SIMULATION_FLAG",
            "type": "Element",
            "namespace": "",
        }
    )
    compressed: Optional[str] = field(
        default=None,
        metadata={
            "name": "COMPRESSED",
            "type": "Element",
            "namespace": "",
        }
    )
    attributes: List[Attributestype] = field(
        default_factory=list,
        metadata={
            "name": "ATTRIBUTES",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Request:
    class Meta:
        name = "REQUEST"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class RequestInfotype:
    class Meta:
        name = "REQUEST_INFOType"

    request_header: Optional[RequestHeadertype] = field(
        default=None,
        metadata={
            "name": "REQUEST_HEADER",
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
    request_error: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "REQUEST_ERROR",
            "type": "Element",
            "namespace": "",
        }
    )
