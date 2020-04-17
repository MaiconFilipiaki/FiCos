from flask import jsonify, request, current_app
from flask_restful import Resource
from flasgger import swag_from

import datetime
import jwt

from fiCos.models.models import User


class LoginResource(Resource):

    @swag_from('static/post.yml', methods=['POST'])
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        user = User.query.filter_by(email=email).first_or_404()

        if not user.verify_password(password):
            return jsonify({
                "error": "credentials are not correct"
            }), 403

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        token = jwt.encode(payload, current_app.config.get('SECRET_KEY'))

        return jsonify({"token": token.decode('utf-8')})
