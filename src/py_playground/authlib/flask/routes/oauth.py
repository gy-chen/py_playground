from flask import Blueprint, url_for, redirect, g, jsonify
from authlib.client.apps import get_app

bp = Blueprint('oauth', __name__)


@bp.route('/auth')
def auth():
    """Step 1: redirect to auth url

    :return:
    """
    app = _get_app()
    callback_uri = url_for('.callback', _external=True)
    return app.authorize_redirect(callback_uri)


@bp.route('/callback')
def callback():
    """Get response from auth provider

    :return:
    """
    app = _get_app()
    app.authorize_access_token()
    return redirect(url_for('.profile'))


@bp.route('/profile')
def profile():
    """Get profile of user from auth provider

    :return:
    """
    app = _get_app()
    user_info = app.profile()
    return jsonify(dict(user_info))


def _get_app():
    return get_app('google')


def init_app(app):
    app.register_blueprint(bp)
