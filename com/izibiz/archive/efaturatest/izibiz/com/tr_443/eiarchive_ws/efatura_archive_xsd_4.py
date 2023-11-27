from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws.efatura_archive_xsd_3 import Signature

__NAMESPACE__ = "http://earsiv.efatura.gov.tr"


@dataclass
class AliciType:
    class Meta:
        name = "aliciType"

    tuzel_kisi: Optional["AliciType.TuzelKisi"] = field(
        default=None,
        metadata={
            "name": "tuzelKisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )
    gercek_kisi: Optional["AliciType.GercekKisi"] = field(
        default=None,
        metadata={
            "name": "gercekKisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )
    tesisat_numarasi: Optional[str] = field(
        default=None,
        metadata={
            "name": "tesisatNumarasi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )

    @dataclass
    class TuzelKisi:
        vkn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "pattern": r"\d\d\d\d\d\d\d\d\d\d",
            }
        )
        unvan: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "min_length": 2,
            }
        )

    @dataclass
    class GercekKisi:
        tckn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "pattern": r"\d\d\d\d\d\d\d\d\d\d\d",
            }
        )
        adi_soyadi: Optional[str] = field(
            default=None,
            metadata={
                "name": "adiSoyadi",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "min_length": 2,
            }
        )


@dataclass
class FaturaIptalType:
    class Meta:
        name = "faturaIptalType"

    fatura_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "faturaNo",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "length": 16,
            "pattern": r"[A-Za-z0-9]{3}20[0-9]{2}[0-9]{9}",
        }
    )
    iptal_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "iptalTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    toplam_tutar: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "toplamTutar",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 2,
        }
    )


class FaturaTypeGonderimSekli(Enum):
    KAGIT = "KAGIT"
    ELEKTRONIK = "ELEKTRONIK"


class FaturaTypeParaBirimi(Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    USS = "USS"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XFU = "XFU"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XTS = "XTS"
    XUA = "XUA"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWL = "ZWL"


@dataclass
class KisiType:
    class Meta:
        name = "kisiType"

    tuzel_kisi: Optional["KisiType.TuzelKisi"] = field(
        default=None,
        metadata={
            "name": "tuzelKisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )
    gercek_kisi: Optional["KisiType.GercekKisi"] = field(
        default=None,
        metadata={
            "name": "gercekKisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )

    @dataclass
    class TuzelKisi:
        vkn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "pattern": r"\d\d\d\d\d\d\d\d\d\d",
            }
        )
        unvan: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "min_length": 2,
            }
        )

    @dataclass
    class GercekKisi:
        tckn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "pattern": r"\d\d\d\d\d\d\d\d\d\d\d",
            }
        )
        adi_soyadi: Optional[str] = field(
            default=None,
            metadata={
                "name": "adiSoyadi",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "min_length": 2,
            }
        )


class OdemeTipEnum(Enum):
    KREDIKARTI_BANKAKARTI = "KREDIKARTI/BANKAKARTI"
    EFT_HAVALE = "EFT/HAVALE"
    KAPIDAODEME = "KAPIDAODEME"
    ODEMEARACISI = "ODEMEARACISI"


class TevkifatTevkifatKodu(Enum):
    VALUE_301 = "301"
    VALUE_302 = "302"
    VALUE_303 = "303"
    VALUE_304 = "304"
    VALUE_305 = "305"
    VALUE_306 = "306"
    VALUE_308 = "308"
    VALUE_309 = "309"
    VALUE_310 = "310"
    VALUE_311 = "311"
    VALUE_312 = "312"
    VALUE_313 = "313"
    VALUE_314 = "314"
    VALUE_315 = "315"
    VALUE_316 = "316"
    VALUE_317 = "317"
    VALUE_318 = "318"
    VALUE_319 = "319"
    VALUE_320 = "320"
    VALUE_321 = "321"
    VALUE_350 = "350"
    VALUE_601 = "601"
    VALUE_602 = "602"
    VALUE_603 = "603"
    VALUE_604 = "604"
    VALUE_605 = "605"
    VALUE_606 = "606"
    VALUE_607 = "607"
    VALUE_608 = "608"
    VALUE_609 = "609"
    VALUE_610 = "610"
    VALUE_611 = "611"
    VALUE_612 = "612"
    VALUE_613 = "613"
    VALUE_614 = "614"
    VALUE_615 = "615"
    VALUE_616 = "616"
    VALUE_617 = "617"
    VALUE_618 = "618"
    VALUE_619 = "619"
    VALUE_620 = "620"
    VALUE_621 = "621"
    VALUE_622 = "622"
    VALUE_623 = "623"
    VALUE_650 = "650"


