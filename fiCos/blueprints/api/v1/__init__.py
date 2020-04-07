from flask import Blueprint
from flask_restful import Api 

from .login.Resources import LoginResource

urlPrefix = '/api/v1'
bpLogin = Blueprint('login', __name__, url_prefix=urlPrefix)

api = Api(bpLogin)

def init_app(app):
    api.add_resource(LoginResource, '/auth')
    app.register_blueprint(bpLogin)
