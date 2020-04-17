from flask import jsonify, request, make_response
from flask_restful import Resource

from fiCos.security.auth import jwt_required

from fiCos.ext.database import db
from fiCos.models.models import Item
from fiCos.models.models import PromptDelivery
from fiCos.models.schemas import prompt_delivery_share_schema


class PromptDeliveryResource(Resource):

    @jwt_required
    def post(self, current_user):
        print(request)
        name = request.json.get('name')
        items = request.json.get('items')
        if name is None:
            return jsonify({
                "error": "You need to fill field name"
            }), 400
        if items is None or len(items) == 0:
            return jsonify({
                "error": "You need to add some item in prompt delivery"
            }), 400
        items_for_save = []
        for item in items:
            description = item['description']
            price = item['price']
            if description is None or price is None:
                db.session.rollback()
                db.session.close()
                return jsonify({
                    "error": "You need to fill all fields"
                }), 400
            item = Item(description=description, price=price)
            db.session.add(item)
            items_for_save.append(item)

        promptDelivery = PromptDelivery(
            name=name,
            items=items_for_save,
            user_id=current_user.id
        )
        db.session.add(promptDelivery)
        db.session.flush()
        idPromptDelivery = promptDelivery.id
        db.session.commit()
        result = prompt_delivery_share_schema.dump(
            PromptDelivery.query.filter_by(id=idPromptDelivery)
        )
        return make_response(
            jsonify({'promptDelivery': result}),
            201
        )
