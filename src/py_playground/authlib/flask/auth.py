from authlib.flask.client import OAuth
from authlib.client.apps import register_apps
from flask import g, session
from .models import User, Connect

session_key_login = 'sid'


def login(user):
    session[session_key_login] = user.id
    g.current_user = user


def logout():
    del session[session_key_login]


def get_current_user():
    user = g.get('current_user')
    if user:
        return user

    # retrieve login user by session
    sid = session.get(session_key_login)
    if not sid:
        return None

    user = User.query.get(sid)
    if user is None:
        logout()

    g.current_user = user
    return user


def fetch_token(name):
    user = get_current_user()
    conn = Connect.query.filter_by(
        user_id=user.id, name=name
    ).first()
    return conn.to_dict()


oauth = OAuth(fetch_token=fetch_token)


def init_app(app):
    oauth.init_app(app)
    register_apps(oauth, ['google'])
