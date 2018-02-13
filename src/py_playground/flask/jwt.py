from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config[
    'JWT_SECRET_KEY'] = b'\x8b\xa8\x98oCa\xd1k\x8bU\xd2\xd5?\xf9\xae\xbc\xfa\xef\xfcV\\\x8e\x0e?\xa9\xc3w6G\x1b\xb9\x8a'
jwt = JWTManager(app)


@app.route('/get_jwt', methods=['POST'])
def get_jwt_token():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    identity = request.json.get('identity', None)
    if identity is None:
        return jsonify({"msg": "Missing identity parameter"}), 400

    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@app.route('/required_jwt')
@jwt_required
def required_jwt_token():
    identity = get_jwt_identity()
    return jsonify(identity=identity)


if __name__ == '__main__':
    app.run()
