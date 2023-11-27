from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from com.izibiz.auth.authentication_ws_xsd_1 import Base64Binary
from com.izibiz.auth.authentication_ws_xsd_3 import (
    Request,
    RequestErrortype,
    RequestReturntype,
)

__NAMESPACE__ = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class AccountAddress:
    class Meta:
        name = "ACCOUNT_ADDRESS"

    commercial_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "COMMERCIAL_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIRST_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LAST_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    vkn_tckno: Optional[str] = field(
        default=None,
        metadata={
            "name": "VKN_TCKNO",
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
    website: Optional[str] = field(
        default=None,
        metadata={
            "name": "WEBSITE",
            "type": "Element",
            "namespace": "",
        }
    )
    tax_office: Optional[str] = field(
        default=None,
        metadata={
            "name": "TAX_OFFICE",
            "type": "Element",
            "namespace": "",
        }
    )
    sicil_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "SICIL_NO",
            "type": "Element",
            "namespace": "",
        }
    )
    mersis_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "MERSIS_NO",
            "type": "Element",
            "namespace": "",
        }
    )
    isletme_merkezi: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISLETME_MERKEZI",
            "type": "Element",
            "namespace": "",
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "STREET",
            "type": "Element",
            "namespace": "",
        }
    )
    building_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BUILDING_NAME",
            "type": "Element",
            "namespace": "",
        }
    )
    building_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "BUILDING_NO",
            "type": "Element",
            "namespace": "",
        }
    )
    house_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "HOUSE_NO",
            "type": "Element",
            "namespace": "",
        }
    )
    sub_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "SUB_CITY",
            "type": "Element",
            "namespace": "",
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "DISTRICT",
            "type": "Element",
            "namespace": "",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "CITY",
            "type": "Element",
            "namespace": "",
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "REGION",
            "type": "Element",
            "namespace": "",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "COUNTRY",
            "type": "Element",
            "namespace": "",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "POSTAL_CODE",
            "type": "Element",
            "namespace": "",
        }
    )
    telno: Optional[str] = field(
        default=None,
        metadata={
            "name": "TELNO",
            "type": "Element",
            "namespace": "",
        }
    )
    faxno: Optional[str] = field(
        default=None,
        metadata={
            "name": "FAXNO",
            "type": "Element",
            "namespace": "",
        }
    )


class AliasType(Enum):
    ALL = "ALL"
    PK = "PK"
    GB = "GB"


class Authorized(Enum):
    Y = "Y"
    N = "N"


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
    account_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ACCOUNT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    deleted: Optional[str] = field(
        default=None,
        metadata={
            "name": "DELETED",
            "type": "Element",
            "namespace": "",
        }
    )
    alias_deletion_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALIAS_DELETION_TIME",
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


class Product(Enum):
    EINVOICE = "EINVOICE"
    EARCHIVE = "EARCHIVE"
    EDESPATCH = "EDESPATCH"
    CREDITNOTE = "CREDITNOTE"
    RECONCILIATION = "RECONCILIATION"
    CONNECTOR = "CONNECTOR"
    ELEDGER = "ELEDGER"
    ELEDGERARCHIVE = "ELEDGERARCHIVE"
    EINVOICEARCHIVE = "EINVOICEARCHIVE"
    ESMM = "ESMM"


class ProductDetailFlag(Enum):
    Y = "Y"
    N = "N"


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
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOCUMENT_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CheckUserResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    user: List[Gibuser] = field(
        default_factory=list,
        metadata={
            "name": "USER",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetAccountRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class GetAccountResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    error_type: Optional[RequestErrortype] = field(
        default=None,
        metadata={
            "name": "ERROR_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    account_address: Optional[AccountAddress] = field(
        default=None,
        metadata={
            "name": "ACCOUNT_ADDRESS",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetGibUserListRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    type_value: Optional[str] = field(
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
    alias_type: Optional[AliasType] = field(
        default=None,
        metadata={
            "name": "ALIAS_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    alias_modify_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ALIAS_MODIFY_DATE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetGibUserListResponse:
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
class GetUserAuthorizationRequest(Request):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    product: Optional[Product] = field(
        default=None,
        metadata={
            "name": "PRODUCT",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    product_detail_flag: Optional[ProductDetailFlag] = field(
        default=None,
        metadata={
            "name": "PRODUCT_DETAIL_FLAG",
            "type": "Element",
            "namespace": "",
            "required": True,
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
class ProductList:
    class Meta:
        name = "PRODUCT_LIST"

    product: List[Product] = field(
        default_factory=list,
        metadata={
            "name": "PRODUCT",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RequestFault(RequestErrortype):
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"


@dataclass
class GetUserAuthorizationResponse:
    class Meta:
        namespace = "http://schemas.i2i.com/ei/wsdl"

    authorized: Optional[Authorized] = field(
        default=None,
        metadata={
            "name": "AUTHORIZED",
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
    product_list: Optional[ProductList] = field(
        default=None,
        metadata={
            "name": "PRODUCT_LIST",
            "type": "Element",
            "namespace": "",
        }
    )
