from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://schemas.i2i.com/ei/common"


@dataclass
class Attributestype:
    """
    A generic name/value Attributes type.
    """
    class Meta:
        name = "ATTRIBUTESTYPE"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )


@dataclass
class AmountType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        }
    )
    currency_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCodeListVersionID",
            "type": "Attribute",
        }
    )


@dataclass
class ChangeInfotype:
    """
    Helper Entity; Contains information related to either Creation or Modification.

    :ivar cdate: Create Date
    :ivar cposition_id: Create Position ID
    :ivar cuser_id: Create User ID
    :ivar udate: Update Date
    :ivar uposition_id: Update Position ID
    :ivar uuser_id: Update User ID
    """
    class Meta:
        name = "CHANGE_INFOType"

    cdate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CDATE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cposition_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CPOSITION_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cuser_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CUSER_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    udate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UDATE",
            "type": "Element",
            "namespace": "",
        }
    )
    uposition_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "UPOSITION_ID",
            "type": "Element",
            "namespace": "",
        }
    )
    uuser_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "UUSER_ID",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Customer:
    class Meta:
        name = "CUSTOMER"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Element",
            "namespace": "",
        }
    )


class FlagValue(Enum):
    Y = "Y"
    N = "N"


@dataclass
class LovValuetype:
    """
    Helper Entity; Holds LOV Value Type.

    :ivar lov_id: Indicates list of value ID
    :ivar lov_code: LOV Internal CODE
    """
    class Meta:
        name = "LOV_VALUEType"

    lov_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LOV_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lov_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LOV_CODE",
            "type": "Element",
            "namespace": "",
            "max_length": 64,
        }
    )


@dataclass
class Partinfo:
    class Meta:
        name = "PARTINFO"

    vkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "VKN",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
        }
    )
