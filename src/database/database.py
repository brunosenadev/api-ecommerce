from os.path import exists, join
from os import getcwd
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class DatabaseClass:
    def __init__(self, db):
        self.database = db
    
        class User(db.Model, UserMixin):
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(80), nullable=False, unique=True)
            password = db.Column(db.String(80), nullable=False)
            cart = db.relationship('CartItem', backref="user", lazy=True)
            
        class Product(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(120), nullable=False)
            price = db.Column(db.Float, nullable=False)
            description = db.Column(db.Text, nullable=True)
            
        class CartItem(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
            product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
        
        self.User = User
        self.Product = Product
        self.Cart = CartItem

    def create_database(self):
        file_database = join(getcwd(), '..', '..', 'instance', 'ecommerce.db')
        if not exists(file_database):
            self.database.create_all()

    def commit_database(self, value, operation = 'add'):
        if operation == 'delete':
            self.database.session.delete(value)
        elif operation == 'add':
            self.database.session.add(value)
        self.database.session.commit()


        
    