from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://schemas.i2i.com/ei/common"


@dataclass
class Attributestype:
    class Meta:
        name = "ATTRIBUTESTYPE"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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


@dataclass
class LovValuetype:
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
    alias: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALIAS",
            "type": "Attribute",
        }
    )
