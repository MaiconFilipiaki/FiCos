from fiCos.ext.database import db
from fiCos.ext.migration import ma
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    usename = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User : {self.username} >'

class UserSchema(ma.Schema):
    class Meta:
        fields = 'id', 'username', 'email', 'password'
