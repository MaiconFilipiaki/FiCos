from flask import jsonify, request, make_response
from flask_restful import Resource
from flasgger import swag_from

from fiCos.security.auth import jwt_required

from fiCos.ext.database import db
from fiCos.models.models import PromptDelivery
from fiCos.models.schemas import prompt_delivery_share_schema, prompt_delivery_share_schemas


class PromptDeliveryResource(Resource):

    @jwt_required
    @swag_from('static/post.yml', methods=['POST'])
    def post(self, current_user):
        name = request.json.get('name')
        items = request.json.get('items')
        if name is None:
            return jsonify({
                "error": "You need to fill field name"
            }), 400
        # items_for_save = []
        # for item in items:
        #     description = item['description']
        #     price = item['price']
        #     if description is None or price is None:
        #         db.session.rollback()
        #         db.session.close()
        #         return jsonify({
        #             "error": "You need to fill all fields"
        #         }), 400
        #     item = Item(description=description, price=price)
        #     db.session.add(item)
        #     items_for_save.append(item)

        promptDelivery = PromptDelivery(
            name=name,
            items=[],
            user_id=current_user.id
        )
        db.session.add(promptDelivery)
        db.session.flush()
        idPromptDelivery = promptDelivery.id
        db.session.commit()
        result = prompt_delivery_share_schema.dump(
            PromptDelivery.query.filter_by(id=idPromptDelivery).first()
        )
        return make_response(
            jsonify(result),
            201
        )

    @jwt_required
    def put(self, current_user):
        id = request.args.get('id')
        name = request.json.get('name')
        latitude = request.json.get('latitude')
        longitude = request.json.get('longitude')
        reach = request.json.get('reach')
        if name is None or id is None or latitude is None or longitude is None or reach is None:
            return make_response(
                jsonify({
                    "error": "You need to fill all field"
                }), 400
            )
        result = PromptDelivery.query.filter_by(id=id).first()
        if result is None:
            return make_response(
                jsonify({
                    "error": "prompt delivery not found"
                }), 404
            )
        result.name = name
        result.latitude = latitude
        result.longitude = longitude
        result.reach = reach
        db.session.commit()
        result = prompt_delivery_share_schema.dump(
            PromptDelivery.query.filter_by(id=id).first()
        )
        return jsonify(result)

    @jwt_required
    def delete(self, current_user):
        id = request.args.get('id')
        if id is None:
            return make_response(
                jsonify({'error': 'You need to inform an id'}),
                400
            )
        result = PromptDelivery.query.filter_by(id=id).first()
        if bool(result) is False:
            return make_response(
                jsonify({'error': 'prompt delivery not found'}),
                404
            )
        db.session.delete(result)
        db.session.commit()
        return jsonify({"msg": "Prompt delivery deleted with success"})

    @jwt_required
    @swag_from('static/get.yml', methods=['GET'])
    def get(self, current_user):
        id = request.args.get('id')
        if id is None:
            result = prompt_delivery_share_schemas.dump(
                PromptDelivery.query.filter_by(user_id=current_user.id)
            )
            return jsonify(result)
        result = prompt_delivery_share_schema.dump(
            PromptDelivery.query.filter_by(id=id).first()
        )
        if bool(result) is False:
            return make_response(
                jsonify({'error': 'prompt delivery not found'}),
                404
            )
        return jsonify(result)
