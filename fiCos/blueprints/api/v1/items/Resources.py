from flask import request, jsonify, make_response
from flask_restful import Resource

from fiCos.ext.database import db
from fiCos.security.auth import jwt_required

from fiCos.models.models import Item, PromptDelivery
from fiCos.models.schemas import item_share_schema


class ItemsResources(Resource):

    @jwt_required
    def post(self, current_user, id_prompt_delivery_id):
        description = request.json.get('description')
        price = request.json.get('price')
        findPromptDelivery = PromptDelivery.query.filter_by(
            id=id_prompt_delivery_id
            ).first()
        if description is None or price is None:
            return jsonify({
                "error": "You need to fill field name"
            }), 400
        if findPromptDelivery is None:
            return make_response(
                jsonify({'error': 'Prompt delivery not found'}),
                404
            )
        new_item = Item(
            description=description,
            price=price
        )
        findPromptDelivery.items.append(new_item)
        db.session.add(new_item)
        db.session.flush()
        id_item = new_item.id
        db.session.commit()
        result = item_share_schema.dump(
            Item.query.filter_by(id=id_item).first()
        )
        return make_response(
            jsonify(result),
            201
        )

    @jwt_required
    def get(self, current_user, id_prompt_delivery_id):
        id = request.args.get('id')
        if id is None:
            return make_response(
                jsonify({'error': 'You need to inform an id'}),
                400
            )
        result = item_share_schema.dump(
            Item.query.filter_by(id=id).first()
        )
        if bool(result) is False:
            return make_response(
                jsonify({'error': 'item not found'}),
                404
            )
        return jsonify(result)

    @jwt_required
    def delete(self, current_user, id_prompt_delivery_id):
        id = request.args.get('id')
        if id is None:
            return make_response(
                jsonify({'error': 'You need to inform an id'}),
                400
            )
        result = Item.query.filter_by(id=id).first()
        if bool(result) is False:
            return make_response(
                jsonify({'error': 'Item not found'}),
                404
            )
        db.session.delete(result)
        db.session.commit()
        return jsonify({"msg": "Item deleted with success"})

    @jwt_required
    def put(self, current_user, id_prompt_delivery_id):
        id = request.args.get('id')
        description = request.json.get('description')
        price = request.json.get('price')
        if description is None or price is None or id is None:
            return make_response(
                jsonify({
                    "error": "You need to fill all field"
                }), 400
            )
        result = Item.query.filter_by(id=id).first()
        if result is None:
            return make_response(
                jsonify({
                    "error": "Item not found"
                }), 404
            )
        result.description = description
        result.price = price
        db.session.commit()
        result = item_share_schema.dump(
            Item.query.filter_by(id=id).first()
        )
        return jsonify(result)
