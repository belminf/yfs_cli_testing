from rauth import OAuth2Service
import json


class OauthException(Exception):
    pass


class YahooOauth:
    request_auth_url = 'https://api.login.yahoo.com/oauth2/request_auth'
    get_token_url = 'https://api.login.yahoo.com/oauth2/get_token'

    oauth_service = None
    oauth_session = None

    def __init__(self, client_id, client_secret, base_url=None, access_token=None):
        self.oauth_service = OAuth2Service(
            name='yahoo',
            base_url=base_url,
            client_id=client_id,
            client_secret=client_secret,
            authorize_url=self.request_auth_url,
            access_token_url=self.get_token_url
        )

        if access_token:
            self.oauth_session = self.oauth_service.get_session(access_token)

    def get_session(self):
        return self.oauth_session

    def auth_session(self, verify_code, callback_url):

        if verify_code:
            self.oauth_session = self.oauth_service.get_auth_session(
                data={
                    'code': verify_code,
                    'grant_type': 'authorization_code',
                    'redirect_uri': callback_url,
                },
                decoder=json.loads
            )

    def get_auth_config(self):
        return {
            'access_token': self.oauth_session.access_token,
            'client_id': self.oauth_session.client_id,
            'client_secret': self.oauth_session.client_secret,
            'base_url': self.oauth_service.base_url,
        }

    def get_auth_url(self, callback_url):

        return self.oauth_service.get_authorize_url(
            redirect_uri=callback_url,
            response_type='code'
        )

    def get(self, URL):
        response = self.oauth_session.get(URL, params={'format': 'json'})

        # Return a specific error for auth
        if response.status_code == 401:
            raise OauthException('Authentication error')

        # ASSERT: Not 401 status code

        return response
