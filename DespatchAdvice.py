import time


from datetime import datetime, timedelta
from Tools import Tools
from Authorization import AuthWSActions
from xsdata.formats.dataclass.client import Client
from datetime import datetime
from Variables import Variable
from com.izibiz.despatch_advice import RequestHeadertype, SendDespatchAdviceRequest, SendReceiptAdviceRequest, \
    Despatchadvice, EirsaliyeServicePortSendDespatchAdviceOutput, EirsaliyeServicePortSendDespatchAdvice, \
    EirsaliyeServicePortSendDespatchAdviceInput, LoadDespatchAdviceRequest, LoadReceiptAdviceRequest, \
    EirsaliyeServicePortLoadDespatchAdviceOutput, EirsaliyeServicePortLoadDespatchAdvice, \
    EirsaliyeServicePortLoadDespatchAdviceInput, GetDespatchAdviceRequest, EirsaliyeServicePortGetDespatchAdviceOutput, \
    EirsaliyeServicePortGetDespatchAdvice, EirsaliyeServicePortGetDespatchAdviceInput, LoadDespatchAdviceResponse, \
    GetDespatchAdviceResponse, GetDespatchAdviceStatusRequest, Despatchadviceinfo, \
    EirsaliyeServicePortGetDespatchAdviceStatusOutput, EirsaliyeServicePortGetDespatchAdviceStatus, \
    EirsaliyeServicePortGetDespatchAdviceStatusInput, GetDespatchAdviceStatusResponse, \
    EirsaliyeServicePortGetDespatchAdviceWithStatusOutput, EirsaliyeServicePortGetDespatchAdviceWithStatus, \
    EirsaliyeServicePortGetDespatchAdviceWithStatusInput, GetDespatchAdviceWithStatusRequest, \
    GetDespatchAdviceWithStatusResponse, EirsaliyeServicePortSendDespatchResponseOutput, \
    EirsaliyeServicePortSendDespatchResponse, EirsaliyeServicePortSendDespatchResponseInput, \
    SendDespatchResponseRequest, SendDespatchResponseResponse, DespatchResponseStatus


