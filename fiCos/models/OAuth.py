from flask_dance.consumer.backend.sqla import OAuthConsumerMixin

from fiCos.ext.database import db
from fiCos.models.User import User


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
