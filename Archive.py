import time
from Tools import Tools
from Authorization import AuthWSActions
from xsdata.formats.dataclass.client import Client
from Variables import Variable
from com.izibiz.archive.efaturatest.izibiz.com.tr.eiarchive_ws import EfaturaArchivePortWriteToArchiveExtendedOutput, \
    EfaturaArchivePortWriteToArchiveExtended, EfaturaArchivePortWriteToArchiveExtendedInput, \
    EfaturaArchivePortReadFromArchiveOutput, EfaturaArchivePortReadFromArchive, EfaturaArchivePortReadFromArchiveInput, \
    EfaturaArchivePortGetEarchiveInvoiceStatusOutput, EfaturaArchivePortGetEarchiveInvoiceStatus, \
    EfaturaArchivePortGetEarchiveInvoiceStatusInput, EfaturaArchivePortCancelEarchiveInvoiceOutput, \
    EfaturaArchivePortCancelEarchiveInvoice, EfaturaArchivePortCancelEarchiveInvoiceInput, \
    EfaturaArchivePortGetEmailEarchiveInvoiceOutput, EfaturaArchivePortGetEmailEarchiveInvoice, \
    EfaturaArchivePortGetEmailEarchiveInvoiceInput, EfaturaArchivePortGetEarchiveReport, \
    EfaturaArchivePortGetEarchiveReportInput, EfaturaArchivePortGetEarchiveReportOutput, \
    EfaturaArchivePortReadEarchiveReportOutput, EfaturaArchivePortReadEarchiveReport, \
    EfaturaArchivePortReadEarchiveReportInput
from com.izibiz.archive.efaturatest.izibiz.com.tr_443.eiarchive_ws import RequestHeadertype, FlagValue, \
    EarsivProperties, EarsivTypeValue, SubStatusValue, ArchiveInvoiceExtendedContent, ArchiveInvoiceExtendedRequest, \
    ArchiveInvoiceReadRequest, ArchiveInvoiceReadResponse, ArchiveInvoiceExtendedResponse, \
    GetEarchiveInvoiceStatusRequest, GetEarchiveInvoiceStatusResponse, CancelEarchiveInvoiceRequest, \
    CancelEarchiveInvoiceResponse, GetEmailEarchiveInvoiceRequest, GetEmailEarchiveInvoiceResponse, \
    GetEarchiveReportResponse, GetEarchiveReportRequest, ReadEarchiveReportRequest, ReadEarchiveReportResponse


