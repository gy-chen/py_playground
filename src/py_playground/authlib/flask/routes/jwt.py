from flask import Blueprint, url_for, jsonify
from authlib.client.apps import get_app
from ..models import User, Connect
from flask_jwt import JWT, jwt_required, current_identity, _default_jwt_encode_handler

bp = Blueprint('jwt', __name__)


def fetch_identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


@bp.route('/auth')
def auth_request_callback():
    app = _get_app()
    callback_uri = url_for('.authenticate_callback', _external=True)
    return app.authorize_redirect(callback_uri)


jwt = JWT(identity_handler=fetch_identity)


@bp.route('/callback')
def authenticate_callback():
    """Create or  update user, then return jwt token"""
    app = _get_app()
    token = app.authorize_access_token()
    user_info = app.profile()
    user = User.get_or_create(user_info)
    token['sub'] = user_info['sub']
    Connect.create_token('google', token, user)
    return _default_jwt_encode_handler(user)


@bp.route('/profile')
@jwt_required()
def profile():
    user = current_identity
    return jsonify(user.to_dict())


def _get_app():
    return get_app('google')


def init_app(app):
    app.config['JWT_AUTH_URL_RULE'] = app.config.get('JWT_AUTH_URL_RULE', None)
    jwt.init_app(app)
    app.register_blueprint(bp)
