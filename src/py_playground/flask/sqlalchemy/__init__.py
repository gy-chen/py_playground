from flask import _app_ctx_stack
from sqlalchemy import orm


class SQLAlchemy:
    """SQLAlchemy

    demonstrate how flask-sqlalchemy managing session
    """

    def __init__(self, app=None):
        self._app = None
        self.session = self._create_scoped_session()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._app = app

        @app.teardown_appcontext
        def shutdown_session(response_or_exc):
            self.session.remove()
            return response_or_exc

    @staticmethod
    def _create_scoped_session():
        session = orm.sessionmaker()
        return orm.scoped_session(session, scopefunc=_app_ctx_stack.__ident_func__)
