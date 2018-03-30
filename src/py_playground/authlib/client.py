from authlib.client import OAuthClient

client_id = 'REPLACE HERE'
client_secret = 'REPLACE HERE'
access_token_url = 'REPLACE HERE'
authorize_url = 'REPLACE HERE'

client = OAuthClient(
    client_id=client_id,
    client_secret=client_secret,
    access_token_url=access_token_url,
    authorize_url=authorize_url
)


def generate_redirect_uri(client, redirect_uri):
    """Generate reidrect  uri

        :param client:
        :param redirect_uri:
        :return: (redirect_uri, state)
        """
    return client.generate_authorize_redirect(redirect_uri)
