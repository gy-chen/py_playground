import logging
import random
import string
from flask import Flask, current_app, _app_ctx_stack


class ContextDemo:
    """demonstrate how context works"""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.logger.debug(
            '[*] ContextDemo: init_app. called app.teardown_appcontext.')
        app.teardown_appcontext(self.teardown)

    def get_context_data(self):
        current_app.logger.debug(
            '[*] ContextDemo: fetch data from app context.')
        ctx = _app_ctx_stack.top
        if 'data' not in ctx:
            ctx.data = ''.join(random.choices(string.ascii_uppercase, k=5))
        return ctx.data

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        current_app.logger.debug(
            '[*] ContextDemo: teardown, clear data: ' + str(ctx.__dict__))


context_demo = ContextDemo()


def create_app():
    app = Flask(__name__)

    context_demo.init_app(app)

    @app.route('/')
    def fetch_context_data():
        return context_demo.get_context_data()

    @app.route('/do_nothing')
    def do_nothing():
        return ''

    return app


app = create_app()
