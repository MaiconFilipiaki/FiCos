from flask import jsonify
from flask_restful import Resource


from fiCos.security.auth import jwt_required


class CatalogResource(Resource):
    @jwt_required
    def get(self, current_user):
        return jsonify({"ok": "ok"})
