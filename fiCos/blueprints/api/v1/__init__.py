from flask import Blueprint
from flask_restful import Api

from .user.Resources import UserResource
from .login.Resources import LoginResource
from .catalog.Resources import CatalogResource
from .prompt_delivery.Resources import PromptDeliveryResource
from .items.Resources import ItemsResources

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)

api.add_resource(UserResource, '/user', endpoint='user')
api.add_resource(LoginResource, '/auth', endpoint='auth')
api.add_resource(CatalogResource, '/catalog', endpoint='catalog')
api.add_resource(
    PromptDeliveryResource,
    '/prompt_delivery',
    endpoint='prompt_delivery'
)
api.add_resource(
    ItemsResources,
    '/prompt_delivery/<id_prompt_delivery_id>/item',
)


def init_app(app):
    app.register_blueprint(api_bp)
