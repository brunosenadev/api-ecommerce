from flask import Flask, request
from flask_cors import CORS
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from utils import json_format
from database import DatabaseClass
from product import ProductClass
from user import UserClass
from cart import CartClass

app = Flask(__name__)
app.config['SECRET_KEY'] = "my_key_python"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
database_class = DatabaseClass(db)
product_class = ProductClass(database_class)
user_class = UserClass(database_class)
cart_class = CartClass(database_class)
login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)

@login_manager.user_loader
def load_user(user_id):
    return user_class.returns_current_user(int(user_id))

@app.route('/login', methods=['POST'])
def route_login():
    data = request.json
    user_login = database_class.User.query.filter_by(username=data.get('username')).first()
    if user_login and data.get('password') == user_login.password:
            login_user(user_login)
            return json_format('Logged in successfully')
    return json_format('Unauthorized. Invalid credentials', 401)

@app.route('/logout', methods=['POST'])
@login_required
def route_logout():
    logout_user()
    return json_format('Logout successfully')

@app.route('/api/products/add', methods=['POST'])
@login_required
def route_add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        response = product_class.add_product(data['name'], data['price'], data.get('description', ''))
        return response
    return json_format('Invalid product data', 400)

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def route_delete_product(product_id):
    response = product_class.delete_product(product_id)
    return response

@app.route('/api/products/<int:product_id>', methods=['GET'])
def route_get_product_details(product_id):
    response = product_class.get_product_details(product_id)
    return response

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def route_update_product(product_id):
    data = request.json
    name = data.get('name', '')
    price = data.get('price', '')
    description = data.get('description', '')
    response = product_class.update_product(product_id, name, price, description)
    return response

@app.route('/api/products', methods=['GET'])
def route_get_all_products():
    response = product_class.get_all_products()
    return response

@app.route('/api/users/add', methods=['POST'])
def route_add_user():
    data = request.json
    response = user_class.add_user(data.get('username', ''), data.get('password', ''))
    return response

@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def route_add_to_cart(product_id):
    response = cart_class.add_to_cart(product_id, current_user.id)
    return response
        
@app.route('/api/cart/remove/<int:product_id>', methods=["DELETE"])
@login_required
def route_remove_from_cart(product_id):
    response = cart_class.delete_from_cart(product_id, current_user.id)
    return response

@app.route('/api/cart', methods=['GET'])
@login_required
def route_view_cart():
    response = cart_class.view_cart_items(int(current_user.id))
    return response

@app.route('/api/cart/checkout', methods=["POST"])
@login_required
def route_checkout():
    response = cart_class.checkout(int(current_user.id))
    return response

if __name__ == '__main__':
    with app.app_context():  
        database_class.create_database()
    app.run(debug=True, port=3333)