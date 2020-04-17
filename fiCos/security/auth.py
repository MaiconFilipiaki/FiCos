from functools import wraps
from flask import request, jsonify, current_app, make_response
import jwt

from fiCos.models.models import User


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        
        token = None

        if 'Authorization' in request.headers:
            token = request.headers.get('Authorization')

        if not token:
            return make_response(
                jsonify({'error': 'You dont have permission'}), 401
            )

        if 'Bearer' not in token:
            return make_response(jsonify({'error': 'token malformed'}), 401)

        try:
            token_pure = token.replace('Bearer ', '')
            decoded = jwt.decode(
                token_pure,
                current_app.config.get('SECRET_KEY')
            )
            current_user = User.query.get(decoded['id'])
        except Exception:
            return make_response(jsonify({'error': 'token invalid'}), 401)

        return f(current_user=current_user, *args, **kwargs)

    return wrapper
