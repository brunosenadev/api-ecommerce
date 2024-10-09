from utils import json_format
from flask_login import login_user, logout_user

def make_login(username, password, user):
    user_login = user.query.filter_by(username=username).first()
    if user_login and password == user_login.password:
            login_user(user_login)
            return json_format('Logged in successfully')
    return json_format('Unauthorized. Invalid credentials', 401)

def make_logout():
    logout_user()
    return json_format('Logout successfully')