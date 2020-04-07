import os
from flask import jsonify
from flask_restful import Resource
from flasgger import swag_from, Schema, fields

from fiCos.models.User import User
from fiCos.ext.database import db

class Palette(Schema):
    pallete_name = fields.Str()

class LoginResource(Resource):

    @swag_from('static/username_specs.yml', methods=['POST'])
    def post(self):
        return jsonify(
            {"ok":"ok"}
        )