from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    confirm_password = db.Column(db.String(150))
    