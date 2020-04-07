from flask import jsonify
from flask_restful import Resource
from flasgger import swag_from

class LoginResource(Resource):

    @swag_from('static/username_specs.yml', methods=['POST'])
    def post(self):
        return jsonify(
            {"ok":"ok"}
        )