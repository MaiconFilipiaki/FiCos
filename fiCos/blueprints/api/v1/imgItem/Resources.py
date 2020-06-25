import os
from flask import request, current_app, make_response, jsonify, send_file, send_from_directory
from flask_restful import Resource
from werkzeug.utils import secure_filename

from fiCos.security.auth import jwt_required


class ImgItemResource(Resource):

    @jwt_required
    def post(self, current_user, id_item, position):
        if 'file' in request.files:
            file = request.files['file']
            extension = file.filename.split('.')
            newFilename = id_item + "_" + position + "." + "jpg"
            filename = secure_filename(file.filename)
            file.save(os.path.join('fiCos', current_app.config['UPLOAD_FOLDER'], newFilename))
            return make_response(
                jsonify({'ok': 'ok'}),
                201
            )

    @jwt_required
    def get(self, current_user, id_item, position):
        print("Maicon")
        return send_file(
            os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                id_item + "_" + position + ".jpg"
            ),
            mimetype='image/gif'
        )
