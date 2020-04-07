from flask import jsonify
from flask_restful import Resource

class UserResource(Resource):

    def post(self):
        return jsonify(
            {"ok":"ok"}
        )