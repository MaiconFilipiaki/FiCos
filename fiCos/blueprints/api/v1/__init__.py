from flask import Blueprint
from flask_restful import Api

from .user.Resources import UserResource
from .login.Resources import LoginResource

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)

api.add_resource(UserResource, '/user')
api.add_resource(LoginResource, '/auth')

def init_app(app):
    app.register_blueprint(api_bp)

