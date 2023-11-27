from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
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


class FindKeytypeVisibilityType(Enum):
    PERSON = "PERSON"
    POSITION = "POSITION"
    POSITION_TYPE = "POSITION_TYPE"
    PEER = "PEER"
    TEAM = "TEAM"
    ORGANIZATION = "ORGANIZATION"
    ADMIN = "ADMIN"


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
class SearchKeytype:
    """
    Base type used for search keys.

    :ivar valid_from: Valid From
    :ivar valid_to: Valid To
    :ivar rownum_offset: For searches that may return many rows, this
        parameters specifies the starting rownum of query to be returned
        by BACKEND system
    :ivar rownum_limit: For searches that may return many rows, this
        parameters specifies the maximum rownums to be returned starting
        with ROWNUM_OFFSET
    """
    class Meta:
        name = "SEARCH_KEYType"

    valid_from: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VALID_FROM",
            "type": "Element",
            "namespace": "",
        }
    )
    valid_to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VALID_TO",
            "type": "Element",
            "namespace": "",
        }
    )
    rownum_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "ROWNUM_OFFSET",
            "type": "Element",
            "namespace": "",
        }
    )
    rownum_limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "ROWNUM_LIMIT",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SearchResulttype:
    """
    Base type used for all search results.

    :ivar rownum_total: Specifies the total number of rows returned
    """
    class Meta:
        name = "SEARCH_RESULTType"

    rownum_total: Optional[int] = field(
        default=None,
        metadata={
            "name": "ROWNUM_TOTAL",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ValidityPeriodtype:
    """
    Helper Entity; Contains validity period info for related entity.

    :ivar sdate: Validity start date of the entity
    :ivar edate: Validity end date of the entity
    """
    class Meta:
        name = "VALIDITY_PERIODType"

    sdate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SDATE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    edate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EDATE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class EntitybaseType:
    """
    :ivar el_action: Requested Elementary Action:C, R, U or D
    :ivar validity_period: See VALIDITY_PERIOD type
    :ivar change_info: See CHANGE_INFO type
    :ivar access_control_info: See ACCESS_CONTROL_INFO type
    """
    class Meta:
        name = "ENTITYBaseType"

    el_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "EL_ACTION",
            "type": "Element",
            "namespace": "",
            "max_length": 1,
            "pattern": r"[CRUDScruds]",
        }
    )
    validity_period: Optional[ValidityPeriodtype] = field(
        default=None,
        metadata={
            "name": "VALIDITY_PERIOD",
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
    access_control_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "ACCESS_CONTROL_INFO",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class FindKeytype:
    """
    Base type used for search keys.

    :ivar datetime: DateTime of Inquire.
    :ivar visibility_type: Visibility Type
    """
    class Meta:
        name = "FIND_KEYType"

    datetime: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DATETIME",
            "type": "Element",
            "namespace": "",
        }
    )
    visibility_type: Optional[FindKeytypeVisibilityType] = field(
        default=None,
        metadata={
            "name": "VISIBILITY_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class IsoCurrencyCodetype(LovValuetype):
    """
    Helper Entity; Holds LOV Value Type.
    """
    class Meta:
        name = "ISO_CURRENCY_CODEType"


@dataclass
class Amounttype:
    """
    Helper Entity; Contains price type.

    :ivar amount: Charge amount.
    :ivar currency_code: See ISO_CURRENCY_CODE Type
    """
    class Meta:
        name = "AMOUNTType"

    amount: Optional[float] = field(
        default=None,
        metadata={
            "name": "AMOUNT",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    currency_code: Optional[IsoCurrencyCodetype] = field(
        default=None,
        metadata={
            "name": "CURRENCY_CODE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Commenttype(EntitybaseType):
    """
    Holds Comment Info.

    :ivar comment_id: Comment Internal ID. -1 if NOT defined
    :ivar comment: Comment
    :ivar intl_txn_id: INTL TXN ID if related to a Workflow
    """
    class Meta:
        name = "COMMENTType"

    comment_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "COMMENT_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "COMMENT",
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_length": 1024,
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


@dataclass
class Filetype(EntitybaseType):
    """
    Holds File Info.

    :ivar create_user_info:
    :ivar filename: Filename
    :ivar filetype: Defines filetype such as PDF, XSL etc.
    :ivar operation_code: Operation Code
    :ivar content: This is the content of the file
    :ivar intl_txn_id: INTL TXN ID if related to a Workflow
    """
    class Meta:
        name = "FILEType"

    create_user_info: Optional["Filetype.CreateUserInfo"] = field(
        default=None,
        metadata={
            "name": "CREATE_USER_INFO",
            "type": "Element",
            "namespace": "",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "FILENAME",
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_length": 256,
        }
    )
    filetype: Optional[str] = field(
        default=None,
        metadata={
            "name": "FILETYPE",
            "type": "Element",
            "namespace": "",
            "max_length": 10,
        }
    )
    operation_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "OPERATION_CODE",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 32,
        }
    )
    content: Optional[object] = field(
        default=None,
        metadata={
            "name": "CONTENT",
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

    @dataclass
    class CreateUserInfo:
        """
        :ivar first_name: First name
        :ivar last_name: Last name
        """
        first_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "FIRST_NAME",
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 256,
            }
        )
        last_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "LAST_NAME",
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 64,
            }
        )


@dataclass
class Commentsettype(EntitybaseType):
    """
    Holds Comment Set Info.

    :ivar comment_set_id: Unique ID indicating a set of comments. If not
        defined may be set to -1
    :ivar comment: Comments
    """
    class Meta:
        name = "COMMENTSETType"

    comment_set_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "COMMENT_SET_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    comment: List[Commenttype] = field(
        default_factory=list,
        metadata={
            "name": "COMMENT",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Filesettype(EntitybaseType):
    """
    Holds File Set Info.

    :ivar file_set_id: Unique ID indicating a set of files. If NOT
        defined may be set to -1
    :ivar file: Files
    """
    class Meta:
        name = "FILESETType"

    file_set_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "FILE_SET_ID",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    file: List[Filetype] = field(
        default_factory=list,
        metadata={
            "name": "FILE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Entitytype(EntitybaseType):
    """
    Helper Entity; defines basic properties for a business entity.

    :ivar fileset: See FILESET type
    :ivar commentset: See COMMENTSET type
    """
    class Meta:
        name = "ENTITYType"

    fileset: Optional[Filesettype] = field(
        default=None,
        metadata={
            "name": "FILESET",
            "type": "Element",
            "namespace": "",
        }
    )
    commentset: Optional[Commentsettype] = field(
        default=None,
        metadata={
            "name": "COMMENTSET",
            "type": "Element",
            "namespace": "",
        }
    )
