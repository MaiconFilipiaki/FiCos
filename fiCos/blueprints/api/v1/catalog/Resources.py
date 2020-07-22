from flask import jsonify, request
from sqlalchemy.sql.functions import func
from sqlalchemy.sql import text
from flask_restful import Resource

from fiCos.ext.database import db
from fiCos.models.models import PromptDelivery, Item

from fiCos.security.auth import jwt_required
from fiCos.models.schemas import prompt_delivery_share_schema, prompt_delivery_share_schemas, item_share_schemas


class CatalogResource(Resource):
    def get(self):
        lat = request.args.get('lat')
        lon = request.args.get('long')
        result = item_share_schemas.dump(
            db.session.query(Item).from_statement(
                text(
                    f'SELECT item.id, item.description, item.price, item.prompt_delivery_id, item.length_img'\
                    f',(6371 * acos(cos(radians({lat})) * cos(radians(latitude)) * cos(radians({lon})'\
                    f' - radians(longitude)) + sin(radians({lat})) * sin(radians(latitude)))) AS reach FROM '\
                    ' prompt_delivery, item where item.prompt_delivery_id = prompt_delivery.id HAVING reach <= 5;'
                )
            )
        )
        return jsonify(result)
