from flask_migrate import Migrate

from fiCos.ext.database import db

from fiCos.models.models import User

def init_app(app):

    @app.cli.command()
    def createdb():
        """Create db"""
        db.create_all()


    @app.cli.command()
    def populate_table_news():
        data = [
            User(id=1, name="Teste", email="asiofns"),
            User(id=2, name="Teste 1", email="asiofnsdnf")
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return User.query.all()

    @app.shell_context_processor
    def shell_context_processor():
        return dict(
            app=app,
            db=db,
            User=User,
        )