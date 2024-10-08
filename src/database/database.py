from main import app
from os.path import exists, join
from os import getcwd
from flask_sqlalchemy import SQLAlchemy

class Database():
    this.db = SQLAlchemy(app)

    class User(this.db.Model, UserMixin):
        id = this.db.Column(this.db.Integer, primary_key=True)
        username = this.db.Column(this.db.String(80), nullable=False, unique=True)
        password = this.db.Column(this.db.String(80), nullable=False)
        cart = this.db.relationship('CartItem', backrefs="user", lazy=True)
        
    class Product(this.db.Model):
        id = this.db.Column(this.db.Integer, primary_key=True)
        name = this.db.Column(this.db.String(120), nullable=False)
        price = this.db.Column(this.db.Float, nullable=False)
        description = this.db.Column(this.db.Text, nullable=True)
        
    class CartItem(this.db.Model):
        id = this.db.Column(this.db.Integer, primary_key=True)
        user_id = this.db.Column(this.db.Integer, this.db.ForeignKey('user.id'), nullable=False)
        product_id = this.db.Column(this.db.Integer, this.db.ForeignKey('product.id'), nullable=False)
    
    def create_database():
        file_database = f'{join(join(join(getcwd(), '..'), '..'), 'instance')}//ecommerce.db'
        if not exists(file_database):
            this.db.create_all()
        
    