class VergiVergiKodu(Enum):
    VALUE_0003 = "0003"
    VALUE_0015 = "0015"
    VALUE_0061 = "0061"
    VALUE_0071 = "0071"
    VALUE_0073 = "0073"
    VALUE_0074 = "0074"
    VALUE_0075 = "0075"
    VALUE_0076 = "0076"
    VALUE_0077 = "0077"
    VALUE_1047 = "1047"
    VALUE_1048 = "1048"
    VALUE_4080 = "4080"
    VALUE_4081 = "4081"
    VALUE_4171 = "4171"
    VALUE_9015 = "9015"
    VALUE_9021 = "9021"
    VALUE_9077 = "9077"
    VALUE_8001 = "8001"
    VALUE_8002 = "8002"
    VALUE_8003 = "8003"
    VALUE_8004 = "8004"
    VALUE_8005 = "8005"
    VALUE_8006 = "8006"
    VALUE_8007 = "8007"
    VALUE_8008 = "8008"


@dataclass
class VknTcknType:
    class Meta:
        name = "vknTcknType"

    vkn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "pattern": r"\d\d\d\d\d\d\d\d\d\d",
        }
    )
    tckn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "pattern": r"\d\d\d\d\d\d\d\d\d\d\d",
        }
    )


@dataclass
class BaslikType:
    class Meta:
        name = "baslikType"

    versiyon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    mukellef: Optional[VknTcknType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    hazirlayan: Optional[VknTcknType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    rapor_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "raporNo",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "length": 36,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    donem_baslangic_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "donemBaslangicTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    donem_bitis_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "donemBitisTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    bolum_baslangic_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "bolumBaslangicTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    bolum_bitis_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "bolumBitisTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    bolum_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "bolumNo",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class FaturaIptal(FaturaIptalType):
    class Meta:
        name = "faturaIptal"
        namespace = "http://earsiv.efatura.gov.tr"


@dataclass
class FaturaType:
    class Meta:
        name = "faturaType"

    fatura_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "faturaNo",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "length": 16,
            "pattern": r"[A-Za-z0-9]{3}20[0-9]{2}[0-9]{9}",
        }
    )
    gonderim_sekli: Optional[FaturaTypeGonderimSekli] = field(
        default=None,
        metadata={
            "name": "gonderimSekli",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    dosya_adi: Optional[str] = field(
        default=None,
        metadata={
            "name": "dosyaAdi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    ozet_deger: Optional[str] = field(
        default=None,
        metadata={
            "name": "ozetDeger",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    duzenlenme_tarihi: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "duzenlenmeTarihi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    duzenlenme_zamani: Optional[str] = field(
        default=None,
        metadata={
            "name": "duzenlenmeZamani",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "min_inclusive": "00:00:00",
            "pattern": r"(([01][0-9])|(2[0-3]))(:[0-5][0-9]){2}(\.[0-9]+)?",
        }
    )
    toplam_tutar: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "toplamTutar",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 2,
        }
    )
    odenecek_tutar: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "odenecekTutar",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 2,
        }
    )
    para_birimi: Optional[FaturaTypeParaBirimi] = field(
        default=None,
        metadata={
            "name": "paraBirimi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    vergi_bilgisi: Optional["FaturaType.VergiBilgisi"] = field(
        default=None,
        metadata={
            "name": "vergiBilgisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    alici_bilgileri: Optional[AliciType] = field(
        default=None,
        metadata={
            "name": "aliciBilgileri",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
            "required": True,
        }
    )
    internet_satis_bilgi: Optional["FaturaType.InternetSatisBilgi"] = field(
        default=None,
        metadata={
            "name": "internetSatisBilgi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )
    yn_okc_fis_bilgisi: Optional["FaturaType.YnOkcFisBilgisi"] = field(
        default=None,
        metadata={
            "name": "ynOkcFisBilgisi",
            "type": "Element",
            "namespace": "http://earsiv.efatura.gov.tr",
        }
    )

    @dataclass
    class VergiBilgisi:
        vergiler_toplami: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "vergilerToplami",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "total_digits": 18,
                "fraction_digits": 2,
            }
        )
        vergi: List["FaturaType.VergiBilgisi.Vergi"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "min_occurs": 1,
            }
        )
        tevkifat: List["FaturaType.VergiBilgisi.Tevkifat"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
            }
        )

        @dataclass
        class Vergi:
            matrah: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                    "total_digits": 18,
                    "fraction_digits": 2,
                }
            )
            vergi_kodu: Optional[VergiVergiKodu] = field(
                default=None,
                metadata={
                    "name": "vergiKodu",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                }
            )
            vergi_tutari: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "vergiTutari",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                    "total_digits": 18,
                    "fraction_digits": 2,
                }
            )
            vergi_orani: Optional[int] = field(
                default=None,
                metadata={
                    "name": "vergiOrani",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                    "min_inclusive": 0,
                    "max_inclusive": 100,
                    "total_digits": 3,
                }
            )

        @dataclass
        class Tevkifat:
            tevkifat_kodu: Optional[TevkifatTevkifatKodu] = field(
                default=None,
                metadata={
                    "name": "tevkifatKodu",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                }
            )
            tevkifat_tutari: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "tevkifatTutari",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                    "total_digits": 18,
                    "fraction_digits": 2,
                }
            )
            tevkifat_orani: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "tevkifatOrani",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                    "max_inclusive": Decimal("100"),
                    "total_digits": 5,
                    "fraction_digits": 2,
                }
            )

    @dataclass
    class InternetSatisBilgi:
        web_adresi: Optional[str] = field(
            default=None,
            metadata={
                "name": "webAdresi",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "min_length": 2,
            }
        )
        odeme_sekli: Optional[Union[OdemeTipEnum, str]] = field(
            default=None,
            metadata={
                "name": "odemeSekli",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
                "pattern": r"DIGER - \S.*",
            }
        )
        odeme_aracisi_adi: Optional[str] = field(
            default=None,
            metadata={
                "name": "odemeAracisiAdi",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
            }
        )
        odeme_tarihi: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "odemeTarihi",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
            }
        )
        gonderi_bilgileri: Optional["FaturaType.InternetSatisBilgi.GonderiBilgileri"] = field(
            default=None,
            metadata={
                "name": "gonderiBilgileri",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
            }
        )

        @dataclass
        class GonderiBilgileri:
            gonderim_tarihi: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "gonderimTarihi",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                }
            )
            gonderi_tasiyan: Optional[KisiType] = field(
                default=None,
                metadata={
                    "name": "gonderiTasiyan",
                    "type": "Element",
                    "namespace": "http://earsiv.efatura.gov.tr",
                    "required": True,
                }
            )

    @dataclass
    class YnOkcFisBilgisi:
        okc_seri_no: Optional[str] = field(
            default=None,
            metadata={
                "name": "okcSeriNo",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
            }
        )
        z_no: Optional[str] = field(
            default=None,
            metadata={
                "name": "zNo",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
            }
        )
        fis_no: Optional[str] = field(
            default=None,
            metadata={
                "name": "fisNo",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
            }
        )
        fis_tarih: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "fisTarih",
                "type": "Element",
                "namespace": "http://earsiv.efatura.gov.tr",
                "required": True,
            }
        )


@dataclass
class EArsivRaporu:
    """
    EArsiv Rapor Bilgileri.
    """
    class Meta:
        name = "eArsivRaporu"
        namespace = "http://earsiv.efatura.gov.tr"

    baslik: Optional[BaslikType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fatura: List[FaturaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fatura_iptal: List[FaturaIptalType] = field(
        default_factory=list,
        metadata={
            "name": "faturaIptal",
            "type": "Element",
        }
    )


@dataclass
class Fatura(FaturaType):
    class Meta:
        name = "fatura"
        namespace = "http://earsiv.efatura.gov.tr"
