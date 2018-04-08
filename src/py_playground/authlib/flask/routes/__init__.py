from . import oauth


def init_app(app):
    oauth.init_app(app)
