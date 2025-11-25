from .models import User
from . import db

def get_all_users():
    return User.query.all()

def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user

    

