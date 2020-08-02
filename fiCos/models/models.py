from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

from fiCos.ext.database import db


class User(db.Model, SerializerMixin):
    """ this user reference model """

    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    prompt_deliverys = db.relationship(
        'PromptDelivery',
        cascade="all,delete",
        backref='prompt_delivery',
        lazy='dynamic'
    )

    def __init__(self, username, email, password, prompt_deliverys):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.prompt_deliverys = prompt_deliverys

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User : {self.username} >'


class PromptDelivery(db.Model):
    __tablename__ = 'prompt_delivery'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    latitude = db.Column(db.Numeric(10,6))
    longitude = db.Column(db.Numeric(10,6))
    reach = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )
    items = db.relationship(
        'Item',
        backref='prompt_delivery',
        cascade="all,delete",
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<PromptDelivery: {self.name}>'


class Item(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    description = db.Column(db.String(84), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    descriptionComplet = db.Column(db.Text)
    categorie = db.Column(db.String(20))
    length_img = db.Column(db.Integer)
    prompt_delivery_id = db.Column(
        db.Integer,
        db.ForeignKey('prompt_delivery.id')
    )
    imgs = db.relationship(
        'ImgItem',
        backref='item',
        cascade="all,delete",
        lazy='dynamic'
    )


class ImgItem(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nameImg = db.Column(db.String(150), nullable=False)
    item_id = db.Column(
        db.Integer,
        db.ForeignKey('item.id')
    )
