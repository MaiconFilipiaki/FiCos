from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from fiCos.ext.database import db

ma = Marshmallow()

def init_app(app):
    ma.init_app(app)
    Migrate(app, db)

