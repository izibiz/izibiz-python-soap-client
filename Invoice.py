from Tools import Tools
from Authorization import AuthWSActions
from xsdata.formats.dataclass.client import Client
from datetime import datetime, timedelta
from Variables import Variable

from com.izibiz.invoice.efaturatest.izibiz.com.tr import EinvoiceWsportSendInvoice, EinvoiceWsportSendInvoiceInput, \
    EinvoiceWsportLoadInvoice, EinvoiceWsportLoadInvoiceInput, EinvoiceWsportGetInvoice, EinvoiceWsportGetInvoiceInput, \
    EinvoiceWsportSendInvoiceOutput, EinvoiceWsportLoadInvoiceOutput, EinvoiceWsportGetInvoiceOutput, \
    EinvoiceWsportGetInvoiceWithTypeOutput, EinvoiceWsportGetInvoiceWithType, EinvoiceWsportGetInvoiceWithTypeInput, \
    EinvoiceWsportMarkInvoiceOutput, EinvoiceWsportMarkInvoice, EinvoiceWsportMarkInvoiceInput, \
    EinvoiceWsportGetInvoiceStatusInput, EinvoiceWsportGetInvoiceStatus, EinvoiceWsportGetInvoiceStatusOutput, \
    EinvoiceWsportGetInvoiceStatusAllOutput, EinvoiceWsportGetInvoiceStatusAll, EinvoiceWsportGetInvoiceStatusAllInput, \
    EinvoiceWsportSendInvoiceResponseWithServerSign, EinvoiceWsportSendInvoiceResponseWithServerSignOutput, \
    EinvoiceWsportSendInvoiceResponseWithServerSignInput
from com.izibiz.invoice.efaturatest.izibiz.com.tr_443 import SendInvoiceRequest, RequestHeadertype, Invoice, \
    LoadInvoiceRequest, GetInvoiceRequest, DateType, GetInvoiceWithTypeRequest, MarkInvoiceRequest, MarkValue, \
    GetInvoiceStatusRequest, GetInvoiceStatusAllRequest, SendInvoiceResponseWithServerSignRequest, \
    GetInvoiceStatusAllResponse, SendInvoiceResponseWithServerSignResponse, SendInvoiceResponse, LoadInvoiceResponse, \
    GetInvoiceResponse, GetInvoiceWithTypeResponse, MarkInvoiceResponse, GetInvoiceStatusResponse


