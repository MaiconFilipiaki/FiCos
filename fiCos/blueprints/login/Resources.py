import os
from flask import jsonify
from flask_restful import Resource
from flasgger import swag_from

from fiCos.models.User import User
from fiCos.ext.database import db

class LoginResource(Resource):
    @swag_from('static/username_specs.yml', methods=['GET'])
    def get(self):
        # print(os.chdir())
        return jsonify(
            {"ok":"ok"}
        )

    def post(self):
        user = User(id=1, name='maicon', email='mdfilipiaki@gmail.com')
        db.session.add(user)
        db.session.commit()
        return jsonify(
            {"ok":"ok"}
        )