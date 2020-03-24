from flask import Flask

from fiCos.ext import configuration
from fiCos.ext import database
from fiCos.ext import commands
from fiCos.ext import presentation

from fiCos.blueprints import login

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    login.init_app(app)
    presentation.init_app(app)
    return app

