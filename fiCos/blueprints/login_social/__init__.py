from flask_dance.contrib.facebook import make_facebook_blueprint

facebook_bp = make_facebook_blueprint()


def init_app(app):
    app.register_blueprint(facebook_bp, url_prefix='/login_social')