class DespatchAdviceActions:
    """E-Fatura mükellefi olmayan firma veya nihai tüketiciye düzenlenen faturaların özel entegratör
       sistemine gönderilmesi ve raporlamasını sağlayan webservis uygulamasıdır."""

    authWSActions = AuthWSActions()
    session_id = authWSActions.login()
    tools = Tools()
    variables = Variable()

    def send_despatch_advice(self):
        """E-İrsaliye Platformu üzerinden 1 ya da daha fazla e-irsaliyeyi GIB E-İrsaliye sistemine gönderir."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "N"
        sendDespatchAdviceRequest = SendDespatchAdviceRequest()
        sendReceiptAdviceRequest = SendReceiptAdviceRequest()
        sendDespatchAdviceRequest.request_header = request_header_type
        sender = SendDespatchAdviceRequest.Sender()
        sender.vkn = "4840847211"
        sender.alias = "urn:mail:defaultgb@izibiz.com.tr"
        receiver = SendDespatchAdviceRequest.Receiver()
        receiver.vkn = "4840847211"
        receiver.alias = "urn:mail:defaultpk@izibiz.com.tr"
        sendDespatchAdviceRequest.sender = sender
        sendDespatchAdviceRequest.receiver = receiver
        despatchadvice = Despatchadvice()
        data_base64, random_uuid = self.tools.set_loading_content_noZip(Variable.DESPATCHADVICE)
        despatchadvice.content = data_base64
        sendDespatchAdviceRequest.despatchadvice = despatchadvice

        eirsaliyeServicePortSendDespatchAdviceOutput = EirsaliyeServicePortSendDespatchAdviceOutput()
        eirsaliyeServicePortSendDespatchAdviceOutput = self.send_request(EirsaliyeServicePortSendDespatchAdvice,
                                                                         EirsaliyeServicePortSendDespatchAdviceInput,
                                                                         sendDespatchAdviceRequest)

        sendDespatchAdviceResponse = eirsaliyeServicePortSendDespatchAdviceOutput.body.send_despatch_advice_response
        print("\nE-Irsaliye Gonderme Islemine Ait Bilgiler : \n**********************************")
        self.tools.display_response_body(sendDespatchAdviceResponse)

    def load_despatch_archice(self):
        """Özel entegratör platformu üzerinden 1 yada daha fazla irsaliyeyi SİSTEME yükler."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "N"
        loadDespatchAdviceRequest = LoadDespatchAdviceRequest()
        loadDespatchAdviceResponse = LoadDespatchAdviceResponse()
        loadDespatchAdviceRequest.request_header = request_header_type
        despatchadvice = Despatchadvice()
        despatchadvice.id = "DMY20231108115758"
        despatchadvice.uuid = "c226e008-73d9-4d0f-9ca6-8ec30d91134e"
        data_base64, random_uuid = self.tools.set_loading_content_noZip(Variable.DESPATCHADVICE)
        despatchadvice.content = data_base64
        loadDespatchAdviceRequest.despatchadvice = despatchadvice

        eirsaliyeServicePortLoadDespatchAdviceOutput = EirsaliyeServicePortLoadDespatchAdviceOutput()
        eirsaliyeServicePortLoadDespatchAdviceOutput = self.send_request(EirsaliyeServicePortLoadDespatchAdvice,
                                                                         EirsaliyeServicePortLoadDespatchAdviceInput,
                                                                         loadDespatchAdviceRequest)

        loadDespatchAdviceResponse = eirsaliyeServicePortLoadDespatchAdviceOutput.body.load_despatch_advice_response
        print("\nE-Irsaliye Yukleme Islemine Ait Bilgiler : \n**********************************")
        self.tools.display_response_body(loadDespatchAdviceResponse)


    def get_despatch_advice(self):
        """E-İrsaliye sisteminden giden imzalı irsaliye veya gelen irsaliyeyi ERP/muhasebe paketine çekmek için kullanılır.
           bu metotda çekme işlemi tarih aralığına göre ve otomotik olarak son 15 günlük zamana göre yapılmaktadır."""

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "Y"

        getDespatchAdviceRequest = GetDespatchAdviceRequest()
        getDespatchAdviceResponse = GetDespatchAdviceResponse()

        getDespatchAdviceRequest.request_header = request_header_type
        searc_key = GetDespatchAdviceRequest.SearchKey()
        searc_key.limit = 50
        today = datetime.now()
        fifteen_days_ago = today - timedelta(days=15)
        searc_key.start_date = fifteen_days_ago.strftime("%Y-%m-%d")
        searc_key.end_date = today.strftime("%Y-%m-%d")
        searc_key.read_included = "N"
        searc_key.direction = "OUT"
        getDespatchAdviceRequest.search_key = searc_key
        getDespatchAdviceRequest.header_only = "N"

        eirsaliyeServicePortGetDespatchAdviceOutput = EirsaliyeServicePortGetDespatchAdviceOutput()
        eirsaliyeServicePortGetDespatchAdviceOutput = self.send_request(EirsaliyeServicePortGetDespatchAdvice,
                                                                        EirsaliyeServicePortGetDespatchAdviceInput,
                                                                        getDespatchAdviceRequest)

        getDespatchAdviceResponse = eirsaliyeServicePortGetDespatchAdviceOutput.body.get_despatch_advice_response
        print("\nE-Irsaliye Okuma Islemine Ait Bilgiler : \n**********************************")
        self.tools.display_response_body_for_getMethods(getDespatchAdviceResponse,"get_despatch_advice")

    def get_despatch_advice_with_status(self):

        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        getDespatchAdviceWithStatusRequest = GetDespatchAdviceWithStatusRequest()
        getDespatchAdviceWithStatusResponse = GetDespatchAdviceWithStatusResponse()

        search_key = GetDespatchAdviceWithStatusRequest.SearchKey()
        search_key.uuid = "197a8790-bf12-4964-9c0d-ccda420cca10"
        search_key.direction = "IN"
        search_key.read_included = True
        getDespatchAdviceWithStatusRequest.request_header = request_header_type
        getDespatchAdviceWithStatusRequest.search_key = search_key
        getDespatchAdviceWithStatusRequest.header_only = "Y"

        eirsaliyeServicePortGetDespatchAdviceWithStatusOutput = EirsaliyeServicePortGetDespatchAdviceWithStatusOutput()
        eirsaliyeServicePortGetDespatchAdviceWithStatusOutput = self.send_request(
            EirsaliyeServicePortGetDespatchAdviceWithStatus,
            EirsaliyeServicePortGetDespatchAdviceWithStatusInput,
            getDespatchAdviceWithStatusRequest)

        getDespatchAdviceWithStatusResponse = eirsaliyeServicePortGetDespatchAdviceWithStatusOutput.body.get_despatch_advice_with_status_response
        print("\nE-Irsaliye Durum Sorgulama Islemine Ait Bilgiler : \n**********************************")
        self.tools.display_response_body_for_getMethods(getDespatchAdviceWithStatusResponse, "get_despatch_advice_with_status")

    def send_despatch_response(self):
        request_header_type = RequestHeadertype()
        request_header_type.session_id = self.session_id
        request_header_type.compressed = "Y"

        sendDespatchResponseRequest = SendDespatchResponseRequest()
        despatchadvice = Despatchadvice()
        despatchadvice.id = "MUH2023000092818"
        despatchadvice.uuid = "3d1e7d99-2bb5-4c1b-8382-9e3526d6596f"
        despatchadvice.direction = "IN"

        sendDespatchResponseRequest.request_header = request_header_type
        sendDespatchResponseRequest.despatchadvice = despatchadvice
        sendDespatchResponseRequest.status = DespatchResponseStatus.RED
        sendDespatchResponseRequest.description = "Red edildi"

        sendDespatchResponseResponse = SendDespatchResponseResponse()

        eirsaliyeServicePortSendDespatchResponseOutput = EirsaliyeServicePortSendDespatchResponseOutput()
        eirsaliyeServicePortSendDespatchResponseOutput = self.send_request(EirsaliyeServicePortSendDespatchResponse,
                                                                           EirsaliyeServicePortSendDespatchResponseInput,
                                                                           sendDespatchResponseRequest)

        sendDespatchResponseResponse = eirsaliyeServicePortSendDespatchResponseOutput.body.send_despatch_response_response
        print("\nE-Irsaliye Yanitlama Islemine Ait Bilgiler : \n**********************************")
        print(eirsaliyeServicePortSendDespatchResponseOutput)
    def send_request(self, service_name, input_service_name, request_data):
        client = Client.from_service(service_name)
        request = input_service_name(
            body=input_service_name.Body(request_data))
        response = client.send(request)
        return response


despatchAdviceActions = DespatchAdviceActions()
# despatchAdviceActions.send_despatch_advice()
# despatchAdviceActions.load_despatch_archice()
# despatchAdviceActions.get_despatch_advice()
despatchAdviceActions.get_despatch_advice_with_status()
# despatchAdviceActions.send_despatch_response()
