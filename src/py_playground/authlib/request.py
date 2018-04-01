import webbrowser
from requests_oauthlib import OAuth2Session

client_id = 'REPLACE HERE'
client_secret = 'REPLACE HERE'
redirect_uri = 'http://127.0.0.1:4416'
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'

scope = [
    'profile'
]

api_url = 'https://www.googleapis.com/oauth2/v2/userinfo'

client = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)


def start_flow(api_url):
    """Start OAuth flow

    1. authorization
    2. fetch access token
    3. request API

    :param api_url: the api want to call after user grant the permission
    :return: response of the API
    """
    authorization_url, state = client.authorization_url(authorization_base_url)
    webbrowser.open(authorization_url)
    redirect_response = input('Input redirect url:')
    client.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
    return client.get(api_url)


if __name__ == '__main__':
    response = start_flow(api_url)
    print(response.content)
