from com.izibiz.auth import LogoutResponse
from com.izibiz.auth.authentication_ws_wsdl import LoginRequest, LoginResponse, LogoutRequest, \
    AuthenticationServicePortLogout, AuthenticationServicePortLogoutInput, \
    AuthenticationServicePortLogin, AuthenticationServicePortLoginInput, AuthenticationServicePortLoginOutput, \
    AuthenticationServicePortLogoutOutput
from xsdata.formats.dataclass.client import Client
from CreateRequiredDirectory import create_directories


class AuthWSActions:

    def login(self):
        """Web servis istemcisinin(client) özel entegratör platformuna kimlik doğrulayarak giriş yapmasını sağlar."""

        loginRequest = LoginRequest()
        login_response = LoginResponse()
        authenticationServicePortLoginOutput = AuthenticationServicePortLoginOutput()
        loginRequest.user_name = "kullanici adi giriniz"
        loginRequest.password = "sifre giriniz"

        client = Client.from_service(AuthenticationServicePortLogin)
        request = AuthenticationServicePortLoginInput(body=AuthenticationServicePortLoginInput.Body(login_request=loginRequest))
        authenticationServicePortLoginOutput = client.send(request)
        login_response = authenticationServicePortLoginOutput.body.login_response
        session_id = login_response.session_id
        create_directories()

        return session_id

    def logout(self):
        """Web servis istemcisinin özel entegratör platformunda ki oturumu kapatmasını sağlayan servistir."""

        logoutRequest = LogoutRequest()
        logoutResponse = LogoutResponse()
        logoutRequest.session_id = self.login()
        authenticationServicePortLogoutOutput = AuthenticationServicePortLogoutOutput()

        client = Client.from_service(AuthenticationServicePortLogout)
        request = AuthenticationServicePortLogoutInput(
            body=AuthenticationServicePortLogoutInput.Body(logout_request=logoutRequest))
        authenticationServicePortLogoutOutput = client.send(request)

        logoutResponse = authenticationServicePortLogoutOutput.body.logout_response
        return_code = logoutResponse.request_return.return_code


auth: AuthWSActions = AuthWSActions()
auth.login()
auth.logout()
