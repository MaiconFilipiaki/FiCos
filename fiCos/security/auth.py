from functools import wraps

import jwt
from flask  import request, jsonify, current_app, make_response

from fiCos.models.User import User

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        
        token = None

        if 'Authorization' in request.headers:
            token = request.headers.get('Authorization')

        if not token:
            return make_response(jsonify({ 'error': 'You dont have permission' }), 401)

        if not 'Bearer' in token:
            return make_response(jsonify({ 'error': 'token malformed' }), 401)

        try:
            token_pure = token.replace('Bearer ', '')
            decoded = jwt.decode(token_pure, current_app.config.get('SECRET_KEY'))
            current_user = User.query.get(decoded['id'])
        except:
            return make_response(jsonify({ 'error': 'token invalid' }), 401)

        return f(current_user=current_user, *args, **kwargs)

    return wrapper
