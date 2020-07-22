import os
import uuid
from flask import request, current_app, make_response, jsonify, send_file, send_from_directory
from flask_restful import Resource
from werkzeug.utils import secure_filename

from fiCos.ext.database import db

from fiCos.security.auth import jwt_required
from fiCos.models.models import Item, ImgItem


class ImgItemResource(Resource):

    @jwt_required
    def post(self, current_user, id_item):
        if 'file' in request.files:
            item_find = Item.query.filter_by(
                id=id_item
            ).first()
            if item_find is None:
                return jsonify({
                    "error": "Item not found"
                }), 404
            file = request.files['file']
            newFilename = id_item + "_" + uuid.uuid4().hex + ".jpg"
            file.save(os.path.join('fiCos', current_app.config['UPLOAD_FOLDER'], newFilename))
            new_img = ImgItem(
                nameImg=newFilename
            )
            item_find.imgs.append(new_img)
            db.session.add(new_img)
            db.session.commit()
            return make_response(
                jsonify({'nameImg': newFilename}),
                201
            )

    def get(self, id_item):
        return send_file(
            os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                id_item
            ),
            mimetype='image/gif'
        )

    @jwt_required
    def delete(self, current_user, id_item):
        img = request.args.get('img')
        img_register = ImgItem.query.filter_by(nameImg=img).first()
        if bool(img_register) is False:
            return jsonify({'error': 'Img not found'}), 404
        os.remove(os.path.join('fiCos', current_app.config['UPLOAD_FOLDER'], img_register.nameImg))
        db.session.delete(img_register)
        db.session.commit()
        return jsonify({ 'msg': 'Img deleted with success' })