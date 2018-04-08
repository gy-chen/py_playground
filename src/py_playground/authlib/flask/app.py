from flask import Flask
from . import auth
from . import routes
from . import config

app = Flask(__name__)


def init_app(app):
    app.config.from_object(config)
    auth.init_app(app)
    routes.init_app(app)


init_app(app)
