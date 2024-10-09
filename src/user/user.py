from utils import json_format

class UserClass:
    def __init__(self, db_class):
        self.commit_db = db_class.commit_database
        self.user_db = db_class.User
        
    def returns_current_user(self, user_id):
        return self.user_db.query.get(user_id)

    def add_user(self, username, password):
        if username != '' and password != '':
            user_added = self.user_db(username=username, password=password)
            self.commit_db(user_added)
            return json_format('User added successfully')
        return json_format('Invalid user data', 400)