from database import User, commit_database
from utils import json_format

def returns_current_user(user_id):
    return User.query.get(user_id)

def add_user(username, password):
    if username != '' and password != '':
        user_added = User(username=username, password=password)
        commit_database(user_added)
        return json_format('User added successfully')
    return json_format('Invalid user data', 400)