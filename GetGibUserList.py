from xsdata.models.datatype import XmlDateTime
from com.izibiz.auth import GetGibUserListRequest, RequestHeadertype, AliasType, Gibuser, GetGibUserListResponse
from com.izibiz.auth.authentication_ws_wsdl import AuthenticationServicePortGetGibUserList, \
    AuthenticationServicePortGetGibUserListInput, AuthenticationServicePortGetGibUserListOutput
from xsdata.formats.dataclass.client import Client
from Tools import Tools
from Authorization import AuthWSActions
from Variables import Variable


class GetGibUserListActions:
    """E-Fatura ve E-İrsaliye sistemine kayıtlı firmalara ait GB/PK etiketlerinin
       sıkıştırılmış olarak istenilen tipte dönüldüğü servistir."""

    def __init__(self):
        self.authWSActions = AuthWSActions()
        self.tools = Tools()
        self.variable = Variable()

    def get_gib_user_list_scenario_1(self):
        """DOCUMENT : ALL, ALIAS : PK senaryosu"""

        session_id = self.authWSActions.login()
        request_header_type = RequestHeadertype()
        request_header_type.session_id = session_id
        gib_user = Gibuser()
        gib_user.document_type = "ALL"

        getGibUserListRequest = GetGibUserListRequest()
        getGibUserListRequest.alias_type = AliasType.PK
        getGibUserListRequest.request_header = request_header_type
        getGibUserListRequest.document_type = gib_user.document_type
        self.send_request(getGibUserListRequest, 1)

    def get_gib_user_list_scenario_2(self):
        """DOCUMENT : ALL, ALIAS : ALL senaryosu"""

        session_id = self.authWSActions.login()
        request_header_type = RequestHeadertype()
        request_header_type.session_id = session_id
        gib_user = Gibuser()
        gib_user.document_type = "ALL"

        getGibUserListRequest = GetGibUserListRequest()
        getGibUserListRequest.alias_type = AliasType.ALL
        getGibUserListRequest.request_header = request_header_type
        getGibUserListRequest.document_type = gib_user.document_type
        self.send_request(getGibUserListRequest, 2)

    def get_gib_user_list_scenario_3(self):
        """DOCUMENT : INVOICE, ALIAS : PK senaryosu"""

        session_id = self.authWSActions.login()
        request_header_type = RequestHeadertype()
        request_header_type.session_id = session_id
        gib_user = Gibuser()
        gib_user.document_type = "INVOICE"

        getGibUserListRequest = GetGibUserListRequest()
        getGibUserListRequest.alias_type = AliasType.PK
        getGibUserListRequest.request_header = request_header_type
        getGibUserListRequest.document_type = gib_user.document_type
        self.send_request(getGibUserListRequest, 3)

    def get_gib_user_list_scenario_4(self):
        """DOCUMENT : ALL, ALIAS : ALL, ALIAS_MODIFY: 2019-12-01 senaryosu"""

        session_id = self.authWSActions.login()
        request_header_type = RequestHeadertype()
        request_header_type.session_id = session_id
        gib_user = Gibuser()
        gib_user.document_type = "ALL"

        getGibUserListRequest = GetGibUserListRequest()
        getGibUserListRequest.alias_type = AliasType.ALL
        xmlDateTime = XmlDateTime(year=2019, month=12, day=1, minute=1, second=1, hour=1)
        getGibUserListRequest.alias_modify_date = xmlDateTime
        getGibUserListRequest.request_header = request_header_type
        getGibUserListRequest.document_type = gib_user.document_type
        self.send_request(getGibUserListRequest, 4)

    def get_gib_user_list_scenario_5(self):
        """DOCUMENT : ALL, ALIAS : ALL, ALIAS_MODIFY: 2019-12-01, REGISTER_TIME: 2013-12-01 senaryosu"""

        session_id = self.authWSActions.login()
        request_header_type = RequestHeadertype()
        request_header_type.session_id = session_id
        gib_user = Gibuser()
        gib_user.document_type = "ALL"

        getGibUserListRequest = GetGibUserListRequest()
        getGibUserListRequest.alias_type = AliasType.ALL
        xmlDateTime = XmlDateTime(year=2019, month=12, day=1, minute=1, second=1, hour=1)
        xmlDateTime_1 = XmlDateTime(year=2013, month=12, day=1, minute=1, second=1, hour=1)
        getGibUserListRequest.alias_modify_date = xmlDateTime
        getGibUserListRequest.register_time_start = xmlDateTime_1
        getGibUserListRequest.request_header = request_header_type
        getGibUserListRequest.document_type = gib_user.document_type
        self.send_request(getGibUserListRequest, 5)

    def send_request(self, getGibUserListRequest, scenario):
        getGibUserListResponse = GetGibUserListResponse()
        authenticationServicePortGetGibUserListOutput = AuthenticationServicePortGetGibUserListOutput()

        client = Client.from_service(AuthenticationServicePortGetGibUserList)
        request = AuthenticationServicePortGetGibUserListInput(
            body=AuthenticationServicePortGetGibUserListInput.Body(get_gib_user_list_request=getGibUserListRequest))
        authenticationServicePortGetGibUserListOutput = client.send(request)
        getGibUserListResponse = authenticationServicePortGetGibUserListOutput.body.get_gib_user_list_response
        data = getGibUserListResponse.content.value

        self.tools.write_content_to_zip(data, self.variable.GETGIBUSERLIST, scenario)
        self.tools.display_user_from_zipfle(scenario)


my_instance = GetGibUserListActions()
my_instance.get_gib_user_list_scenario_1()
my_instance.get_gib_user_list_scenario_2()
my_instance.get_gib_user_list_scenario_3()
my_instance.get_gib_user_list_scenario_4()
my_instance.get_gib_user_list_scenario_5()
