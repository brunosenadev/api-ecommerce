from main import app
from os.path import exists, join
from os import getcwd
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy(app)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    cart = db.relationship('CartItem', backrefs="user", lazy=True)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

def create_database():
    file_database = f'{join(join(join(getcwd(), '..'), '..'), 'instance')}//ecommerce.db'
    if not exists(file_database):
        db.create_all()

def commit_database(value, operation = 'add'):
    if operation == 'delete':
        db.session.delete(value)
    elif operation == 'add':
        db.session.add(value)
    db.session.commit()

def config_database_uri(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
        
    