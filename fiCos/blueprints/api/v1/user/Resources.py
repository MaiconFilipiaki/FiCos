from flask import jsonify, request, make_response
from flask_restful import Resource
from flasgger import swag_from

from fiCos.ext.database import db
from fiCos.models.User import User, user_share_schema


class UserResource(Resource):

    @swag_from('static/post.yml', methods=['POST'])
    def post(self):
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        if username is None or email is None or password is None:
            return make_response(
                jsonify({"error": "All fields need filled"}),
                400
            )
        
        verifyUserExist = User.query.filter_by(email=email).first()
        if verifyUserExist is not None:
            return make_response(
                jsonify({"error": "E-mail already registered"}),
                400
            )

        user = User(
            username,
            email,
            password
        )

        db.session.add(user)
        db.session.commit()
        result = user_share_schema.dump(
            User.query.filter_by(email=email).first()
        )
        return jsonify(result)
