from flask import Flask
from . import auth
from . import models
from . import routes
from . import config

app = Flask(__name__)


def init_app(app):
    app.config.from_object(config)
    models.init_app(app)
    auth.init_app(app)
    routes.init_app(app)


init_app(app)
