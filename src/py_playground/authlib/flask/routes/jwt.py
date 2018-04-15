from flask import Blueprint, url_for, jsonify
from authlib.client.apps import get_app
from ..models import User, Connect
from flask_jwt_simple import JWTManager, jwt_required, create_jwt, get_jwt_identity

bp = Blueprint('jwt', __name__)


def fetch_identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


@bp.route('/auth')
def auth_request_callback():
    app = _get_app()
    callback_uri = url_for('.authenticate_callback', _external=True)
    return app.authorize_redirect(callback_uri)


jwt = JWTManager()


@bp.route('/callback')
def authenticate_callback():
    """Create or  update user, then return jwt token"""
    app = _get_app()
    token = app.authorize_access_token()
    user_info = app.profile()
    user = User.get_or_create(user_info)
    token['sub'] = user_info['sub']
    Connect.create_token('google', token, user)
    return create_jwt(user.id)


@bp.route('/profile')
@jwt_required
def profile():
    identity = get_jwt_identity()
    user = fetch_identity({'identity': identity})
    return jsonify(user.to_dict())


def _get_app():
    return get_app('google')


def init_app(app):
    app.config.setdefault('JWT_SECRET_KEY', 'monshin4413')
    jwt.init_app(app)
    app.register_blueprint(bp)