class EArchiveActions:
    """E-Fatura mükellefi olmayan firma veya nihai tüketiciye düzenlenen faturaların özel entegratör
       sistemine gönderilmesi ve raporlamasını sağlayan webservis uygulamasıdır."""

    authWSActions = AuthWSActions()
    session_id = authWSActions.login()
    tools = Tools()
    varianles = Variable()

    def write_to_archieve_extended(self):
        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "Y"

        earsivProperties = EarsivProperties()
        earsivProperties.earsiv_type = EarsivTypeValue.NORMAL
        earsivProperties.sub_status = SubStatusValue.NEW
        earsivProperties.seri = "SMM"
        earsivProperties.earsiv_email_flag = FlagValue.N
        earsivProperties.earsiv_email = "destek@izibiz.com.tr"
        earsivProperties.earsiv_sms_flag = FlagValue.N
        earsivProperties.sms_phone_number = "5050000000"

        invoiceProperties = ArchiveInvoiceExtendedContent.InvoiceProperties()
        archiveInvoiceExtendedContent = ArchiveInvoiceExtendedContent()
        invoiceProperties.earsiv_flag = FlagValue.Y
        invoiceProperties.earsiv_properties = earsivProperties
        invoiceProperties.archive_note = "Belge Arsive Alindi"
        content, uuid = self.tools.prepare_loading_content_inZipfile()
        invoiceProperties.invoice_content = content
        archiveInvoiceExtendedContent.invoice_properties = invoiceProperties

        archiveInvoiceExtendedRequest = ArchiveInvoiceExtendedRequest()
        archiveInvoiceExtendedResponse = ArchiveInvoiceExtendedResponse()
        archiveInvoiceExtendedRequest.request_header = request_header_type
        archiveInvoiceExtendedRequest.archive_invoice_extended_content = archiveInvoiceExtendedContent

        efaturaArchivePortWriteToArchiveExtendedOutput = EfaturaArchivePortWriteToArchiveExtendedOutput()
        efaturaArchivePortWriteToArchiveExtendedOutput = self.send_request(EfaturaArchivePortWriteToArchiveExtended,
                                                                           EfaturaArchivePortWriteToArchiveExtendedInput,
                                                                           archiveInvoiceExtendedRequest)

        archiveInvoiceExtendedResponse = efaturaArchivePortWriteToArchiveExtendedOutput.body.archive_invoice_extended_response
        print("\nE Arsive Gonderme Islemine Ait Bilgiler : \n**********************************")
        print("INTL_TXN_ID : ", archiveInvoiceExtendedResponse.request_return.intl_txn_id)
        print("CLIENT_TXN_ID : ", archiveInvoiceExtendedResponse.request_return.client_txn_id)
        print("RETURN_CODE : ", archiveInvoiceExtendedResponse.request_return.return_code)
        print("WARNINGS : ", archiveInvoiceExtendedResponse.request_return.warnings)
        print("INVOICE_ID : ", archiveInvoiceExtendedResponse.invoice_id)
        print("ERROR_TYPE : ", archiveInvoiceExtendedResponse.error_type)
        print("WEB_KEY : ", archiveInvoiceExtendedResponse.web_key)

        return uuid

    def read_from_archive(self):
        """Özel entegratör sistemine gönderilen e-arşiv faturalarının farklı formatlarda (XML,HTML,PDF)
           okumasını sağlayan servistir.Bu metotta belgeler compressed="Y" formatında indirilmektedir.
           compressed="Y" de PDF ve HTML zip formatında indirilirken XML kendi formatında yani .xml olarak indirilir.."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "Y"

        archiveInvoiceReadRequest = ArchiveInvoiceReadRequest()
        archiveInvoiceReadResponse = ArchiveInvoiceReadResponse()
        archiveInvoiceReadRequest.request_header = request_header_type
        archiveInvoiceReadRequest.invoiceid = "3353b5ea-bc9a-442c-ba41-2bb525260167"
        archiveInvoiceReadRequest.portal_direction = "OUT"
        archiveInvoiceReadRequest.profile = "XML"
        efaturaArchivePortReadFromArchiveOutput = EfaturaArchivePortReadFromArchiveOutput()
        efaturaArchivePortReadFromArchiveOutput = self.send_request(EfaturaArchivePortReadFromArchive,
                                                                    EfaturaArchivePortReadFromArchiveInput,
                                                                    archiveInvoiceReadRequest)

        archiveInvoiceReadResponse = efaturaArchivePortReadFromArchiveOutput.body.archive_invoice_read_response
        all_variables = vars(archiveInvoiceReadResponse)
        print("\nE Arsiv Fatura Indirme Islemine Ait Bilgiler : \n**********************************")
        for Key, Value in all_variables.items():
            if Key == "invoice":
                if archiveInvoiceReadRequest.profile == "PDF" or archiveInvoiceReadRequest.profile == "HTML":
                    self.tools.write_content_to_zip(Value[0].value, self.varianles.E_ARCHIVE,
                                                    archiveInvoiceReadRequest.invoiceid)
                elif archiveInvoiceReadRequest.profile == "XML":
                    path = f"Files/EArchive/{archiveInvoiceReadRequest.invoiceid}.xml"
                    file = open(path, 'wb')
                    file.write(Value[0].value)

                print("-\t", Key, ":", f"Files/EArchive/{archiveInvoiceReadRequest.invoiceid} Dizinine Kaydedildi.")
            if Key == "request_return":
                all_variables = vars(Value)
                for key, value in all_variables.items():
                    print("-\t", key, ":", value)

    def get_archive_status(self):
        """Özel entegratör platformuna gönderilen bir veya birden çok faturanın
        durumunu sorgulamayı sağlayan servistir."""
        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "Y"

        getEarchiveInvoiceStatusRequest = GetEarchiveInvoiceStatusRequest()
        getEarchiveInvoiceStatusResponse = GetEarchiveInvoiceStatusResponse()
        getEarchiveInvoiceStatusRequest.request_header = request_header_type
        getEarchiveInvoiceStatusRequest.uuid = "f181a2c1-e498-493c-a24a-415d9317bbf9"

        efaturaArchivePortGetEarchiveInvoiceStatusOutput = EfaturaArchivePortGetEarchiveInvoiceStatusOutput()
        efaturaArchivePortGetEarchiveInvoiceStatusOutput = self.send_request(EfaturaArchivePortGetEarchiveInvoiceStatus,
                                                                             EfaturaArchivePortGetEarchiveInvoiceStatusInput,
                                                                             getEarchiveInvoiceStatusRequest)

        getEarchiveInvoiceStatusResponse = efaturaArchivePortGetEarchiveInvoiceStatusOutput.body.get_earchive_invoice_status_response
        all_variables = vars(getEarchiveInvoiceStatusResponse)
        print("\nSorgulanan E Arsiv Faturasina Ait Bilgiler : \n**********************************")
        for Key, Value in all_variables.items():
            if Key == "invoice":
                header_dict = vars(Value[0].header)
                for key_1, value_1 in header_dict.items():
                    print("-\t", key_1, ":", value_1)
            if Key == "request_return":
                all_variables = vars(Value)
                for key, value in all_variables.items():
                    print("-\t", key, ":", value)

    def cancel_earsiv_invoice(self):
        """Entegratör platformuna gönderildikten veya GİB'e raporlandıktan sonra eksik veya hata tespit edilen
           veya müşteri tarafından iade edilen belgenin GIB'e iptal fatura durumunda raporlanmasını sağlayan servistir
           E-Arşiv platformunda bulunmayan faturalar için iptal_tarihi ve toplam_tutar değerleride kullanılmalıdır.
           Bu metotda ilk olarak sisteme e arşiv fatura yüklemesi yapılıyor ve daha sonra da bu yüklenen
           fatura iptal ediliyor. Yüklenen faturanın entegrator sistemine düşmesi için iptal edilmeden önce 10 bekleniyor.
           Entegrator sisteminde yoğunluk bulunması durumunda "iptal edilecek belge bulunamadı" hatası almamak için
           bekleme süresi manuel olarak artırılabili."""
        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id

        cancelEarchiveInvoiceRequest = CancelEarchiveInvoiceRequest()
        cancelEarchiveInvoiceResponse = CancelEarchiveInvoiceResponse()
        cancelEarsivInvoiceContent = CancelEarchiveInvoiceRequest.CancelEarsivInvoiceContent()

        cancelEarsivInvoiceContent.fatura_uuid = self.write_to_archieve_extended()
        time.sleep(10)
        cancelEarsivInvoiceContent.earsiv_cancel_email = "destek25@izibiz.com"
        cancelEarsivInvoiceContent.delete_flag = "N"
        cancelEarsivInvoiceContent.iptal_notu = "Yanlis fatura kesilmesinden kaynakli fatura iptal edilmistir"

        cancelEarchiveInvoiceRequest.request_header = request_header_type
        cancelEarchiveInvoiceRequest.cancel_earsiv_invoice_content = cancelEarsivInvoiceContent

        efaturaArchivePortCancelEarchiveInvoiceOutput = EfaturaArchivePortCancelEarchiveInvoiceOutput()
        efaturaArchivePortCancelEarchiveInvoiceOutput = self.send_request(EfaturaArchivePortCancelEarchiveInvoice,
                                                                          EfaturaArchivePortCancelEarchiveInvoiceInput,
                                                                          cancelEarchiveInvoiceRequest)
        cancelEarchiveInvoiceResponse = efaturaArchivePortCancelEarchiveInvoiceOutput.body.cancel_earchive_invoice_response
        all_variables = vars(cancelEarchiveInvoiceResponse)
        print("\nIptal Raporlanan E Arsiv Faturasina Ait Bilgiler : \n**********************************")
        for Key, Value in all_variables.items():
            if Value is not None:
                all_variables = vars(Value)
                for key, value in all_variables.items():
                    print("-\t", key, ":", value)
            else:
                print("-\t", Key, ":", Value)

    def get_email_archice_invoice(self):
        """E-Arşiv faturasını yükledikten sonra e-posta olarak aynı veya farklı e-postalara tekrar
           gönderilmesini sağlayan servistir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getEmailEarchiveInvoiceRequest = GetEmailEarchiveInvoiceRequest()
        getEmailEarchiveInvoiceRequest.request_header = request_header_type
        getEmailEarchiveInvoiceRequest.fatura_uuid = "2e75ba95-e68e-43c9-be9d-4cc99835b0f0"
        getEmailEarchiveInvoiceRequest.email = "muhammet.comertt.25@gmail.com"

        getEmailEarchiveInvoiceResponse = GetEmailEarchiveInvoiceResponse()
        efaturaArchivePortGetEmailEarchiveInvoiceOutput = EfaturaArchivePortGetEmailEarchiveInvoiceOutput()
        efaturaArchivePortGetEmailEarchiveInvoiceOutput = self.send_request(EfaturaArchivePortGetEmailEarchiveInvoice,
                                                                            EfaturaArchivePortGetEmailEarchiveInvoiceInput,
                                                                            getEmailEarchiveInvoiceRequest)

        getEmailEarchiveInvoiceResponse = efaturaArchivePortGetEmailEarchiveInvoiceOutput.body.get_email_earchive_invoice_response

        all_variables = vars(getEmailEarchiveInvoiceResponse)
        print("\nMaile Fatura Gonderme Islemine Ait Bilgiler\n**********************************")
        for Key, Value in all_variables.items():
            if Value is not None:
                all_variables = vars(Value)
                for key, value in all_variables.items():
                    print("-\t", key, ":", value)
            else:
                print("-\t", Key, ":", Value)

    def get_archice_report(self):
        """Özel entegratör platformunda mükellefe ait oluşturulan bir döneme ait rapor listesini çekmek için
           kullanılır. Bu servis sadece rapor listesini döndecektir. Servisin döndüğü raporlara ait içerikleri
           almak için ReadEArchiveReport servisi kullanılabilir."""
        report_no = ""
        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getEarchiveReportRequest = GetEarchiveReportRequest()
        getEarchiveReportResponse = GetEarchiveReportResponse()
        getEarchiveReportRequest.request_header = request_header_type
        getEarchiveReportRequest.report_status_flag = "Y"
        getEarchiveReportRequest.report_period = "202311"

        efaturaArchivePortGetEarchiveReportOutput = EfaturaArchivePortGetEarchiveReportOutput()
        efaturaArchivePortGetEarchiveReportOutput = self.send_request(EfaturaArchivePortGetEarchiveReport,
                                                                      EfaturaArchivePortGetEarchiveReportInput,
                                                                      getEarchiveReportRequest)

        getEarchiveReportResponse = efaturaArchivePortGetEarchiveReportOutput.body.get_earchive_report_response
        all_variables = vars(getEarchiveReportResponse)
        print("\nListelenen Raporlara Ait Bilgiler\n**********************************")
        for Key, Value in all_variables.items():
            if Key == "request_return":
                print("-\t", Key, ":", Value)

            elif Key == "error_type":
                print("-\t", Key, ":", Value)

            elif Key == "report":

                path = "Files/EArchive/earchive_rapor_list.txt"
                file = open(path, 'w')

                for temp in Value:
                    report_no = temp.report_no
                    file.write(f"{temp}\n")
                    print(f"-\t{temp}")
                file.close()

            else:
                pass

        return report_no

    def read_earchive_report(self):
        """Mükellef için GİB'e gönderilen raporun imzalı XML dosyasını okumayı sağlayan servistir.
           rapor numarası olarak get_archice_report servisindeki son raporun numrasını kullanır"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        readEarchiveReportRequest = ReadEarchiveReportRequest()
        readEarchiveReportResponse = ReadEarchiveReportResponse()
        readEarchiveReportRequest.request_header = request_header_type
        readEarchiveReportRequest.rapor_no = self.get_archice_report()

        efaturaArchivePortReadEarchiveReportOutput = EfaturaArchivePortReadEarchiveReportOutput()
        efaturaArchivePortReadEarchiveReportOutput = self.send_request(EfaturaArchivePortReadEarchiveReport,
                                                                       EfaturaArchivePortReadEarchiveReportInput,
                                                                       readEarchiveReportRequest)

        readEarchiveReportResponse = efaturaArchivePortReadEarchiveReportOutput.body.read_earchive_report_response
        all_variables = vars(readEarchiveReportResponse)
        print("\nRapor Cekme Islemine Ait Bilgiler : \n**********************************")
        all_variables = vars(readEarchiveReportResponse)
        for key, value in all_variables.items():
            if key == "earchivereport":
                path = f"Files/EArchive/{readEarchiveReportRequest.rapor_no}.zip"
                file = open(path, 'wb')
                file.write(value[0].value)
                print("-\t", key, ":", f"Belge Files/EArchive/{readEarchiveReportRequest.rapor_no}.zip konumuna kaydedildi")
            else:
                print("-\t", key, ":", value)

    def send_request(self, service_name, input_service_name, request_data):
        client = Client.from_service(service_name)
        request = input_service_name(
            body=input_service_name.Body(request_data))
        response = client.send(request)
        return response


eArchiveActions = EArchiveActions()
eArchiveActions.write_to_archieve_extended()
eArchiveActions.read_from_archive()
eArchiveActions.get_archive_status()
eArchiveActions.cancel_earsiv_invoice()
eArchiveActions.get_email_archice_invoice()
eArchiveActions.get_archice_report()
eArchiveActions.read_earchive_report()
