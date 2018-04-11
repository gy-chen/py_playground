from . import oauth
from . import jwt


def init_app(app):
    #oauth.init_app(app)
    jwt.init_app(app)
