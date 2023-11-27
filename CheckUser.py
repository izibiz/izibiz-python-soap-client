from Authorization import AuthWSActions
from com.izibiz.auth import RequestHeadertype, CheckUserRequest, Gibuser, CheckUserResponse
from com.izibiz.auth.authentication_ws_wsdl import AuthenticationServicePortCheckUser, \
    AuthenticationServicePortCheckUserInput, AuthenticationServicePortCheckUserOutput
from xsdata.formats.dataclass.client import Client
from Tools import Tools


class CheckUserActions:
    """Mükellefin, Gelir İdaresi Başkanlığı sistemine kayıtlı olup olmadığının kontrol edildiği servistir."""

    def __init__(self):
        self.authWSActions = AuthWSActions()
        self.tools = Tools()

    def check_user(self):
        request_header_type = RequestHeadertype()
        checkUserRequest = CheckUserRequest()
        checkUserResponse = CheckUserResponse()
        gibUser = Gibuser()
        request_header_type.session_id = self.authWSActions.login()
        gibUser.identifier = "2090135146"
        gibUser.document_type = "INVOICE"
        checkUserRequest.request_header = request_header_type
        checkUserRequest.user = gibUser

        authenticationServicePortCheckUserOutput = AuthenticationServicePortCheckUserOutput()
        client = Client.from_service(AuthenticationServicePortCheckUser)
        request = AuthenticationServicePortCheckUserInput(
            body=AuthenticationServicePortCheckUserInput.Body(check_user_request=checkUserRequest))

        authenticationServicePortCheckUserOutput = client.send(request)
        checkUserResponse = authenticationServicePortCheckUserOutput.body.check_user_response
        expected_user = checkUserResponse.user
        user = expected_user[0]

        print("Sorgulanan Hesap Bilgileri : ")
        print("**********************************************")
        print("ACCOUNT_TYPE:", user.account_type)
        print("ALIAS:", user.alias)
        print("ALIAS_CREATION_TIME:", user.alias_creation_time)
        print("ALIAS_DELETION_TIME:", user.alias_deletion_time)
        print("DELETED:", user.deleted)
        print("DOCUMENT_TYPE:", user.document_type)
        print("IDENTIFIER:", user.identifier)
        print("REGISTER_TIME", user.register_time)
        print("TITLE:", user.title)
        print("TYPE_VALUE:", user.type_value)
        print("UNIT:", user.unit)


check_user_actions = CheckUserActions()
check_user_actions.check_user()
