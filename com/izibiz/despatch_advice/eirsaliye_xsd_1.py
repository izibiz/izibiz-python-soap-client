from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2005/05/xmlmime"


@dataclass
class Base64Binary:
    class Meta:
        name = "base64Binary"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2005/05/xmlmime",
        }
    )


@dataclass
class HexBinary:
    class Meta:
        name = "hexBinary"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2005/05/xmlmime",
        }
    )
