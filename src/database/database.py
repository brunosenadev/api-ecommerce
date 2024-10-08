from os.path import exists, join
from os import getcwd
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class Database:
    def __init__(self, app):
        self.db = SQLAlchemy(app)
    class User(SQLAlchemy.Model, UserMixin):
        id = SQLAlchemy.Column(SQLAlchemy.Integer, primary_key=True)
        username = SQLAlchemy.Column(SQLAlchemy.String(80), nullable=False, unique=True)
        password = SQLAlchemy.Column(SQLAlchemy.String(80), nullable=False)
        cart = SQLAlchemy.relationship('CartItem', backrefs="user", lazy=True)
    class Product(SQLAlchemy.Model):
        id = SQLAlchemy.Column(SQLAlchemy.Integer, primary_key=True)
        name = SQLAlchemy.Column(SQLAlchemy.String(120), nullable=False)
        price = SQLAlchemy.Column(SQLAlchemy.Float, nullable=False)
        description = SQLAlchemy.Column(SQLAlchemy.Text, nullable=True)
    class CartItem(SQLAlchemy.Model):
        id = SQLAlchemy.Column(SQLAlchemy.Integer, primary_key=True)
        user_id = SQLAlchemy.Column(SQLAlchemy.Integer, SQLAlchemy.ForeignKey('user.id'), nullable=False)
        product_id = SQLAlchemy.Column(SQLAlchemy.Integer, SQLAlchemy.ForeignKey('product.id'), nullable=False)

    def create_database(self):
        file_database = join(getcwd(), '..', '..', 'instance', 'ecommerce.self.db')
        if not exists(file_database):
            self.db.create_all()

    def commit_database(self, value, operation = 'add'):
        if operation == 'delete':
            self.db.session.delete(value)
        elif operation == 'add':
            self.db.session.add(value)
        self.db.session.commit()

        
    