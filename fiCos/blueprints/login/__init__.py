from flask import Blueprint
from flask_restful import Api 

from .Resources import LoginResource

bpLogin = Blueprint('login', __name__, url_prefix='/api/v1')

api = Api(bpLogin)

def init_app(app):
    api.add_resource(LoginResource, '/auth')
    app.register_blueprint(bpLogin)
