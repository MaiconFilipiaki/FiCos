from flask import Flask

from fiCos.ext import configuration
from fiCos.ext import database
from fiCos.ext import commands

from fiCos.blueprints import restapi

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    restapi.init_app(app)
    return app

