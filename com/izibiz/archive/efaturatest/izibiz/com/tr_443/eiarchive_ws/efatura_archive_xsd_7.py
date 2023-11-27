from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_6 import (
    Attributestype,
    ChangeInfotype,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/entity"


@dataclass
class RequestErrortype:
    """
    This will be fault type.

    :ivar intl_txn_id: Internal TXN ID
    :ivar client_txn_id: Initiating domain Transaction ID of the action
    :ivar error_code: Error Code
    :ivar error_short_des: Error Short Description
    :ivar error_long_des: Error Long Description
    :ivar stacktrace: This is printStackTrace output...
    :ivar error_element_index: In case of multiple requests this is the
        failing element index
    """
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
    """
    Request response related context information including data such as
    RETURN_CODE, DETAILED_RESULT information etc.

    :ivar intl_txn_id: Internal TXN ID
    :ivar client_txn_id: Initiating domain Transaction ID of the action
    :ivar return_code: Numeric return code of the action. 0: success,
        negative: failure, positive: success with warning
    :ivar warnings:
    """
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
    """
    Request related information context including data such as SESSION_ID,
    INTL_TXN_ID etc.

    :ivar session_id: Initiating domain Transaction ID of the action
    :ivar client_txn_id: Initiating domain Transaction ID of the action
    :ivar intl_txn_id: Internal Transaction ID
    :ivar intl_parent_txn_id: Parent Transaction ID
    :ivar action_date: Action Date provided by client system
    :ivar change_info: See CHANGE_INFO type
    :ivar reason: Reason of the Action
    :ivar application_name: Application Name
    :ivar hostname: Initiating host name or IP address
    :ivar channel_name: Initiating domain channel name of the action
    :ivar simulation_flag: A true or yes indicates that the request will
        be executed but not committed
    :ivar compressed: Indicates parent message contains compressed
        content
    :ivar attributes: Attributes array that composed by name-value pairs
        using for information manners.
    :ivar api_key: Request related information external customer key, it
        is not a SESSION_ID
    """
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
    api_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "API_KEY",
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
    """
    Detailed Information about the status of a request.

    :ivar request_header: See REQUEST_HEADER type
    :ivar request_return: See REQUEST_RETURNType
    :ivar request_error: See REQUEST_ERRORType
    """
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
