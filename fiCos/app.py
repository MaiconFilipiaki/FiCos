from flask import Flask

from fiCos.ext import configuration
from fiCos.ext import database
from fiCos.ext import commands
from fiCos.ext import presentation
from fiCos.ext import migration

from fiCos.blueprints.api import v1


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    commands.init_app(app)
    v1.init_app(app)
    presentation.init_app(app)
    return app
