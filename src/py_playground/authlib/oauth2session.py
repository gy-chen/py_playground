import os
from authlib.client import OAuth2Session

client_id = os.getenv('GITHUB_CLIENT_ID')
client_secret = os.getenv('GITHUB_CLIENT_SECRET')
scope = 'user:email'

session = OAuth2Session(client_id, client_secret, scope=scope)

# 1. redirect to authorization endpoint
authorize_url = 'https://github.com/login/oauth/authorize'
uri, state = session.authorization_url(authorize_url)
print('GitHub authorize uri and state: {}, {}'.format(uri, state))

# 2. fetch access token
access_token_url = 'https://github.com/login/oauth/access_token'
authorize_code = os.getenv('GITHUB_CODE')
if authorize_code:
    token = session.fetch_access_token(access_token_url, code=authorize_code)
    print('fetched access token: {}'.format(token))