class EInvoiceActions:
    """e-fatura mükellefinin fatura gönderimini ve gelen faturaları kendisi
    sistemine çekmesini sağlayan webservis uygulamasıdır."""

    authWSActions = AuthWSActions()
    session_id = authWSActions.login()
    tools = Tools()
    varianles = Variable()

    def SendInvoice(self):
        """FATURA Entegrasyon Platformu üzerinden 1 yada daha fazla faturayı GIB EFATURA sistemine gönderir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "N"
        sendInvoiceRequest = SendInvoiceRequest()
        sendInvoiceResponse = SendInvoiceResponse()

        SendInvoiceRequest.Receiver.alias = "urn:mail:defaultpk@izibiz.com.tr"
        SendInvoiceRequest.Receiver.vkn = "4840847211"

        invoice = Invoice()
        data_base64, random_uuid = self.tools.set_loading_content()
        invoice.content = data_base64
        sendInvoiceRequest.request_header = request_header_type
        sendInvoiceRequest.invoice = invoice

        einvoiceWsportSendInvoiceOutput = EinvoiceWsportSendInvoiceOutput()
        einvoiceWsportSendInvoiceOutput = self.send_request(EinvoiceWsportSendInvoice,
                                                            EinvoiceWsportSendInvoiceInput,
                                                            sendInvoiceRequest)

        sendInvoiceResponse = einvoiceWsportSendInvoiceOutput.body.send_invoice_response
        print("\nSend Invoice : \n******************************")
        all_variables = vars(sendInvoiceResponse)
        for Key, Value in all_variables.items():
            if Value is not None:
                if Key == "request_return" or "error_type":
                    all_variables = vars(Value)
                    for key, value in all_variables.items():
                        print("-\t", key, ":", value)
                else:
                    print("-\t", Key, ":", Value)
            else:
                print("-\t", Key, ":", Value)

    def load_invoice(self):
        """FATURA Entegrasyon Platformu üzerinden 1 yada daha fazla faturayı E-Fatura sistemine yükler.
           Eğer fatura numarası atanmışsa (16 hane ise) şema ve şematron kontrolünden geçirilir.
           atanmamışsa şema ve şematron kontrolü yapılmaz. Aynı faturanın tekrar yüklenmesine müsade edilir.
           Farklı kayıt oluşturulmaz. Oluşan kayıt yeni içerik ile güncellenir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "N"
        loadInvoiceRequest = LoadInvoiceRequest()
        loadInvoiceResponse = LoadInvoiceResponse()

        invoice = Invoice()
        data_base64, random_uuid = self.tools.set_loading_content()
        invoice.content = data_base64
        loadInvoiceRequest.request_header = request_header_type
        loadInvoiceRequest.invoice = invoice

        einvoiceWsportLoadInvoiceOutput = EinvoiceWsportLoadInvoiceOutput()
        einvoiceWsportLoadInvoiceOutput = self.send_request(EinvoiceWsportLoadInvoice,
                                                            EinvoiceWsportLoadInvoiceInput,
                                                            loadInvoiceRequest)
        loadInvoiceResponse = einvoiceWsportLoadInvoiceOutput.body.load_invoice_response
        print("\nLoad Invoice : \n******************************")
        all_variables = vars(loadInvoiceResponse)
        print("-\t Belgen UUID Degeri :",random_uuid )
        for Key, Value in all_variables.items():
            if Value is not None:
                if Key == "request_return" or "error_type":
                    all_variables = vars(Value)
                    for key, value in all_variables.items():
                        print("-\t", key, ":", value)
                else:
                    print("-\t", Key, ":", Value)
            else:
                print("-\t", Key, ":", Value)

        return random_uuid

    def get_invoice_scenario_1(self):
        """E-Fatura sisteminden giden imzalı veya gelen faturaları muhasebe paketine çekmek için kullanılır.
           date_type = "CREATE",start_date = today, end_date = (today - 30) , header_only = "Y" senaryosu"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getInvoiceRequest = GetInvoiceRequest()
        getInvoiceResponse = GetInvoiceResponse()
        invoice_search_key = GetInvoiceRequest.InvoiceSearchKey()
        invoice_search_key.limit = 10
        invoice_search_key.read_included = True
        invoice_search_key.direction = "IN"

        invoice_search_key.date_type = DateType.CREATE
        today = datetime.now()
        thirty_days_ago = today - timedelta(days=30)
        invoice_search_key.start_date = thirty_days_ago.strftime("%Y-%m-%d")
        invoice_search_key.end_date = today.strftime("%Y-%m-%d")
        getInvoiceRequest.header_only = "Y"

        getInvoiceRequest.request_header = request_header_type
        getInvoiceRequest.invoice_search_key = invoice_search_key

        einvoiceWsportGetInvoiceOutput = EinvoiceWsportGetInvoiceOutput()
        einvoiceWsportGetInvoiceOutput = self.send_request(EinvoiceWsportGetInvoice,
                                                           EinvoiceWsportGetInvoiceInput,
                                                           getInvoiceRequest)
        print("\nVerilen Tarih Araligindaki Fatura(Date Type : CREATE) Bilgileri: ")
        getInvoiceResponse = einvoiceWsportGetInvoiceOutput.body.get_invoice_response
        self.tools.display_invoice_header(getInvoiceResponse, self.varianles.GETINVOICE)

    def get_invoice_scenario_2(self):
        """E-Fatura sisteminden giden imzalı veya gelen faturaları muhasebe paketine çekmek için kullanılır.
           date_type = "ISSUE, start_date = today, end_date = (today - 30), header_only = "Y" senaryosu"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getInvoiceRequest = GetInvoiceRequest()
        getInvoiceResponse = GetInvoiceResponse()
        invoice_search_key = GetInvoiceRequest.InvoiceSearchKey()
        invoice_search_key.limit = 15
        invoice_search_key.read_included = True
        invoice_search_key.direction = "IN"

        invoice_search_key.date_type = DateType.ISSUE
        today = datetime.now()
        thirty_days_ago = today - timedelta(days=30)
        invoice_search_key.start_date = thirty_days_ago.strftime("%Y-%m-%d")
        invoice_search_key.end_date = today.strftime("%Y-%m-%d")
        getInvoiceRequest.header_only = "N"

        getInvoiceRequest.request_header = request_header_type
        getInvoiceRequest.invoice_search_key = invoice_search_key

        einvoiceWsportGetInvoiceOutput = EinvoiceWsportGetInvoiceOutput()
        einvoiceWsportGetInvoiceOutput = self.send_request(EinvoiceWsportGetInvoice,
                                                           EinvoiceWsportGetInvoiceInput,
                                                           getInvoiceRequest)
        print("\nVerilen Tarih Araligindaki Fatura(Date Type : ISSUE) Bilgileri: ")
        getInvoiceResponse = einvoiceWsportGetInvoiceOutput.body.get_invoice_response
        self.tools.display_invoice_header(getInvoiceResponse, self.varianles.GETINVOICE)

    def get_invoice_scenario_3(self):
        """E-Fatura sisteminden giden imzalı veya gelen faturaları muhasebe paketine çekmek için kullanılır.
            id = "MUH2023000027507" ile çekme senaryosu"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getInvoiceRequest = GetInvoiceRequest()
        getInvoiceResponse = GetInvoiceResponse()
        invoice_search_key = GetInvoiceRequest.InvoiceSearchKey()
        invoice_search_key.limit = "15"
        invoice_search_key.read_included = True
        invoice_search_key.direction = "IN"

        invoice_search_key.id = "MUH2023000026232"
        getInvoiceRequest.header_only = "Y"

        getInvoiceRequest.request_header = request_header_type
        getInvoiceRequest.invoice_search_key = invoice_search_key

        einvoiceWsportGetInvoiceOutput = EinvoiceWsportGetInvoiceOutput()
        einvoiceWsportGetInvoiceOutput = self.send_request(EinvoiceWsportGetInvoice,
                                                           EinvoiceWsportGetInvoiceInput,
                                                           getInvoiceRequest)

        print("\nVerilen Id Değerine Sahip Fatura Bilgileri: ")
        getInvoiceResponse = einvoiceWsportGetInvoiceOutput.body.get_invoice_response
        self.tools.display_invoice_header(getInvoiceResponse, self.varianles.GETINVOICE)

    def get_invoice_scenario_4(self):
        """E-Fatura sisteminden giden imzalı veya gelen faturaları muhasebe paketine çekmek için kullanılır.
            uuid ="993d2505-a05e-4c40-bd21-fd9e8e455ae7" ile çekme senaryosu"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getInvoiceRequest = GetInvoiceRequest()
        getInvoiceResponse = GetInvoiceResponse()
        invoice_search_key = GetInvoiceRequest.InvoiceSearchKey()
        invoice_search_key.limit = "15"
        invoice_search_key.read_included = True
        invoice_search_key.direction = "IN"

        invoice_search_key.uuid = "993d2505-a05e-4c40-bd21-fd9e8e455ae7"
        getInvoiceRequest.header_only = "Y"

        getInvoiceRequest.request_header = request_header_type
        getInvoiceRequest.invoice_search_key = invoice_search_key

        einvoiceWsportGetInvoiceOutput = EinvoiceWsportGetInvoiceOutput()
        einvoiceWsportGetInvoiceOutput = self.send_request(EinvoiceWsportGetInvoice,
                                                           EinvoiceWsportGetInvoiceInput,
                                                           getInvoiceRequest)

        print("\nVerilen Uuid Değerine Sahip Fatura Bilgileri: ")
        getInvoiceResponse = einvoiceWsportGetInvoiceOutput.body.get_invoice_response
        self.tools.display_invoice_header(getInvoiceResponse, self.varianles.GETINVOICE)

    def get_invoice_with_type(self):
        """E-Fatura sisteminden bulunan bir faturanın görselini çekmek için tasarlanmış servistir.
        uuid = "993d2505-a05e-4c40-bd21-fd9e8e455ae7" ve direction = "OUT" ile fatura görsel(xml) okuma senaryosu"""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.application_name = "INVOICE"
        getInvoiceWithTypeRequest = GetInvoiceWithTypeRequest()
        getInvoiceWithTypeResponse = GetInvoiceWithTypeResponse()
        invoice_search_key = GetInvoiceWithTypeRequest.InvoiceSearchKey()
        getInvoiceWithTypeRequest.header_only = "N"
        invoice_search_key.read_included = True
        invoice_search_key.uuid = "77827d1c-3d9a-407f-a07e-523b15e4c4d6"
        invoice_search_key.id = "SFT2023333721482"
        invoice_search_key.type_value = "PDF"
        invoice_search_key.direction = "OUT"
        getInvoiceWithTypeRequest.request_header = request_header_type
        getInvoiceWithTypeRequest.invoice_search_key = invoice_search_key

        einvoiceWsportGetInvoiceWithTypeOutput = EinvoiceWsportGetInvoiceWithTypeOutput()
        einvoiceWsportGetInvoiceWithTypeOutput = self.send_request(EinvoiceWsportGetInvoiceWithType,
                                                                   EinvoiceWsportGetInvoiceWithTypeInput,
                                                                   getInvoiceWithTypeRequest)
        print("\nGorseli Cekilmek Istenen Fatura Bilgileri: ")
        getInvoiceWithTypeResponse = einvoiceWsportGetInvoiceWithTypeOutput.body.get_invoice_with_type_response
        self.tools.display_invoice_header(getInvoiceWithTypeResponse, self.varianles.GETINVOICEWITHTYPE)

    def mark_invoice(self):
        """E-Fatura sisteminde bir veya daha fazla faturayı alındı/alınmadı olarak
           işaretlemek için geliştirilmiş servistir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.application_name = "INVOICE"
        markInvoiceRequest = MarkInvoiceRequest()
        markInvoiceResponse = MarkInvoiceResponse()
        invoice = Invoice()
        invoice.id = "MUH2023000086913"
        invoice.uuid = "afa98272-b251-47b7-9337-9ad0fcc84254"
        mark = MarkInvoiceRequest.Mark()
        mark.value = MarkValue.READ
        mark.invoice = invoice

        markInvoiceRequest.request_header = request_header_type
        markInvoiceRequest.mark = mark
        einvoiceWsportMarkInvoiceOutput = EinvoiceWsportMarkInvoiceOutput()
        einvoiceWsportMarkInvoiceOutput = self.send_request(EinvoiceWsportMarkInvoice,
                                                            EinvoiceWsportMarkInvoiceInput,
                                                            markInvoiceRequest)

        markInvoiceResponse = einvoiceWsportMarkInvoiceOutput.body.mark_invoice_response
        print("\nMark Invoice : \n******************************")
        print("INTL_TXN_ID : ", markInvoiceResponse.request_return.intl_txn_id)
        print("CLIENT_TXN_ID : ", markInvoiceResponse.request_return.client_txn_id)
        print("RETURN_CODE : ", markInvoiceResponse.request_return.return_code)
        print("WARNINGS : ", markInvoiceResponse.request_return.warnings)

    def get_invoice_status(self):
        """E-Fatura sisteminde bulunan bir veya birden fazla taslak, gelen ve giden faturaların durumunu
           sorgulamayı sağlayan servistir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.application_name = "INVOICE"

        getInvoiceStatusRequest = GetInvoiceStatusRequest()
        getInvoiceStatusResponse = GetInvoiceStatusResponse()
        invoice = Invoice()
        invoice.id = "MUH2023000010476"
        invoice.uuid = "a49c19e6-a1f3-48f0-8469-22ef96291d4e"

        getInvoiceStatusRequest.request_header = request_header_type
        getInvoiceStatusRequest.invoice = invoice
        einvoiceWsportGetInvoiceStatusOutput = EinvoiceWsportGetInvoiceStatusOutput()
        einvoiceWsportGetInvoiceStatusOutput = self.send_request(EinvoiceWsportGetInvoiceStatus,
                                                                 EinvoiceWsportGetInvoiceStatusInput,
                                                                 getInvoiceStatusRequest)

        getInvoiceStatusResponse = einvoiceWsportGetInvoiceStatusOutput.body.get_invoice_status_response
        print("\nDurumu Sorgulanan Belge : \n**********************************")
        all_variables = vars(getInvoiceStatusResponse.invoice_status)
        for key, value in all_variables.items():
            print("-\t", key, ":", value)

    def get_invoice_status_all(self):
        """E-Fatura sisteminde bulunan bir veya birden fazla taslak, gelen ve giden faturaların durumunu sorgulamayı
           sağlayan servistir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.application_name = "INVOICE"

        getInvoiceStatusAllRequest = GetInvoiceStatusAllRequest()
        getInvoiceStatusAllResponse = GetInvoiceStatusAllResponse()
        uuid_1 = "a49c19e6-a1f3-48f0-8469-22ef96291d4e"
        uuid_2 = "d51318ab-4862-42f3-8f3c-148ecf5e760e"

        getInvoiceStatusAllRequest.request_header = request_header_type
        getInvoiceStatusAllRequest.uuid = uuid_1, uuid_2
        einvoiceWsportGetInvoiceStatusAllOutput = EinvoiceWsportGetInvoiceStatusAllOutput()
        einvoiceWsportGetInvoiceStatusAllOutput = self.send_request(EinvoiceWsportGetInvoiceStatusAll,
                                                                    EinvoiceWsportGetInvoiceStatusAllInput,
                                                                    getInvoiceStatusAllRequest)

        getInvoiceStatusAllResponse = einvoiceWsportGetInvoiceStatusAllOutput.body.get_invoice_status_all_response
        print("\nDurumu Sorgulanan Belgeler : \n**********************************")
        Count = 1
        for piece in getInvoiceStatusAllResponse.invoice_status:
            print(f"########### {Count}. Belge ###########")
            all_variables = vars(piece)
            for key, value in all_variables.items():
                if key == "header":
                    header_dict = vars(value)
                    for key_1, value_1 in header_dict.items():
                        print("-\t", key_1, ":", value_1)
                else:
                    print("-\t", key, ":", value)
            Count += 1

    def send_invoice_response_with_server_sign(self):
        """E-Fatura sisteminde bulunan bir veya birden fazla gelen ticari faturaya uygulama yanıtı göndermeyi
           sağlayan servistir. verilen id değerleri yanıt bekleyen faturalara ait olmalıdır. aksi halde hata döner."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.application_name = "INVOICE"

        sendInvoiceResponseWithServerSignRequest = SendInvoiceResponseWithServerSignRequest()
        sendInvoiceResponseWithServerSignResponse = SendInvoiceResponseWithServerSignResponse()
        sendInvoiceResponseWithServerSignRequest.request_header = request_header_type
        sendInvoiceResponseWithServerSignRequest.status = "RED"
        sendInvoiceResponseWithServerSignRequest.description = ["Fatura gerekli kontrollerden gecemedi."]
        invoice = Invoice()

        invoice.id = "MUH2023000060670"
        sendInvoiceResponseWithServerSignRequest.invoice = invoice

        einvoiceWsportSendInvoiceResponseWithServerSignOutput = EinvoiceWsportSendInvoiceResponseWithServerSignOutput()
        einvoiceWsportSendInvoiceResponseWithServerSignOutput = self.send_request(
            EinvoiceWsportSendInvoiceResponseWithServerSign,
            EinvoiceWsportSendInvoiceResponseWithServerSignInput,
            sendInvoiceResponseWithServerSignRequest)

        sendInvoiceResponseWithServerSignResponse = einvoiceWsportSendInvoiceResponseWithServerSignOutput.body.send_invoice_response_with_server_sign_response
        print("\nSend Invoice Response With Server Sign : \n**********************************")
        if sendInvoiceResponseWithServerSignResponse.request_return is not None:
            print("INTL_TXN_ID : ", sendInvoiceResponseWithServerSignResponse.request_return.intl_txn_id)
            print("CLIENT_TXN_ID : ", sendInvoiceResponseWithServerSignResponse.request_return.client_txn_id)
            print("RETURN_CODE : ", sendInvoiceResponseWithServerSignResponse.request_return.return_code)
            print("WARNINGS : ", sendInvoiceResponseWithServerSignResponse.request_return.warnings)
        else:
            print("HATA : ", sendInvoiceResponseWithServerSignResponse.error_type.error_short_des)

    def send_request(self, service_name, input_service_name, request_data):
        client = Client.from_service(service_name)
        request = input_service_name(
            body=input_service_name.Body(request_data))
        response = client.send(request)
        return response


einvoice = EInvoiceActions()
# einvoice.SendInvoice()
# einvoice.load_invoice()
# einvoice.get_invoice_scenario_1()
# einvoice.get_invoice_scenario_2()
# einvoice.get_invoice_scenario_3()
# einvoice.get_invoice_scenario_4()
# einvoice.get_invoice_with_type()
# einvoice.mark_invoice()
einvoice.get_invoice_status()
einvoice.get_invoice_status_all()
# einvoice.send_invoice_response_with_server_sign()
