from dataclasses import dataclass, field
from typing import Optional
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_1 import (
    CertificateValues,
    RevocationValues,
    XadEstimeStampType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass
class ArchiveTimeStampV2(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass
class ValidationDataType:
    certificate_values: Optional[CertificateValues] = field(
        default=None,
        metadata={
            "name": "CertificateValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    revocation_values: Optional[RevocationValues] = field(
        default=None,
        metadata={
            "name": "RevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    ur: Optional[str] = field(
        default=None,
        metadata={
            "name": "UR",
            "type": "Attribute",
        }
    )


@dataclass
class TimeStampValidationData(ValidationDataType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"
